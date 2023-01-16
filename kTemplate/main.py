from functools import reduce
from functools import partial
from collections.abc import Callable
from typing import Unpack


TaggedElement = Callable[[str | list[str] | None, Unpack[dict]], str]
"""type alias of tagged element function"""


def attr2str(key: str, attrs: dict) -> str:
    """
    create attribute portion of an html element

    Examples:

        - str -> str
        >>> attr2str(key="x", attrs={"x": "y"})
        ' x="y"'

        - empty str -> empty str
        >>> attr2str(key="x", attrs={"x": ""})
        ' x=""'

        - non str truthy -> key itself
        >>> attr2str(key="x", attrs={"x": True})
        ' x'
        >>> attr2str(key="x", attrs={"x": 1})
        ' x'

        - non str falsy -> omit
        >>> attr2str(key="x", attrs={"x": False})
        ''
        >>> attr2str(key="x", attrs={"x": None})
        ''
        >>> attr2str(key="x", attrs={"x": 0})
        ''

        - convert attr underscore to hyphen
        >>> attr2str(key="data_y", attrs={"data_y": "y"})
        ' data-y="y"'

        - convert attr name cls to class
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
    val = attrs[key]

    if isinstance(val, str):
        return f' {attr}="{val}"'

    return f" {attr}" if val else ""


def element(tag: str, content: str | list[str] = None, **attrs) -> str:
    """create html element with specific tag and attributes

    Examples:

        - void element, content=None (default)
        >>> element(tag="br")
        '<br />'

        - void element w/ attr
        >>> element(tag="img", src="http://img.url")
        '<img src="http://img.url" />'

        - empty string content -> element with end tag but no content
        >>> element(tag="script", content="", src="url")
        '<script src="url"></script>'

        - non-string truthy attrubite -> return attribute key itself
        >>> element(tag="option", content="a", selected=True)
        '<option selected>a</option>'

        - non-string falsy attrubite -> attribute omitted
        >>> element(tag="option", content="a", selected=False)
        '<option>a</option>'

        - element tree
        >>> element(tag="div", content=element("div", "x"))
        '<div><div>x</div></div>'

        - mix text w/ element
        >>> element(tag="div", content=f'x{element("i", "y")}')
        '<div>x<i>y</i></div>'

        - content w/ list of elements -> elements in list are siblings
        >>> element(
        ...     tag="div",
        ...     content=[element("br"), element("a", content="a link", href="url")]
        ... )
        '<div><br /><a href="url">a link</a></div>'

    Args:
        tag (str): element tag name
        content (str | list[str], optional): Defaults to None.
            text or list of other elements, `None` returns element w/o closing tag
        attrs (dict): key-value pairs of html attributes
            - if val is str, assign `key="val"`
            - if key is non-string truthy, assign the key itself, eg.
                - selected=True -> selected
                - defer=1 -> defer
            - if key is non-str falsy, the key is omitted
                - eg. <option selected=
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

    Notes:
        This is a higher order function that returns a list of functions

    Examples:

        - single element
        >>> funcs = create_elements("div")
        >>> [f() for f in funcs]
        ['<div />']

        - multiple elements
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
