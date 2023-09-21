import queue
import subprocess
import threading
from pathlib import Path
from subprocess import Popen
from typing import Optional, IO, Union

from .buffered_line_reader import BufferedLineReader
from .matcher import Matcher


class ReaderThread(threading.Thread):
    def __init__(self, process_stdout: IO[str]):
        super().__init__()
        self._process_stdout: IO[str] = process_stdout
        self.stream = queue.Queue()

        self.daemon = True
        self.start()

    def run(self):
        while True:
            read_character = self._process_stdout.read(1)

            print(read_character, end='')  # Print it out so the students can see what's going on
            self.stream.put(read_character)

            if read_character == '':  # EOF
                # Currently safe to print, and it's put into the stream above so downstream readers know we're done.
                return


class SubprocessControl:
    def __init__(self, process: Popen[str]):
        self._process = process
        self._stdout_reader_thread = ReaderThread(self._process.stdout)
        self._line_reader = BufferedLineReader(self._stdout_reader_thread.stream)
        self._matcher = Matcher(self._line_reader.lines)

    @property
    def matcher(self) -> Matcher:
        return self._matcher

    @property
    def is_running(self) -> bool:
        return self._process is not None and self._process.poll() is None

    def terminate(self):
        self._process.stdin.close()  # Close off our input stream to the program
        self._process.terminate()
        self._process.wait(
            5)  # Wait 5 seconds for the program to die. If it's not dead by then, an exception is raised.

    def __guard_no_process(self):
        if self._process is None:
            raise Exception("There is no process, did you use this class in a `with` block?")

    def println(self, line: Union[str, int]):
        self.print(f"{line}\n")

    def print(self, line: str):
        print(line, end='')  # Print it for the student
        self.__guard_no_process()
        self._process.stdin.write(line)
        self._process.stdin.flush()


class SubprocessRunner:
    def __init__(self, cwd: Path, args):
        self._cwd = cwd
        self._args = args
        self._control: Optional[SubprocessControl] = None

    def __enter__(self) -> SubprocessControl:
        self._control = SubprocessControl(Popen(self._args,
                                                shell=False,
                                                stdin=subprocess.PIPE,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.STDOUT,
                                                cwd=self._cwd,
                                                text=True,
                                                encoding="utf-8",
                                                ))
        return self._control

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            raise exc_val
        self._control.terminate()


class GradleRunner(SubprocessRunner):
    def __init__(self, project_dir: Path):
        self._project_dir = project_dir
        args = [
            str(project_dir / "gradlew"),
            "run",
            "--quiet",
            "--console=plain",
        ]
        print(args)

        super().__init__(project_dir, args)
