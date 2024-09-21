import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('hello world', 'text')
        node1 = TextNode('hello world', 'bold')
        node2 = TextNode('hello world', 'italic')
        node3 = TextNode('hello world', 'code')
        node4 = TextNode('hello world', 'link', 'www.ufsm.br')
        node5 = TextNode('hello world', 'image', 'www.ufsm.br')
        #node6 = TextNode('hello world','josepeh', 'www.ufsm.br')
        #node7 = TextNode('hello world', None)
        #node8 = TextNode('hello world', '')
        node9= TextNode('hello world', 'image')
        #node10 = TextNode( None, 'link')

        node = node.text_node_to_html_node()
        node1 = node1.text_node_to_html_node()
        node2 = node2.text_node_to_html_node()
        node3 = node3.text_node_to_html_node()
        node4 = node4.text_node_to_html_node()
        node5 = node5.text_node_to_html_node()
        #node6 = node6.text_node_to_html_node()
        #node7 = node7.text_node_to_html_node()
        #node8 = node8.text_node_to_html_node()
        node9 = node9.text_node_to_html_node()
        #node10 = node10.text_node_to_html_node()

        print(node.to_html())
        print(node1.to_html())
        print(node2.to_html())
        print(node3.to_html())
        print(node4.to_html())
        print(node5.to_html())
        #print(node6.to_html())
        #print(node7.to_html())
        #print(node8.to_html())
        print(node9.to_html())
        #print(node10.to_html())
        print(node.to_html())
        print(node.to_html())



if __name__ == "__main__":
    unittest.main()