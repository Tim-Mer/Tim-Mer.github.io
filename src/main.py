from textnode import *
from htmlnode import *
from funcs import *

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node1 = TextNode("This is text with a **bold block** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node, node1], "`", TextType.CODE)
    print(new_nodes)
    for item in new_nodes:
        print(item)
    other_nodes = split_nodes_delimiter([node, node1], "**", TextType.BOLD)
    print(other_nodes)
    for item in other_nodes:
        print(item)


main()