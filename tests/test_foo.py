# Must invoke via python3 -m pytest due to relative local import
import pytest
from foo import foo


@pytest.mark.parametrize(
    ("v", "expected"),
    [
        (0, "foo(0)"),
        (12, "foo(12)"),
        ("bar", "foo(bar)"),
        (None, "foo(None)"),
    ],
)
def test_foo(v: int | str | None, expected: str):
    assert foo(v) == expected
