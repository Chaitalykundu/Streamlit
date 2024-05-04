# st.write

This is the `Swiss Army knife` of Streamlit commands.

It does different things depending on what you throw at it.

&nbsp;

Unlike other Streamlit commands, `write()` has some unique properties:

* It accepts multiple arguments.

* It supports various datatypes. Its behavior depends on the input types as follows.

* It returns None, so its "slot" in the App cannot be reused.

&nbsp;

&nbsp;

## Syntax

```py
st.write(*args, unsafe_allow_html=False, **kwargs)
```

&nbsp;

&nbsp;

## Parameters

`st.write()` can have the following arguments:

1. args (any)
2. unsafe_allow_html (bool)

&nbsp;

&nbsp;

## Example

### String

```py
import streamlit as st
st.write('Hello World! :heart:')

# O.P.: Hello World! ❤️
```

&nbsp;

### Markdown

```py
st.write('''
This is markdown
''')
```

&nbsp;

### Multiple arguments (string,number)

```py
st.write("1+1=",1+1)
```

&nbsp;

### DataFrame

```py
df = pd.DataFrame({"First column":[1,2,3],"Second Column":[4,5,6]})
st.write(df)
```

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
