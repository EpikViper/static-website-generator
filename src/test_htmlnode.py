import unittest
from htmlnode import HTMLNode, LeafNode
from parentnode import ParentNode


class TestHMTLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        text_1 = HTMLNode().props_to_html()
        text_2 = ''
        self.assertEqual(text_1, text_2)


    def test_props_to_html_2(self):
        text_1 = HTMLNode(props={"href":"abgdevzt"}).props_to_html()
        text_2 = ' href="abgdevzt"'
        self.assertEqual(text_1, text_2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


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


if __name__ == "__main__":
    unittest.main()