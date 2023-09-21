import queue
import threading
from queue import Queue


class BufferedLineReader(threading.Thread):
    def __init__(self, character_stream: Queue):
        super().__init__()
        self._character_stream = character_stream
        self.lines = queue.Queue()
        self._current_line = ''

        self.daemon = True
        self.start()

    def run(self):
        while True:
            try:
                read_character = self._character_stream.get(timeout=0.1)  # Wait max 100 ms. Testing was like ~300 us
            except queue.Empty:
                # Hopefully, this is a line where we're waiting for input on the Java program side
                self._maybe_send_line()

                continue

            self._current_line += read_character

            if read_character == '\n':  # Newline terminated strings should
                self._maybe_send_line()
            elif read_character == '':  # Input stream hit EOF
                self._maybe_send_line()
                self.lines.put('')  # Force send EOF downstream

    def _maybe_send_line(self):
        if len(self._current_line) == 0:
            return  # Nothing to send

        self.lines.put(self._current_line)
        self._current_line = ''
