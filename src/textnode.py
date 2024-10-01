from leafnode import *
from parentnode import *

class TextNode:
    

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    #there's a problem with image. Leafnodes should always have a value. but image should be an empty string as value
    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(None, self.text)
        elif self.text_type == "bold":
            return LeafNode('b', self.text)
        elif self.text_type == "italic":
            return LeafNode('i', self.text)
        elif self.text_type == "code":
            return LeafNode('code', self.text)
        elif self.text_type == "link":
            return LeafNode('a', self.text, {'href': self.url,})
        elif self.text_type == "image":
            return LeafNode('img', "img", {'src': self.url, 'alt': self.text})
        else:
            raise Exception("Text type is not on the list")
        

    
