import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_init(self):
        node = LeafNode(tag="div", value="Hello World")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_leaf_to_html(self):
        node = LeafNode(tag="div", value="Hello World")
        self.assertEqual(node.to_html(), "<div>Hello World</div>")
        node = LeafNode(tag="div", value=None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("span", "child")], props={"id": "123"})
        self.assertEqual(node.to_html(), "<div id='123'><span>child</span></div>")

if __name__ == '__main__':
    unittest.main()
