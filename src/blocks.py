from enum import Enum

class BlockType(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote = 4
    unordered_list = 5
    ordered_list = 6

def markdown_to_blocks(md: str):
    blocks = [x.strip() for x in md.split("\n\n") if x]
    return blocks

def block_to_block_type(md):
    return BlockType