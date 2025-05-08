from textnode import *
from htmlnode import *
from funcs import *
from blocks import *
from md_to_html import *#
from generate import *

def main():
    clean_public()
    copy_static()
    
    generate_page("./content/index.md", "template.html", "./public/index.html")
    
main()