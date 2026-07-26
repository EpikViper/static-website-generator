
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None: return ""

        full_text = " "

        for key,val in self.props.items():
            full_text += f'{key}="{val}" '

        return full_text[:-1]

    def __repr__(self):

        return f"HTMLNode({self.tag}, {self.val}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        
        if self.tag is None:
            return self.value

        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):

        return f"HTMLNode({self.tag}, {self.val}, {self.props})"
