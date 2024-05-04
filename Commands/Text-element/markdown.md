# st.markdown

Display string formatted as Markdown.

&nbsp;

&nbsp;

## Syntax

```py
st.markdown(body, unsafe_allow_html=False, *, help=None)
```

&nbsp;

&nbsp;


## Parameters

1. body (str)
2. unsafe_allow_html (bool)
3. help (str)

&nbsp;


### body (str)

The string to display as Github-flavored Markdown.

```py
st.markdown("Hello World! *Streamlit* is **really** ***Cool***")
```

&nbsp;

This also supports:

* **Emoji shortcodes** such as `:+1:` and `:sunglasses:`

    ```py
    st.markdown(":+1: :sunglasses: :heart:")
    ```

* **LaTeX expressions** by wrapping them in `"$"` or `"$$"`

    ```py
    st.markdown("$Hello$")
    ```

* **Colored text** using the syntax `:color[text to be colored]`

    ```py
    st.markdown(":green[This is green text]")
    ```

&nbsp;

### unsafe_allow_html (bool)

By default, any HTML tags found in the body will be escaped and therefore treated as pure text. This behavior may be turned off by setting this argument to True.

&nbsp;

### Help (str)

An optional tooltip that gets displayed next to the Markdown.

&nbsp;

&nbsp;
&nbsp;

&nbsp;
&nbsp;

&nbsp;
&nbsp;

&nbsp;
&nbsp;

&nbsp;
