from functools import reduce
from functools import partial


def attr2str(key: str, attrs: dict) -> str:
    """create attribute string for element"""
    # work around python naming restriction: `class` and hyphen, in html attributes
    attr = "class" if key == "cls" else key.replace("_", "-")

    match attrs[key]:
        case bool(x):
            return f" {attr}" if x else ""
        case str(x):
            return f' {attr}="{x}"'
        case _:
            return ""


def element(tag: str, content: str | list[str] | None = None, **attrs) -> str:
    """return html element for specific tag and attributes
    content: text or list of other elements, empty str returns element w/o closing tag
    attrs: assign html attributes in key-value pairs
        if val is str, assign `key="val"`
        `key=True` assign the key itself eg. selected, defer
        key will be omitted if
            val is not str nor bool type
            val=False (useful for omitting attr in loop or list comprehension)
    """

    attr_str = reduce(lambda cum, key: cum + attr2str(key, attrs), attrs, "")

    # content-less `void` element with self closing tag
    if content is None:
        return f"<{tag}{attr_str} />"

    inner = "".join(content) if isinstance(content, list) else content
    return f"<{tag}{attr_str}>{inner}</{tag}>"


def create_elements(tags: str):
    """a higher order function that create html element functions dynamically
    tags: string contains elements that are comma seperated, spaces will be stripped, eg. "div, i, span"
    returns: list of element functions
    """
    return [partial(element, t.strip()) for t in tags.split(",")]
