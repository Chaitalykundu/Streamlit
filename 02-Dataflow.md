# Data flow

Streamlit's architecture allows you to write apps the same way you write plain Python scripts. To unlock this, Streamlit apps have a unique data flow: any time something must be updated on the screen, Streamlit reruns your entire Python script from top to bottom.

This can happen in two situations:

- Whenever you modify your app's source code.

- Whenever a user interacts with widgets in the app. For example, when dragging a slider, entering text in an input box, or clicking a button.

&nbsp;

&nbsp;

Whenever a `callback` is passed to a widget via the `on_change` (or `on_click`) parameter, the `callback` will always run before the rest of your script.

And to make all of this fast and seamless, Streamlit does some heavy lifting for you behind the scenes. A big player in this story is the `@st.cache_data` decorator, which allows developers to skip certain costly computations when their apps rerun. We'll cover caching later in this page.
