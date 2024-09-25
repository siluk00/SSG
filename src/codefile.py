import re
from textnode import TextNode

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
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(list_of_links)
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
            print("*****")
            print(node.text)
            extracted_list = extract_markdown_links(node.text)
            if extracted_list:
                print("@@@@@@@@@")
                print(node.text)

                list_of_links = re.findall(r"\[.+?\]\(.+?\)", node.text)  
                
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

        

