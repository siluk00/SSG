from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        
        value = ""

        for child in self.children:
            value += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{value}</{self.tag}>"