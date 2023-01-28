## Installation

`pip install kTemplate`

Pure python package, zero dependency.

## Common HTML Elements

- common elements(div, span, a, img ...etc) can be imported directly

    eg. `#!py from kTemplate import div, span, a, img`

- see list of common HTML elements [here][common_ele]
- rare or custom element could be created by the `element` function

    eg. `#!py element(tag='MyTag', content='foo', href='bar')`

    → `#!html <MyTag href="bar">foo</MyTag>`

## Custom Elements

We use `element` function to create custom HTML elements. Usage of the function arguments is illustrated below.

### tag

required: name of the custom tag.

### content

- `content=None` (default value) create void element such as: `br`, `hr`, `img`, `meta` ... etc

    eg. `br()` → `#!html <br />`

- empty string `content=""` creates element with end tag but no content.

    eg `script(content="")` → `<script></script>`

- since elements are just text, it can interpolate with other text

    eg. `content=f"this {i('is')} good"` →  `#!html this <i>is</i> good`

- use `list` to create multiple child elements

    eg. `div(content=[br(), hr()])` → `#!html <div><br /><hr /></div>`

### *args

variable non-keyword arguments will be converted to element attributes without values. eg. `defer`, `option`

It is useful when working with UnoCSS [attributify mode][attributify], you can assign CSS utility classes directly as attributes. eg.

```python
div(None, 'm-2', 'rounded', 'text-teal-400')
```

returns

```html
<div m-2 rounded text-teal-400 />
```

### **kwargs

variable keyword arguments

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

## Templates and Components

You can create HTML templates and components with the same mechanism of creating elements.

```python
from kTemplate import div, h2, hr, DOCTYPE, html, head, script, body


def template(slot: str) -> str:
    """html template with slot"""
    return DOCTYPE + html(
        [
            # UnoCSS
            head(script("", src="https://cdn.jsdelivr.net/npm/@unocss/runtime")),
            body(slot),
        ]
    )


def component(name: str, age: int, slot1: str, slot2: str = ""):
    """component with props and slots"""
    return div(
        [
            h2(f"Hi {name} 🚀", cls="bg-orange-300 rounded"),
            div(f"I am {age} ~", cls="m-2 rounded text-teal-400"),
            slot1,
            hr(),
            slot2,
        ]
    )


with open("index.html", "w") as f:
    html = template(component("Kelvin", 42, div("Good Day 🍀")))
    f.write(html)
```

then the following HTML will be created(without indents and line breaks):

```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/@unocss/runtime"></script>
  </head>
  <body>
    <div>
      <h2 class="bg-orange-300 rounded">Hi Kelvin 🚀</h2>
      <div class="m-2 rounded text-teal-400">I am 42 ~</div>
      <div>Good Day 🍀</div>
      <hr />
    </div>
  </body>
</html>
```

[common_ele]: https://github.com/hoishing/kTemplate/blob/main/kTemplate/elements.py
[attributify]: https://github.com/unocss/unocss/tree/main/packages/preset-attributify/
