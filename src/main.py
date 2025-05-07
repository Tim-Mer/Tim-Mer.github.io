from textnode import *
from htmlnode import *
from funcs import *
from blocks import *
from md_to_html import *#
from generate import *

def main():
    clean_public()
    copy_static()
    md = """
This is a paragraph

# just a h1 heading

## h2 heading

```
code block
```

> this is a quote

- unordered
- list
- blah blah blah

1. ordered
2. list

end
"""
    #tmp = markdown_to_html_node(md)
    #print(tmp.to_html())
    
main()