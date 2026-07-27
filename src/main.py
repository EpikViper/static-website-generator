from textnode import TextNode, TextType
from static_to_public import static_to_public
from structure_page import generate_page, generate_page_recursive
import sys

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else '/'

    static_to_public("static", "docs")
    generate_page_recursive("content", "template.html", "docs", base_path)
    

main()