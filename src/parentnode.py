from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing")
        
        if self.children is None:
            raise ValueError("Children are required")

        html_text = f"<{self.tag}>"

        for child in self.children:
            child_html = child.to_html()
            html_text += child_html

        return html_text + f"</{self.tag}>"
