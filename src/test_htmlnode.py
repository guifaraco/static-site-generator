import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello World")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = HTMLNode(tag="div", value="Hello World")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"id": "123", "class": "abc"})
        self.assertEqual(node.props_to_html(), " id='123' class='abc'")

if __name__ == '__main__':
    unittest.main()
