## Installation

`pip install kTemplate`

Pure python package, zero dependency.

## Tagged Element Functions

- common elements(div, span, a, img ...etc) can be imported directly

    eg. `#!py from kTemplate import div, span, a, img`

- see list of common elements [here][common_ele]
- rare or custom element could be created by the `element` function

    eg. `#!py element(tag='MyTag', content='foo', href='bar')`

    → `#!html <MyTag href="bar">foo</MyTag>`

## Element Function

To create uncommon or custom tags, `element` function can be used. Below explains the use of function arguments.

### tag

required: name of the custom tag.

### content

- `content=None`, which is the default value, create void element.

    void element examples: br, hr, img, meta ... etc

    eg. `br()` → `#!html <br />`

- empty string `content=""` creates element with end tag without content.

    eg `content=script(content="")` → `<o></script>`

- can mix other elements with text.

    eg. `content=f"this {i('is')} good"` →  `#!html this <i>is</i> good`

- use `list` to create multiple child elements

    eg. `div(content=[br(), hr()])` → `#!html <div><br /><hr /></div>`

### *args

Optional positional arguments. They will be converted into tag attributes without values. eg. `defer`, `option`

An other use case is working with UnoCSS [attributify mode][attributify], which you can assign CSS utility classes directly as tag attributes. eg.

```python
div(None, 'm-2', 'rounded', 'text-teal-400')
```

returns

```html
<div m-2 rounded text-teal-400 />
```

### **kwargs

- string, included empty string `""` create string attributes
- non-string truthy value create empty attribute

    eg. `#!py option("foo", selected=True)` -> `#!py <option selected>foo</option>`

- attribute is omitted for non-string falsy value(`None`, `False`, `[]`, `0` ...etc)

    eg. `#!py option("bar", selected=False)` -> `#!py <option>bar</option>`

## Example

The following example demonstrate the key features provided by kTemplate. See [References](./ref.md) for full documentation.

```python
from kTemplate import (
    DOCTYPE,  # special non-element
    html,
    div,
    img,
    body,
    head,
    title,
    script,
    select,
    option,
)
from kTemplate import element  # for creating custom element


html_str = DOCTYPE + html(
    [
        head(
            # use list to enclose multiple siblings
            [
                title("testing html template"),
                
                # attr=True will convert to attribute w/o value, eg. defer
                script(
                    src="https://cdn.jsdelivr.net/npm/@unocss/runtime/attributify.global.js",
                    defer=True
                ),
            ]
        ),
        body(
            [
                # content-less element without closing tag
                img(src="http://placekitten.com/150/100"),

                # cls attribute will convert to `class`
                div("pls select the direction:", cls="text-xl"),
                select(
                    # attr selected showup when selected=True, otherwise omitted
                    [
                      option(dir, selected=(dir == "South"))
                      for dir in "East South West North".split()
                    ]
                    # underscore will convert to hyphen, eg. `data-type`
                    data_type="direction"  
                ),

                # create custom element
                element(tag="MyElement", props="some-props")
            ],
            cls="font-sans",
        ),
    ]
)
```

Note that in order to workaround python naming constrains:

- `class` attribute denoted by `cls`
- underscore `_` will be converted to hyphen `-`

[common_ele]: https://github.com/hoishing/kTemplate/blob/main/kTemplate/elements.py
[attributify]: https://github.com/unocss/unocss/tree/main/packages/preset-attributify/
