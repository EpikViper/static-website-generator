from textnode import TextNode, TextType
from static_to_public import static_to_public
from structure_page import generate_page, generate_page_recursive
import sys

def main():
    base_path = sys.argv[0]
    static_to_public("/home/turmana/static-website-generator/static", "/home/turmana/static-website-generator/docs")
    generate_page_recursive("/home/turmana/static-website-generator/content", "/home/turmana/static-website-generator/template.html",
    "/home/turmana/static-website-generator/docs", base_path)
    

main()