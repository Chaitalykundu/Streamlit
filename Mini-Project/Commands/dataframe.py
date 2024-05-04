import streamlit as st
import pandas as pd
import numpy as np

df = {"first column":[1,2,3,4,5], "second column":[9,8,7,6,5]}

df = pd.DataFrame(df)
df 

# Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write()

# or
st.write(df)
