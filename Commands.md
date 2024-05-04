# Create virtual environment

    > python -m venv env

&nbsp;

# Activate virtual environment

    > & env_name\Scripts\Activate.ps1

&nbsp;

## Example

    ```md
    & env_name\Scripts\Activate.ps1

    ```

&nbsp;

# import the **streamlit**

    > import streamlit as st

&nbsp;

# Run application

    > streamlit run filename

&nbsp;

# Check the Streamlit Version using Terminal

    > streamlit --version

&nbsp;

# Check the Streamlit Version using the pip

    > pip freeze

&nbsp;

# Add title

    > st.title("message")

It is recommended to use `title` only once

&nbsp;

# Add headers

    > st.header("Header")

&nbsp;

# Add sub header

    > st.subheader("Sub Header")

&nbsp;

# Add text

    > st.text("text")

&nbsp;

# Using write function, we can also display code in coding format. This is not possible using `st.text(”)`.

    > st.write("Text with write")

    > st.write(range(10))

# Add markdown

    > st.markdown("### This is a markdown")

# Add Error message

    > st.error("Error message")

# Add Success message

    > st.success("Success message")

# Add Information

    > st.info("information")

# Add Warning

    > st.warning("Warning")

# Exception - This has been added later

    > exp = ZeroDivisionError("Trying to divide by Zero") <br> st.exception(exp)

# Select box

## Syntax :

```py
st.selectbox("option1", "option2",...)
```

## Example :

```py
# first argument takes the titleof the selectionbox

# second argument takes options

hobby = st.selectbox("Hobbies: ",
['Dancing', 'Reading', 'Sports'])

# print the selected hobby

st.write("Your hobby is: ", hobby)
```

&nbsp;

# Multi-Selectbox

## Syntax :

```py
st.multiselect("1",['2','3'])

```

## Example :

```py
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')
```

# Add Sidebar with selectbox

    > st.sidebar.selectbox("name",[values])

# Add Sidebar with radio

    ```py
    st.sidebar.radio("Files",[])
    ```

    ## Example

    ```md
    # radio button

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

# User input (number)

    ```md
     st.number_input("Enter a number", start_value, end_value)
    ```

&nbsp;

# User input (text)

    ```md
     st.text_input("Enter your name")
    ```

&nbsp;

# User input (date)

    > st.text_input("Enter a date")

&nbsp;
&nbsp;
&nbsp;

# Add checkbox

A checkbox returns a boolean value. When the box is checked, it returns a True value else returns a False value.

# Syntax :

```md
st.checkbox("Value")
```

## Example:

```md
# check if the checkbox is checked

# title of the checkbox is 'Show/Hide'

if st.checkbox("Show/Hide"): # display the text if the checkbox returns True value
st.text("Showing the widget")
```

&nbsp;

# To write a caption

## Syntax :

```md
st.caption("Caption")
```

&nbsp;

# Add a button

`st.button()` returns a boolean value. It returns a True value when clicked else returns False.

## Syntax :

```py
st.button("button value")
```

## Example :

```py
# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")

```

&nbsp;

# Split page using columns width

    ```py
     st.columns([60, 40])
    ```

&nbsp;

# Split page using number of columns

    ```py
    st.columns(number)
    ```

&nbsp;

# Display image

    ```md
    # import Image from pillow to open images

    from PIL import Image
    img = Image.open("streamlit.png")

    # display image using streamlit

    # width is used to set the width of an image

    st.image(img, width=200)
    ```

&nbsp;

# Slider

## Syntax :

```py
st.slider("Select the level", 1, 5)
```

## Example :

```py
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
&nbsp;

Run Django

> python manage.py runserver

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
&nbsp;
