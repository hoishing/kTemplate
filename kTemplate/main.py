#!/usr/bin/env python3

from functools import reduce
from functools import partial
from collections.abc import Callable
from typing import Unpack


TaggedElement = Callable[[str | list[str] | None, Unpack[dict]], str]
# """type alias of tagged element function"""


def attr2str(key: str, attrs: dict) -> str:
    """
    create attribute portion of an html element

    Examples:
        >>> # bool True -> key itself
        >>> attr2str(key="x", attrs={"x": True})
        ' x'

        >>> # bool False -> omit
        >>> attr2str(key="x", attrs={"x": False})
        ''
        >>> # not string nor `True`, eg. None -> omit
        >>> attr2str(key="x", attrs={"x": None})
        ''

        >>> # not string or `True`, eg. int -> omit
        >>> attr2str(key="x", attrs={"x": 1})
        ''

        >>> # empty str -> normal
        >>> attr2str(key="x", attrs={"x": ""})
        ' x=""'

        >>> # str -> normal
        >>> attr2str(key="x", attrs={"x": "y"})
        ' x="y"'

        >>> # convert attr underscore to hyphen
        >>> attr2str(key="data_y", attrs={"data_y": "y"})
        ' data-y="y"'

        >>> # convert attr name cls to class
        >>> attr2str(key="cls", attrs={"cls": "y"})
        ' class="y"'

    Note:
        to work around python naming restriction,
        the key `cls` will conver to `class`,
        and underscore `_` will convert to hyphen `-`

    Args:
        key (str): attribute key name
        attrs (dict): attribute key-value pairs of an element

    Returns:
        str: attribute portion of an element
    """
    attr = "class" if key == "cls" else key.replace("_", "-")

    match attrs[key]:
        case bool(x):
            return f" {attr}" if x else ""
        case str(x):
            return f' {attr}="{x}"'
        case _:
            return ""


def element(
    tag: str, content: str | list[str] | None = None, **attrs: Unpack[dict]
) -> str:
    """create html element with specific tag and attributes

    Examples:

        >>> # void element
        >>> element(tag="br")
        '<br />'

        >>> # void element w/ attr
        >>> element(tag="img", src="http://img.url")
        '<img src="http://img.url" />'

        >>> # empty string content
        >>> element(tag="script", content="", src="url")
        '<script src="url"></script>'

        >>> # element tree
        >>> element(tag="div", content=element("div", "x"))
        '<div><div>x</div></div>'

        >>> # mix text w/ element
        >>> element(tag="div", content=f'x{element("i", "y")}')
        '<div>x<i>y</i></div>'

        >>> # content w/ list of elements
        >>> element(
        ...     tag="div",
        ...     content=[element("br"), element("a", content="a link", href="url")]
        ... )
        '<div><br /><a href="url">a link</a></div>'

    Args:
        tag (str): element tag name
        content (str | list[str] | None, optional): Defaults to None.
            text or list of other elements, `None` returns element w/o closing tag
        **attrs (Unpack[dict]): html attributes in key-value pairs
            - if val is str, assign `key="val"`
            - `key=True` assign the key itself eg. selected, defer
            - key will be omitted if:
                val is not str nor `True`
                val=False (useful for omitting attr in loop or list comprehension)

    Returns:
        str: html element with specific tag and attributes
    """

    attr_str = reduce(lambda cum, key: cum + attr2str(key, attrs), attrs, "")

    # content-less `void` element with self closing tag
    if content is None:
        return f"<{tag}{attr_str} />"

    inner = "".join(content) if isinstance(content, list) else content
    return f"<{tag}{attr_str}>{inner}</{tag}>"


def create_elements(tags: str) -> list[TaggedElement]:
    """create tagged element functions

    Examples:
        >>> # single element
        >>> funcs = create_elements("div")
        >>> [f() for f in funcs]
        ['<div />']

        >>> # multiple elements
        >>> funcs = create_elements("a, br")
        >>> [f() for f in funcs]
        ['<a />', '<br />']

    Args:
        tags (str): names of functions to be created, comma separated
            eg. "a, br, div, span"

    Returns:
        list[TaggedElement]: list of tagged element functions
            eg. [a br div span]
    """
    return [partial(element, t.strip()) for t in tags.split(",")]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
