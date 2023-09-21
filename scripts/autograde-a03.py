import enum
from pathlib import Path
from typing import Dict

from autograding.utils.subprocess_runner import GradleRunner, SubprocessControl


class Result(enum.Enum):
    TOO_LOW = enum.auto()
    TOO_HIGH = enum.auto()
    CORRECT = enum.auto()


class GamePlayer:
    def __init__(self, root_path: Path, be_thorough: bool):
        self.root_path = root_path
        self._be_thorough = be_thorough
        self.results: Dict[int, Result] = {}
        self._min: int = 1
        self._max: int = 1000

    def run(self):
        with GradleRunner(self.root_path) as control:
            while True:
                target = (self._min + self._max) // 2
                result = self._play_game_with_number(control, target)

                match result:
                    case Result.TOO_LOW:
                        self._ensure_range(control, Result.TOO_LOW, range(self._min, target))
                        self._min = target
                    case Result.TOO_HIGH:
                        self._ensure_range(control, Result.TOO_HIGH, range(target + 1, self._max + 1))
                        self._max = target
                    case Result.CORRECT:
                        return  # Success! You did it! Sadly, we can't check any other numbers now as the program is done

    def _play_game_with_number(self, control: SubprocessControl, number: int) -> Result:
        control.matcher.wait_until_input_needed()
        control.println(number)
        next_line = control.matcher.next_line.lower()
        if 'too high' in next_line:
            self.results[number] = Result.TOO_HIGH
        elif 'too low' in next_line:
            self.results[number] = Result.TOO_LOW
        elif 'correct' in next_line:
            self.results[number] = Result.CORRECT
        else:
            raise Exception("Could not find expected high/low/correct in program output.")

        return self.results[number]

    def _ensure_range(self, control: SubprocessControl, expected_result: Result, target_range: range):
        if not self._be_thorough:
            return

        for i in target_range:
            if i in self.results:  # Already calculated, ignored
                continue

            result = self._play_game_with_number(control, i)
            self.results[i] = result
            if result != expected_result:
                raise Exception(f"Got {result} for {i} when we expected {expected_result}")


def main():
    program_root_path = Path.cwd()

    print("Running fast game")
    GamePlayer(program_root_path, False).run()  # Fast game

    print("Running slow, thorough game")
    GamePlayer(program_root_path, True).run()  # Slow, thorough game


if __name__ == '__main__':
    main()
