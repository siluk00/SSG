import re
from textnode import TextNode
from htmlnode import HTMLNode
from parentnode import ParentNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_split = []
    for node in old_nodes:
        if node.text_type == "text":
            if delimiter in node.text:         
                new_list = node.text.split(delimiter)
                new_list2 = []
                for text in new_list:
                    if not text:
                        pass
                    elif (delimiter + text) in node.text and (text + delimiter)in node.text:
                        new_list2.append(TextNode(text, text_type))
                    else:
                        new_list2.append(TextNode(text, "text"))
                if new_list2:
                    list_of_split += new_list2                      
            else:
                if node.text:
                    list_of_split.append(TextNode(node.text, "text"))
        else:
            list_of_split.append(node)
    
    return list_of_split

def extract_markdown_images(text):
    list_of_images = re.findall(r"!\[.+?\]\(.+?\)", text)
    list_return = []
    for img in list_of_images:
        str1 = img[2:img.find(']')]
        str2 = img[img.find('(')+1:-1]
        list_return.append((str1,str2))
    return list_return

def extract_markdown_links(text):
    list_of_links = re.findall(r"\[.+?\]\(.+?\)", text)
    list_return = []
    for link in list_of_links:
        str1 = link[1:link.find(']')]
        str2 = link[link.find('(')+1:-1]
        list_return.append((str1,str2))
    return list_return

def split_nodes_link(old_nodes):
    list_of_return = []
    for node in old_nodes:
        if node.text_type == "text":
            
            extracted_list = extract_markdown_links(node.text)
            if extracted_list:
                

                list_of_links = re.findall(r"\[.+?\]\(.+?\)", node.text)  
                
                str_text = [node.text]
            
                for j in range(len(list_of_links)):
                    str_list = str_text[j].split(list_of_links[j], 1)
                    n = str_text[j].find(list_of_links[j])
                
                    if j != len(list_of_links)-1:
                        if str_list[0]:
                            list_of_return.append(TextNode(str_list[0], "text"))    
                        list_of_return.append(TextNode(extracted_list[j][0], "link", extracted_list[j][1]))
                        str_text.append(str_list[1])  
                    else:
                        
                        if str_list[0]:
                            list_of_return.append(TextNode(str_list[0], "text"))
                        list_of_return.append(TextNode(extracted_list[j][0], "link", extracted_list[j][1]))                            
                        if str_list[1]:
                            list_of_return.append(TextNode(str_list[1], "text"))                             
            else:
                if node.text:
                    list_of_return.append(node)
        else:
            list_of_return.append(node)
    return list_of_return

def extract_markdown_images(text):
    list_of_images = re.findall(r"!\[.+?\]\(.+?\)", text)
    list_return = []
    for img in list_of_images:
        str1 = img[2:img.find(']')]
        str2 = img[img.find('(')+1:-1]
        list_return.append((str1,str2))
    return list_return

def split_nodes_image(old_nodes):
    list_of_return = []

    for node in old_nodes:
        if node.text_type == "text":
           
            extracted_list = extract_markdown_images(node.text)
            if extracted_list:

                list_of_links = re.findall(r"!\[.+?\]\(.+?\)", node.text)  
                
                str_text = [node.text]
            
                for j in range(len(list_of_links)):
                    str_list = str_text[j].split(list_of_links[j], 1)
                    n = str_text[j].find(list_of_links[j])
                
                    if j != len(list_of_links)-1:
                        if str_list[0]:
                            list_of_return.append(TextNode(str_list[0], "text"))    
                        list_of_return.append(TextNode(extracted_list[j][0], "image", extracted_list[j][1]))
                        str_text.append(str_list[1])  
                    else:
                        
                        if str_list[0]:
                            list_of_return.append(TextNode(str_list[0], "text"))
                        list_of_return.append(TextNode(extracted_list[j][0], "image", extracted_list[j][1]))                            
                        if str_list[1]:
                            list_of_return.append(TextNode(str_list[1], "text"))                             
            else:
                if node.text:
                    list_of_return.append(node)
        else:
            list_of_return.append(node)
    return list_of_return
         
def text_to_textnodes(text):
    list_bold = split_nodes_delimiter([TextNode(text, "text")], "**", "bold")
    list_italic = split_nodes_delimiter(list_bold, "*", "italic")
    list_code = split_nodes_delimiter(list_italic, "`", "code")
    list_image = split_nodes_image(list_code)
    list_link = split_nodes_link(list_image)
    return list_link

def markdown_to_blocks(markdown):
    markdown = __remove_lines(markdown)
    list_of_markdown = markdown.split("\n\n")
    list_of_markdown = list(filter(lambda x: not x.isspace() and x, list_of_markdown))

   
    for i in range(len(list_of_markdown)):
        count = 0
        md = list_of_markdown[i]
        s = md[0]
        if i == 0:
            while s=='\n':
                count += 1
                s = md[count]
            md = md[count:]
            count = 0
            s = md[0]

        while s == " ":
            count+=1
            s = md[count]
        md = md[count:]
        count = 0
        s = md[-1]
        while s == " ":
            count-=1
            s = md[count-1]
        if count != 0:
            md = md[:count]
        list_of_markdown[i] = md

    return list_of_markdown
        
def __remove_lines(str):
    if str.find("\n\n\n") == -1:
        return str
    str = str.replace("\n\n\n", "\n\n")
    return __remove_lines(str)

def block_to_blocktype(markdown):
    markdown_list = markdown.split('\n')
    n = 0

    if markdown[0] == '#':
        count = 0
        s = markdown[0]
        while count <= 6 and s == '#':
            count+=1
            s = markdown[count]
        return f"h{count}"
    elif markdown[0:3]=="```" and markdown[-3:]=='```':
        return "code"
    elif len(list(filter(lambda x: x[0]=='>', markdown_list))) == len(markdown_list):
        return "blockquote"
    elif len(list(filter(lambda x: x[0]=='*' or x[0]=='-', markdown_list))) == len(markdown_list):
        return "unordered_list"
    elif len(list(filter(lambda x: x[0] == str(markdown_list.index(x)+ 1) and x[1:3] =='. ', markdown_list))) == len(markdown_list):
        return "ordered_list"
    else:
        return "text"

def markdown_to_html_node(markdown):
    list_of_markdown = markdown_to_blocks(markdown)
    html_list = []
    for block in list_of_markdown:
        blocktype = block_to_blocktype(block)
        if blocktype[0] == 'h':
            htmlnode = ParentNode(blocktype, list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(block[2:]))),)
        elif blocktype == "code":
            auxnode = ParentNode(blocktype, list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(block[3:-3]))))
            htmlnode = ParentNode("pre", [auxnode])
        elif blocktype == "blockquote":
            block_list = block.split("\n")
            block_list = list(map(lambda x: x[1:]), block_list)
            block = "\n".join(block_list)
            htmlnode = ParentNode(blocktype, list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(block))), None)
        elif blocktype == "unordered_list":
            block_list = block.split("\n")
            li_list=[]
            for li in block_list:
                li_list.append(ParentNode("li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(li[2:])))))
            htmlnode = ParentNode("ul", li_list)
        elif blocktype == "ordered_list":
            block_list = block.split("\n")
            li_list=[]
            for li in block_list:
                li_list.append(ParentNode("li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(li[2:])))))
            htmlnode = ParentNode("ol", li_list)
        else:
            htmlnode = ParentNode("p", list(map(lambda x: x.text_node_to_html_node() ,text_to_textnodes(block))))
        html_list.append(htmlnode)        
    return html_list


        

