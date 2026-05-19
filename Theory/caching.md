# Caching

The Streamlit cache allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

The basic idea behind caching is to store the results of expensive function calls and return the cached result when the same inputs occur again rather than calling the function on subsequent runs.

To cache a function in Streamlit, you need to decorate it with one of two decorators (st.cache_data and st.cache_resource):

```py
@st.cache_data
def long_running_function(param1, param2):
    return …
```