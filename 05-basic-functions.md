# 1. Title:

```py
st.title("Hello!!!")
```

&nbsp;

# 2. Header and Subheader:

```py
# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")
```

&nbsp;

# 3. Text:

```py
# Text
st.text("Hello GeeksForGeeks!!!")
```

&nbsp;

# 4. Markdown:

Markdown is specially used to add html code in streamlit.


```py
# Markdown
st.markdown("### This is a markdown")
```

&nbsp;

# 5. Success, Info, Warning, Error, Exception:

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

# 6. Write:

Using `write` function, we can also display code in coding format. This is not possible using `st.text(”)`

```py

# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))
```

&nbsp;

# 7. Display Images:

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

# 8. Checkbox:

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

# 9. Radio Button:

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

# 10. Selection Box:

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

# 11. Multi-Selectbox:

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

# 12. Button:

`st.button()` returns a boolean value. It returns a True value when clicked else returns False.

```py

# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")
```

&nbsp;

# 13. Text Input:

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

# 14. Slider:

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
