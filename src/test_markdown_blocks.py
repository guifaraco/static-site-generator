import unittest

from markdown_blocks import block_to_block_type, markdown_to_blocks, BlockType, markdown_to_html_node

class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
           blocks,
           [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
           ],
       )

    def test_block_to_block_type(self):
        block = "This is **bolded** paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        block = "## This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

        block = "```\nx = 2\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

        block = ">hi\n>this\n>is\n>a\n>quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

        block = "- line1\n- line2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

        block = "1. line1\n2. line2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
if __name__ == "__main__":
    unittest.main()
