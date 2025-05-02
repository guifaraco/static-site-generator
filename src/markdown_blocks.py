from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith("#"):
        is_heading = True
        for char in block[1:7]:
            if char == " ":
                break
            if char != "#":
                is_heading = False
                break
        if is_heading == True:
            return BlockType.HEADING

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    lines_type = []
    for i in range(len(lines)):
        if lines[i][0] == ">":
            lines_type.append("quote")
        if lines[i][:2] == "- ":
            lines_type.append("unordered_list")
        if lines[i][0] == (f"{i+1}") and lines[i][1:3] == ". ":
            lines_type.append("ordered_list")

    if len(lines) == len(lines_type):
        if lines_type.count("quote") == len(lines_type):
            return BlockType.QUOTE

        if lines_type.count("unordered_list") == len(lines_type):
            return BlockType.UNORDERED_LIST

        if lines_type.count("ordered_list") == len(lines_type):
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
