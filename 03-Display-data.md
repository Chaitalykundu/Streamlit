# Display and style data

There are a few ways to display data (tables, arrays, data frames) in Streamlit apps. Below, you will be introduced to `magic` and `st.write()`, which can be used to write anything from text to tables. After that, let's take a look at methods designed specifically for visualizing data.

&nbsp;

&nbsp;

## Use magic

You can also write to your app without calling any Streamlit methods. Streamlit supports `"magic commands"`, which means you don't have to use `st.write()` at all! To see this in action try this snippet:

&nbsp;

* Example : dataframe

&nbsp;

```py
import streamlit as st
import pandas as pd

df = {"first column":[1,2,3,4,5], "second column":[9,8,7,6,5]}

df = pd.DataFrame(df)
df 
```

Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using `st.write()`

&nbsp;

&nbsp;

&nbsp;

## Other data specific functions

There are other data specific functions like `st.dataframe()` and `st.table()` that you can also use for displaying data. Let's understand when to use these features and how to add colors and styling to your data frames.

&nbsp;

You might be asking yourself, "why wouldn't I always use `st.write()`?" There are a few reasons:

* `Magic` and `st.write()` inspect the type of data that you've passed in, and then decide how to best render it in the app. Sometimes you want to draw it another way. For example, instead of drawing a dataframe as an interactive table, you may want to draw it as a static table by using `st.table(df)`.

* The second reason is that other methods return an object that can be used and modified, either by adding data to it or replacing it.

* Finally, if you use a more specific Streamlit method you can pass additional arguments to customize its behavior.

&nbsp;
