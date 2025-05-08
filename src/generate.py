import os
import shutil
from textnode import *
from htmlnode import *
from funcs import *
from blocks import *
from md_to_html import *#
from generate import *

def clean_public(dir="./public"):
    logging(f"Removing {dir}")
    shutil.rmtree(dir)
    os.mkdir(dir)

def copy_static(input_dir="./static/", output_dir="./public/"):
    for item in os.listdir(input_dir):
        in_file = os.path.join(input_dir, item)
        out_file = os.path.join(output_dir, item)
        if os.path.isfile(in_file):
            logging(f"Copying {in_file} to {output_dir}")
            shutil.copy(in_file, output_dir)
        else:
            if not os.path.isdir(out_file):
                logging(f"Making directory {out_file}")
                os.mkdir(out_file)
            copy_static(in_file, out_file)

def logging(msg):
    print(f"LOG: {msg}")
    pass

def extract_title(md):
    if md == "":
        raise Exception("Empty .md file")
    title = ""
    for line in md.split("\n"):
        if line.strip().startswith('# '):
            title = line.replace("# ", "")
            break
    if title == "":
        raise Exception("No title found")
    return title

def generate_page(from_path, template_path, dest_path):
    logging(f"Generating page from {from_path} to {dest_path}, using template {template_path}")
    input_md = ""
    with open(from_path, "r") as file:
        input_md = file.read()
    
    template = ""
    with open(template_path, "r") as file:
        template = file.read()

    input_html = markdown_to_html_node(input_md).to_html()
    title = extract_title(input_md)
    
    output_html = template.replace("{{ Title }}", title).replace("{{ Content }}", input_html)
    
    with open(dest_path, "w") as file:
        file.write(output_html)
    
    
    
    
    