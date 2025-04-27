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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    len_delimiter = len(delimiter)
    pos1 = 0
    pos2 = 0
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            pos1 = node.text.find(delimiter)
            if not pos1 == -1:
                pos2 = node.text[pos1+len(delimiter):].find(delimiter)
                if pos2 == -1:
                    raise ValueError('Second delimeter not found (Invalid Markdown syntax)')
                pos2 = pos1 + node.text[pos1+len(delimiter):].find(delimiter) + len_delimiter
                new_nodes.append(TextNode(node.text[:pos1],node.text_type))
                new_nodes.append(TextNode(node.text[pos1+len_delimiter:pos2], text_type))
                new_nodes.extend(split_nodes_delimiter([TextNode(node.text[pos2+len_delimiter:], node.text_type)], delimiter, text_type))
            else:
                new_nodes.append(node)      
    return new_nodes