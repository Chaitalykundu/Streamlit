import streamlit as st
import pandas as pd

# String
st.write('Hello World! :heart:')


# O.P.: Hello World! ❤️



# Multiple arguments
st.write("1+1=",1+1)

# Markdown
st.write('''
This is markdown
''')

# DataFrame
df = pd.DataFrame({"First column":[1,2,3],"Second Column":[4,5,6]})
st.write(df)
