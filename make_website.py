from tqdm import tqdm
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
    
def parse_filename(orig_path, has_path=False):
    path_part = r'.+\/' if has_path else ''
    m = re.search(fr'{path_part}(.*)_[0-9]+\.yml', orig_path)
    if m:
        return m.group(1)
    raise ValueError(f"{orig_path} couldn't be parsed!")

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
has_toc: true
parent: {published.capitalize()}
---
This is level {level[-1]} of the RAs.
"""
        md.write(level_md)
        # return level_md





def website(f):
    with open(f) as handle:
        md_content = handle.read()
        
    md_name, (published, level, lang, name) = get_export_path(f)

    english_version = ""
    if lang.lower() == "Dutch":
        english_version = f"{MD_DIR}/{published}/{level}/English/{name}"
        if os.path.exists(english_version):
            english_version = f"see also [the English version]({WEBSITE_BASE_URL}/{published}/{level}/English/{name})"
            english_version += "\n\n"
    
    
    pdf_path = f"EXPORTS/PDF/{published}/{level}/{lang}/{name}"
    docx_path = f"EXPORTS/DOCX/{published}/{level}/{lang}/{name}"
    
    pdf_button = f"[Download PDF]({GITHUB_RAW_BASE_URL + pdf_path}){{: .btn .btn-blue }}"
    docx_button = f"[Download DOCX]({GITHUB_RAW_BASE_URL + docx_path}){{: .btn .btn-blue }}"
    
    website_content = front_matter(published, name, level, lang) + "\n\n" +\
                                english_version +\
                                pdf_button + "\t\t\t" + docx_button +\
                                "\n\n" + md_content

    with open(md_name, "w") as web_handle:
        web_handle.write(website_content)
    # return website_content


if __name__ == "__main__":
    for cur_dir in ("published", "review"):
        eng = glob(f"{cur_dir}/*/English/*.yml")
        dutch = glob(f"{cur_dir}/*/Dutch/*.yml")
        # top = glob(f"{BASE_DIR}/TopLevel/*.yml")
    
        yaml_files = sorted(dutch + eng)
        for f in tqdm(yaml_files):
            level_base(f)
            website(f)

    
