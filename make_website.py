# from tqdm import tqdm
import os
from glob import glob
import yaml
import json
import re
import argparse
from io import StringIO
import os
from datetime import datetime

MD_DIR = "./EXPORTS/MD"
WEBSITE_DIR = "./docs"

GITHUB_RAW_BASE_URL = "https://raw.githubusercontent.com/colonial-heritage/research-aids/refs/heads/main/"
WEBSITE_BASE_URL = "https://research-aids.github.io/"

# def download_button(published, level, language, name, extension):
    # link_text = dict(pdf="Download PDF", docx="Download DOCX")
    # link_text = link_text[extension.lower()]

    # # language = "English" if language.lower().startswith("en") else "Dutch"
    # link_path = f"EXPORTS/{published}/{extension.upper()}/{level}/{language}/{name}.{extension.lower()}"
    # link = GITHUB_RAW_BASE_URL + link_path

    # return f"[{link_text}]({link}){{: .btn .btn-blue }}"
  

def front_matter(published, ra_name, level, lang):
    exclude_from_navbar = (lang == "English")
    return f"""---
layout: default
title: {ra_name}
parent: {level}
ancestor: {published.capitalize()}
nav_enabled: true
has_toc: true
date: {datetime.today().strftime("%Y-%m-%d")}
nav_exclude: {exclude_from_navbar}
--- 
"""


def related_aids_table(own_level, related_aids_dict):
    pass
    
# def parse_filename(orig_path, extension, has_path=False):
#     path_part = r'.+\/' if has_path else ''
#     m = re.search(fr'{path_part}(.*)_[0-9]+\.{extension}', orig_path)
#     if m:
#         return m.group(1)
#     else:
#         return 
#     raise ValueError(f"{orig_path} couldn't be parsed!")

def parse_filename(fname):
    return fname.replace(".md", "")

def parse_filepath(fp):
    *pref, published, level, lang, fname = fp.split(os.path.sep)
    return published, level, lang, parse_filename(fname)

def get_export_path(orig_path, make_dirs=True):
    published, level, lang, name = parse_filepath(orig_path)
    extension = ".md"
    export_path =  os.path.join(WEBSITE_DIR, published, level, lang, name) + extension
    os.makedirs(os.path.dirname(export_path), exist_ok=True)
    return export_path, (published, level, lang, name)



def level_base(f):
    _, (published, level, lang, name) = get_export_path(f)
    folder_name = f"{WEBSITE_DIR}/{published}/{level}"
    # os.makedirs(folder_name, exist_ok=True)
    

    # published = os.path.split(out_dir)[-1].capitalize()
    with open(f"{folder_name}/{level}.md", "w") as md:
        level_md = f"""---
layout: default
title: {level}
nav_enabled: true
has_toc: false
parent: {published.capitalize()}
---
This is level {level[-1]} of the RAs.
{{: .no_toc }}
"""
        md.write(level_md)
        # return level_md



def get_title(md_content):
    title_lines = [(l.replace("# ", ""), i) for i, l in enumerate(md_content.splitlines()) if l.strip().startswith("# ")]
    return title_lines[0]



def website(f):
    with open(f) as handle:
        md_content = handle.read()

    title, title_ind = get_title(md_content)
        
    md_name, (published, level, lang, name) = get_export_path(f)

    lang_link = ""
    if lang == "Dutch":
        english_version = f"{MD_DIR}/{published}/{level}/English/{name}.md"
        if os.path.exists(english_version):
            lang_link = f"[English version]({WEBSITE_BASE_URL}/{published}/{level}/English/{name}.html){{: .btn .btn-blue }}"
            lang_link += "\n\n"
    elif lang == "English":
        dutch_version = f"{MD_DIR}/{published}/{level}/Dutch/{name}.md"
        if os.path.exists(dutch_version):
            lang_link = f"[Nederlandse versie]({WEBSITE_BASE_URL}/{published}/{level}/Dutch/{name}.html){{: .btn .btn-blue }}"
            lang_link += "\n\n"

    
    
    pdf_path = f"EXPORTS/PDF/{published}/{level}/{lang}/{name}.pdf"
    docx_path = f"EXPORTS/DOCX/{published}/{level}/{lang}/{name}.docx"
    
    pdf_button = f"[Download PDF]({GITHUB_RAW_BASE_URL + pdf_path}){{: .btn .btn-blue }}"
    docx_button = f"[Download DOCX]({GITHUB_RAW_BASE_URL + docx_path}){{: .btn .btn-blue }}"
    
    website_content = front_matter(published, title, level, lang) + "\n\n" +\
                                lang_link +\
                                pdf_button + "        " + docx_button +\
                                "\n\n" + md_content + "SOMETHING STUPID"

    with open(md_name, "w") as web_handle:
        print(f"writing website to file: {md_name}", flush=True)
        web_handle.write(website_content)
    # return website_content


if __name__ == "__main__":
    print("GLOB: ", glob("*"), flush=True)
    
    print(glob(f"{MD_DIR}/published/*/English/*.md"), flush=True)
    for cur_dir in ("published", "review"):
        eng = sorted(glob(f"{MD_DIR}/{cur_dir}/*/English/*.md"))
        dutch = sorted(glob(f"{MD_DIR}/{cur_dir}/*/Dutch/*.md"))
        # top = glob(f"{BASE_DIR}/TopLevel/*.yml")

        # ORDER IMPORTANT!!! (English first)
        yaml_files = eng + dutch
        for f in yaml_files:
            level_base(f)
            website(f)