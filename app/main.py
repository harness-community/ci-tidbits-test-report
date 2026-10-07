"""Entrypoint for the test-and-report demo.

The pipeline does not build an image. It runs Pytest against this module
and publishes the JUnit XML report to the Harness Tests tab.
"""

APP_NAME = "tidbits-test-report-demo"
VERSION = "1.0.0"


def greeting() -> str:
    return f"{APP_NAME} {VERSION} — unit tests published as JUnit XML"


def add(left: int, right: int) -> int:
    """Tiny pure function so the suite has more than string asserts."""
    return left + right


if __name__ == "__main__":
    print(greeting())
