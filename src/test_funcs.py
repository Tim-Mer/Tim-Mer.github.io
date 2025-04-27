import unittest

from funcs import *

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an italic node")
        
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")
        
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.link.node")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "www.link.node"})
        
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "This is an image node"})

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError) as cm:
            node = TextNode("Invalid node", "INVALID_TYPE")
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Unsupported TextType: INVALID_TYPE")

    def test_link_missing_props(self):
        with self.assertRaises(ValueError) as cm:
            node = TextNode("This is a link node", TextType.LINK)
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "LINK nodes must have a valid href property")

    def test_image_missing_props(self):
        with self.assertRaises(ValueError) as cm:
            node = TextNode("This is an image node", TextType.IMAGE)
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "IMAGE nodes must have a valid src property")

    def test_empty_value(self):
        node = TextNode("", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_props_in_non_link_or_image(self):
        node = TextNode("This is a bold node", TextType.BOLD, "extra_props")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertIsNone(html_node.props)

    def test_none_value(self):
        with self.assertRaises(ValueError) as cm:
            node = TextNode(None, TextType.TEXT)
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "TextNode value cannot be None")

    def test_image_with_alt_text(self):
        node = TextNode("Custom alt text", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "Custom alt text"})

    def test_link_with_additional_props(self):
        node = TextNode("This is a link node", TextType.LINK, "www.link.node")
        html_node = text_node_to_html_node(node)
        html_node.props["target"] = "_blank"
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "www.link.node", "target": "_blank"})

    def test_unsupported_props(self):
        node = TextNode("This is a text node", TextType.TEXT, "unsupported_props")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertIsNone(html_node.props)
    
    def test_split_nodes_delimiter_basic(self):
        nodes = [TextNode("Hello **World** Again", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "World")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " Again")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        
    def test_split_nodes_delimiter_multiple(self):
        nodes = [TextNode("Hello **World** Again and Hello **World** Again", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "World")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " Again and Hello ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "World")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " Again")
        self.assertEqual(result[4].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_multiple_nodes(self):
        nodes = [
            TextNode("First`Node`Test", TextType.TEXT),
            TextNode("Second_Node_Test", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].text, "First")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "Node")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, "Test")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "Second")
        self.assertEqual(result[3].text_type, TextType.TEXT)
        self.assertEqual(result[4].text, "Node")
        self.assertEqual(result[4].text_type, TextType.ITALIC)
        self.assertEqual(result[5].text, "Test")
        self.assertEqual(result[5].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_missing_second_delimiter(self):
        nodes = [TextNode("Hello**World", TextType.TEXT)]
        with self.assertRaises(ValueError) as cm:
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(str(cm.exception), "Second delimeter not found (Invalid Markdown syntax)")

    def test_split_nodes_delimiter_no_delimiters(self):
        nodes = [TextNode("NoDelimitersHere", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "NoDelimitersHere")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_empty_text(self):
        nodes = [TextNode("", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_empty_nodes_list(self):
        nodes = []
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 0)

    def test_split_nodes_delimiter_nested_delimiters(self):
        nodes = [TextNode("Nested **bold **inside** text** example", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "Nested ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold ")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, "inside")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, " text")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " example")
        self.assertEqual(result[4].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_multiple_delimiters_in_single_node(self):
        nodes = [TextNode("Multiple **bold** and **italic** delimiters", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "Multiple ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "italic")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " delimiters")
        self.assertEqual(result[4].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_single_character_delimiter(self):
        nodes = [TextNode("Single_Character_Delimiter", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Single")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "Character")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, "Delimiter")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        
    
if __name__ == "__main__":
    unittest.main()