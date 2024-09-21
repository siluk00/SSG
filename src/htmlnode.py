class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception("Not Implemented")
    

    #implement Error if called None
    def props_to_html(self):
        if not self.props:
            return ""

        attribute_list = []
        
        for key, value in self.props.items():
            attribute_list.append(f'{key}="{value}"')

        return " " + " ".join(attribute_list)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

        