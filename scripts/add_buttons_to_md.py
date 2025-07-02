from tqdm import tqdm
import os
from glob import glob
import yaml
import json
import re
import argparse
from io import StringIO
import os

MD_DIR = "./EXPORTS/MD"

mds = glob(MD_DIR + "/*/*.md")

def add_front_matter(md_str):
    default_front_matter = """---
layout: default
title: Home
nav_enabled: true
---

"""
    return default_front_matter + md_str

def add_button(md_str, link, link_text):
    button_md = f"[{link_text}]({link}){{: .btn .btn-green }}"
    return to_add + "\n\n" + md_str


# def download_link_from_path(path):    

BASE_URL = "https://research-aids.github.io/"
BASE_URL = "https://raw.githubusercontent.com/research-aids/research-aids.github.io/refs/heads/main/"

for f in mds:
    with open(f) as handle:
        md_content = handle.read()
        pdf_path = f.replace("MD", "PDF")
        
        if os.path.isfile(pdf_path):
            md_content = add_button(md_content, link, "Download PDF")

        docx_path = f.replace("MD", "DOCX")
        if os.path.isfile(docx_path):
            md_content = add_button(md_content, link, "Download DOCX")

