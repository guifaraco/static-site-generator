import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Maybe this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node.url, "https://www.google.com")

    def test_is_none_url(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertIsNone(node.url)

    def test_is_not_none_text(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertIsNotNone(node.url)

    def test_instance(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsInstance(node, TextNode)
if __name__ == "__main__":
    unittest.main()
