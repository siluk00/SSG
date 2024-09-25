from textnode import *
import os
import shutil


def main():
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode)
    copy_static_to_public()
    shutil.rmtree("public/")

def copy_static_to_public():
    print(os.getcwd())

main()