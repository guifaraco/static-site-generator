class HTMLNode():
    def __init__(self, tag, attrs=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        stringified_props = ""
        for key, value in self.props.items():
            stringified_props += f" {key}='{value}'"
        return stringified_props

    def __repr__(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError

        stringified_children = ""
        for child in self.children:
            stringified_children += child.to_html()

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{stringified_children}</{self.tag}>"

        return f"<{self.tag}>{stringified_children}</{self.tag}>"
