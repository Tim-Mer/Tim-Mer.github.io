from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            if text_node.text == None:
                raise ValueError('TextNode value cannot be None')
            return HTMLNode(None, text_node.text)
        case TextType.BOLD:
            return HTMLNode('b', text_node.text)
        case TextType.ITALIC:
            return HTMLNode('i', text_node.text)
        case TextType.CODE:
            return HTMLNode('code', text_node.text)
        case TextType.LINK:
            if text_node.url == None:
                raise ValueError('LINK nodes must have a valid href property')
            return HTMLNode('a', text_node.text, None, {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url == None:
                raise ValueError('IMAGE nodes must have a valid src property')
            return HTMLNode('img', "", None, {"src": text_node.url, "alt": text_node.text})
    raise ValueError('Unsupported TextType: INVALID_TYPE')