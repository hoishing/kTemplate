When building web apps with python, no matter using which framework, Flask, FastAPI, Django...etc. The go-to template is [Jinja][jinja]. In many cases, using Jinja for simple web app is just over-kill. Also, I am not the fan of its template syntax, I feel a bit clumsy putting python  loops in html with `{% ... %}` like this:

```html
<ul id="navigation">
{% for item in navigation %}
    <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
{% endfor %}
</ul>
```

in contrast, I prefer something like this:

```python
ul(
  id = "navigation",
  content = [
    li(
      a(item.caption, href=item.href)
    )
    for item in navigation
  ]  
)
```

Its pure python, having full support of intellisense, type checking, and all language supports from the IDE / text editor. So in general I feel better DX with this approach.

Separation of concern sounds good, but it comes with a cost of adding an extra layer of concern, ie. complexity. So separating HTML with python is not always a good choice. That's why people invented JSX in javascript, or prefer Tailwind over separate CSS file.

Mixing template logic within python reduces that layer of complexity, which I think is a reasonable choice for small/medium size projects. There are libs provide html template within python, such as [Dominate][dominate] and [fast-html][fast-html].

Dominate is a well designed lib and I'll certainly go for it for medium sized project. Their `with element_name` pattern is a brilliant use of python context manager, highly recommended 👍 However, for small project, I still looking for a simpler solution.

fast-html come close to what I want. It uses python `generator` as element output to speed up the template concatenation process. This is a efficient technical choice, and I think that's why the author name it "fast" html. But still, when dealing with small or even single page demo sites, pure text elements is what I am looking for instead of generator. Performance hit of pure text manipulation in small projects is negligible.

Thats why I create this text centric html template lib and share it on PyPi. I name it "k" template after my name, that is 😜. Hope u find it useful.

[jinja]: https://jinja.palletsprojects.com
[fast-html]: https://pypi.org/project/fast-html
[dominate]: https://pypi.org/project/dominate
