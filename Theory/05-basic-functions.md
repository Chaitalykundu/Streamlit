# Overview

- [Overview](#overview)
- [1. Title](#1-title)
  - [Output](#output)
- [2. Header](#2-header)
  - [Output](#output-1)
- [3. Subheader](#3-subheader)
  - [Output](#output-2)
- [4. Text](#4-text)
- [5. Write](#5-write)
  - [st.text vs st.write](#sttext-vs-stwrite)
- [6. Markdown](#6-markdown)
- [5. Success, Info, Warning, Error, Exception](#5-success-info-warning-error-exception)
- [7. Display Images](#7-display-images)
- [8. Checkbox](#8-checkbox)
- [9. Radio Button](#9-radio-button)
- [10. Selection Box](#10-selection-box)
- [11. Multi-Selectbox](#11-multi-selectbox)
- [12. Button](#12-button)
- [13. Text Input](#13-text-input)
- [14. Slider](#14-slider)

&nbsp;

&nbsp;

&nbsp;

# 1. Title

Used for the main title of the app.

```py
st.title("Hello!!!")
```

&nbsp;

### Output

- Largest heading
- Usually used once at the top

&nbsp;

&nbsp;

# 2. Header

Used for section headings inside the app.

```py
# Header
st.header("This is a header")
```

&nbsp;

### Output

- Smaller than title
- Bigger than normal text

&nbsp;

&nbsp;

# 3. Subheader

`st.subheader()` is used for smaller section titles inside a header.

```py
# Subheader
st.subheader("This is a subheader")
```

&nbsp;

### Output

- smaller than st.header()
- bigger than normal text

&nbsp;

&nbsp;

| Function         | Purpose            | Size    |
| ---------------- | ------------------ | ------- |
| `st.title()`     | Main app title     | Largest |
| `st.header()`    | Section heading    | Medium  |
| `st.subheader()` | Subsection heading | Smaller |
| `st.write()`     | Normal text        | Normal  |

&nbsp;

&nbsp;

# 4. Text

Used for displaying plain fixed text.

It:

- shows text exactly as written,
- uses monospace formatting,
- does not format markdown.

&nbsp;

```py
# Text
st.text("Hello GeeksForGeeks!!!")
```

&nbsp;

&nbsp;

# 5. Write

`st.write()` is more flexible.

Using `write` function, we can also display code in coding format. This is not possible using `st.text()`

&nbsp;

```py
# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))
```

&nbsp;

It can display:

- text,
- markdown,
- tables,
- dataframes,
- variables,
- charts,
- lists,
- dictionaries.

&nbsp;

&nbsp;

## st.text vs st.write

| Feature            | `st.text()` | `st.write()` |
| ------------------ | ----------- | ------------ |
| Plain text         | ✅          | ✅           |
| Markdown support   | ❌          | ✅           |
| DataFrames         | ❌          | ✅           |
| Lists/Dictionaries | ❌          | ✅           |
| Variables          | Limited     | ✅           |
| Most commonly used | ❌          | ✅           |

&nbsp;

&nbsp;

# 6. Markdown

Markdown is specially used to add html code in streamlit.

```py
# Markdown
st.markdown("### This is a markdown")
```

&nbsp;

&nbsp;

# 5. Success, Info, Warning, Error, Exception

```py
# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
```

&nbsp;

# 7. Display Images

```py

# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)
```

&nbsp;

# 8. Checkbox

A checkbox returns **a boolean value**. When the box is checked, it returns a True value else returns a False value.

```py
# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")
```

&nbsp;

# 9. Radio Button

```py
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
```

&nbsp;

# 10. Selection Box

```py
# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)
```

&nbsp;

# 11. Multi-Selectbox

The multi-select box returns the output in the form of a list. You can select multiple options.

```py
# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')
```

&nbsp;

# 12. Button

`st.button()` returns a boolean value. It returns a True value when clicked else returns False.

```py

# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")
```

&nbsp;

# 13. Text Input

```py
# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
```

&nbsp;

# 14. Slider

```py
# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))
```

&nbsp;
&nbsp;
&nbsp;

```

```
