from textnode import *
from htmlnode import *
from funcs import *
from blocks import *

def main():
#    node = TextNode("This is text with a `code block` word", TextType.TEXT)
#    node1 = TextNode("This is text with a **bold block** word", TextType.TEXT)
#    new_nodes = split_nodes_delimiter([node, node1], "`", TextType.CODE)
#    print(new_nodes)
#    for item in new_nodes:
#        print(item)
#    other_nodes = split_nodes_delimiter([node, node1], "**", TextType.BOLD)
#    print(other_nodes)
#    for item in other_nodes:
#        print(item)
#    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    
#    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
#    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

#    node = TextNode(
#        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#        TextType.TEXT,
#    )
#    new_nodes = split_nodes_link([node])
#    print(new_nodes)
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

#    node = TextNode(
#        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#        TextType.TEXT,
#    )
#    new_nodes = split_nodes_image([node])
    #print(new_nodes)

#    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#    nodes = text_to_textnodes(text)
#    print(nodes)
#    for node in nodes:
#        print(node)
#
    md = """
This is a paragraph

# just a h1 heading

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
    blocks = markdown_to_blocks(md)
    for block in blocks:
        print(block)
        print(block_to_block_type(block))
        print("")


main()