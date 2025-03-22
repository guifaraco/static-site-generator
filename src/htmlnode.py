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
