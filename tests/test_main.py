from kTemplate import create_elements, element, attr2str
import pytest
from typing import Any


@pytest.mark.parametrize(
    "input, expected",
    [
        # bool True -> key itself
        (dict(key="x", attrs={"x": True}), " x"),
        # bool False -> omit
        (dict(key="x", attrs={"x": False}), ""),
        # not string nor `True`, eg. None -> omit
        (dict(key="x", attrs={"x": None}), ""),
        # not string nor `True`, eg. int -> omit
        (dict(key="x", attrs={"x": 1}), ""),
        # empty str -> normal
        (dict(key="x", attrs={"x": ""}), ' x=""'),
        # str -> normal
        (dict(key="x", attrs={"x": "y"}), ' x="y"'),
        # convert attr underscore to hyphen
        (dict(key="data_y", attrs={"data_y": "y"}), ' data-y="y"'),
        # convert attr name cls to class
        (dict(key="cls", attrs={"cls": "y"}), ' class="y"'),
    ],
)
def test_attr2str(input: dict, expected: str):
    """test attr2str with different input combinations

    Args:
        input (dict): attr name; val: attr dict
        expected (str): generated attribute string portion
    """

    assert attr2str(**input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        # void element
        (dict(tag="br"), "<br />"),
        # void element w/ attr
        (dict(tag="img", src="http://img.url"), '<img src="http://img.url" />'),
        # empty string content
        (dict(tag="script", content="", src="url"), '<script src="url"></script>'),
        # element tree
        (dict(tag="div", content=element("div", "x")), "<div><div>x</div></div>"),
        # mix text w/ element
        (dict(tag="div", content=f'x{element("i", "y")}'), "<div>x<i>y</i></div>"),
        # content w/ list of elements
        (
            dict(
                tag="div",
                content=[element("br"), element("a", content="a link", href="url")],
            ),
            '<div><br /><a href="url">a link</a></div>',
        ),
    ],
)
def test_element(input, expected):
    assert element(**input) == expected


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
