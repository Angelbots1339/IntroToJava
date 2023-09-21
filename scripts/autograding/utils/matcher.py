from queue import Queue, Empty


class Matcher:
    def __init__(self, line_queue: Queue):
        self._line_queue = line_queue
        self._timeout_seconds = 60  # We'll wait up to 60 seconds for the next line.
        self._case_sensitive = False  # Will we ignore capital vs lower case letters on matching

    def timeout(self, timeout_seconds) -> 'Matcher':
        self._timeout_seconds = timeout_seconds
        return self

    def case_sensitive(self, case_sensitive=True) -> 'Matcher':
        self._case_sensitive = case_sensitive
        return self

    def case_insensitive(self) -> 'Matcher':
        return self.case_sensitive(False)

    def wait_until_input_needed(self) -> 'Matcher':
        while True:
            try:
                line = self._fetch_line()
            except Empty:
                raise Exception(
                    "Failed waiting for input. Make sure you're not sending a newline before waiting for input.")

            if line[-1] != '\n':  # If we see a newline, we're not waiting for input (within our expected parameters)
                break

        return self

    @property
    def next_line(self) -> str:
        try:
            return self._fetch_line()
        except Empty:
            raise Exception("Could not get next line within timeout")

    def match(self, match_string: str) -> 'Matcher':
        while True:
            try:
                line = self._fetch_line()
            except Empty:
                raise Exception(f"Unable to match line within timeout: {match_string}")

            if match_string in line:  # Todo case sensitive
                break

        return self

    def _fetch_line(self) -> str:
        line = self._line_queue.get(timeout=self._timeout_seconds)
        if line == '':
            raise Exception("Unexpectedly reached the end of the program")
        return line
