import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode(tag="div", value="Hello World")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = LeafNode(tag="div", value="Hello World")
        self.assertEqual(node.to_html(), "<div>Hello World</div>")
        node = LeafNode(tag="div", value=None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == '__main__':
    unittest.main()
