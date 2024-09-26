import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from codefile import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        st = """          # This is a heading            

        




         This is a paragraph of text. It has some **bold** and *italic* words inside of it.  




  * This is the first list item in a list block
* This is a list item
* This is another list item   



1. uehfuihuiwfhuihwesf
2. siudhfiuhsduihfuishdf
3. asoifjiosiodjfiojsdiofjsae
4. osdauifoiiosjgiojijiorjew
5. soduioijfioajoiwejijijf

```kuashduhiaushiudh
wduihawuihdiuahuidhuihaiuwhiudh
awiuhduihquihiuehu iuqhw iuehiuqwhieu iuqwh eiuqhwiuehqiuweh```


###### uasygduygauygwyudg

"""
        listt = markdown_to_blocks(st)
        print(list(map(lambda x: block_to_blocktype(x), listt)))
        print(markdown_to_html_node(st))
        



        node = TextNode('hello world **what are** hjhh', 'text')
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

        print("*********** TEXTNODE ***********************")
        print(split_nodes_image([TextNode("![asd](asd.dd)![sdfsdfsdf](asd.dasd)ashjhfjijhsdfkjhuwehiuhfsd![asjihdjkl](joasdashudh.ai)oasoijdij aosijdiojw aosijdioasjdoijas ![kasjhdjnjkasnd](aksjhd.jj) sdufhuih\n iuasHUHAUISH![asjihdjkl](joasdashudh.ai)IUAHSUHDUIHASUIDHIUH![asjihdjkl](joasdashudh.ai)", "text")]))
        print("****")
        print(split_nodes_delimiter([node, node2], '**', "bold"))
        print("******")
        print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))

        print("*********************LEAFNODES*****************")

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

        print(extract_markdown_images("aisuh iauhsuih. dhaiushd\n aiusduh ooo ![sujhjhd](udhuhd.uhf) saioudhhasd ![akjhsdjh](fduihsdfuh.jfjd)oisa \n ouiasdhfiuh"))
        print(extract_markdown_links("aojshdusajh\nd jfjsdnf [asoijiifisdifj](http:\\www.aisuehuas.fjidjf)oasidoiidpoiawdi [oaisjdij](www.idjaijsd.aiosjdijiasjd)asudjaisojidjiajsd[has](https://www.dusaujduasu.aisujdujas.jij)"))
        print(extract_markdown_images("uszhruihasuiheuihasuihease"))
        


if __name__ == "__main__":
    unittest.main()