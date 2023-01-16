from kTemplate import create_elements
import pytest


@pytest.mark.parametrize(
    "input, outputs",
    [
        # single element
        ("div", ["<div />"]),
        # multiple elements
        ("a, br", ["<a />", "<br />"]),
    ],
)
def test_create_elements(input, outputs):
    funcs = create_elements(tags=input)
    for i, f in enumerate(funcs):
        assert f() == outputs[i]
