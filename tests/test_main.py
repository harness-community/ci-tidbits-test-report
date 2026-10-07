"""Pytest cases for the test-and-report demo.

These tests are intentionally green. Flip an assertion locally if you want
to rehearse a red build that still publishes XML to the Tests tab.
"""

from app.main import APP_NAME, add, greeting


def test_greeting_names_the_demo():
    assert APP_NAME in greeting()


def test_greeting_mentions_junit():
    assert "JUnit XML" in greeting()


def test_add_sums_integers():
    assert add(2, 3) == 5
