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


if __name__ == "__main__":
    unittest.main()