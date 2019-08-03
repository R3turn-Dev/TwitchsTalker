from typing import Any, Optional


class InvalidArgumentTypeError(BaseException):
    passed: Any
    expected: str
    message: str

    def __init__(
            self,
            passed,
            expected: Optional[str]=None,
            message: Optional[str]=None,
            ):
        self.passed = passed
        self.expected = expected
        self._message = message

    @property
    def message(self):
        return self._message or "Unexpected type of argument passed (Expected: {}, Passed: {})".format(
            self.expected,
            type(self.passed)
            )
