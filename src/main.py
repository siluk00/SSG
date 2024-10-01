from textnode import *
from codefile import *
from parentnode import *
import os
import shutil
import os.path


def main(): 
    cwd = os.getcwd()
    static_folder = os.path.join(cwd, "static")
    public_folder = os.path.join(cwd, "public")
    from_path_file = os.path.join(cwd, "content")
    template_file = os.path.join(cwd, "template.html")
    
    delete_public(public_folder)
    copy_static_to_public(static_folder, public_folder)
    generate_pages_recursive(from_path_file, template_file, public_folder)

def copy_static_to_public(static_folder, public_folder):
    static_dir = os.listdir(static_folder) 
    static_paths = [] #everything that there is in static folder

    for file in static_dir:
        static_paths.append(os.path.join(static_folder, file))

    file_paths = list(filter(os.path.isfile, static_paths))
    
    for file in file_paths:
        shutil.copy(file, public_folder)
    
    dir_paths = list(filter(os.path.isdir ,static_paths))
    
    for dir in dir_paths:
        bs = os.path.basename(dir)
        new_dir = os.path.join(public_folder, bs)
        os.mkdir(new_dir)
        copy_static_to_public(dir, new_dir)

def delete_public(public_folder):
    shutil.rmtree(public_folder)
    os.mkdir(public_folder)

def generate_file(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, 'r')
    f = f.read()
    t = open(template_path)
    t = t.read()
    html_list = markdown_to_html_node(f)
    html = ""
    for node in html_list:
        html += node.to_html()
    title = extract_title(f.split('\n')[0])
    t = t.replace("{{ Title }}", title)
    t = t.replace("{{ Content }}", html)
    d = open(dest_path, 'w')
    d.write(t)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_dir = os.listdir(dir_path_content) 
    paths = [] #everything that there is in static folder

    for file in list_dir:
        paths.append(os.path.join(dir_path_content, file))

    file_paths = list(filter(os.path.isfile, paths))
    
    for file in file_paths:
        file_base , ext = os.path.splitext(file)
        base = os.path.basename(file_base)
        if ext == '.md':
            dest = os.path.join(dest_dir_path, base + ".html")
        
            generate_file(file, template_path, dest) 
        else:
            shutil.copy(file, dest_dir_path)
    
    dir_paths = list(filter(os.path.isdir , paths))
    
    for dir in dir_paths:
        bs = os.path.basename(dir)
        new_dir = os.path.join(dest_dir_path, bs)
        os.mkdir(new_dir)
        generate_pages_recursive(dir, template_path, new_dir)




main()