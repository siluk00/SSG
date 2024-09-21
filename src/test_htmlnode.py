import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node3 = LeafNode('a', "click me", {'href': "www.ufsm.br",})
        node = HTMLNode('p', "Hello WOrld", [node3])
        node2 = LeafNode('h1',"Sweet Home")
        node4 = ParentNode("p",[LeafNode("b", "Bold text"),                        
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),],)
        node5 = ParentNode("body", [node2, node3, node4], {'font-color':'ff66a4',})


        print(node3.props_to_html())
        print(node2.props_to_html())
        print(node.props_to_html())
        print(node4.props_to_html())
        print(node5.props_to_html())
        print(node3.to_html())
        print(node2.to_html())
        print(node4.to_html())
        print(node5.to_html())
        print(node)
        print(node2)
        print(node3)
        print(node5)
        



if __name__ == "__main__":
    unittest.main()