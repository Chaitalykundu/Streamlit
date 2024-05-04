# magic

Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all.

Just put the thing you want to show on its own line of code, and it will appear in your app.

&nbsp;

&nbsp;

## Example

### String

```py
"Hello World"
```

&nbsp;

### Multiple arguments

```py
"1+1=",1+1
```

&nbsp;

### Markdown

```py
'''
This is markdown
'''
```

&nbsp;

### DataFrame

```py
df = pd.DataFrame({"First column":[1,2,3],"Second Column":[4,5,6]})
df
```
