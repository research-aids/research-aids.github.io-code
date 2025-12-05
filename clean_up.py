from glob import glob
import yaml
import json
import re

import os
from pathlib import Path
import shutil


#############################################
### REMOVE UNCESSARY FILES FROM PARENT
### WARNING: REMOVES EVERTHING *EXCEPT* EXPLICITLY WANTED FOLDERS/FILES
#############################################


keep = ("published",
        "review",
        "handbook.md",
        "README.md",
        "LICENSE",
        "docs")


for f in glob("*"):
    if not f in keep:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            Path.unlink(f)
    else:
        print(f"keeping {f}")




# try:
#     Path.unlink("directory_tree.md")
#     Path.unlink("README.md")
#     Path.unlink("handbook.md")

#     shutil.rmtree("offline")
#     # shutil.rmtree("review")
#     shutil.rmtree("scripts")

# except FileNotFoundError:
#     print("seems like files were already gone...")


# try:
#     Path.unlink(".github/workflows/check_yaml.yml")
#     Path.unlink(".github/workflows/yaml2json.yml")
#     Path.unlink(".github/workflows/yaml_export.yaml")
# except FileNotFoundError:
#     print("phew, workflow files already gone")



#############################################
### ADD DATE TO INDEX.HTML
#############################################

# print(glob("*"))
# print(glob(DOCS_DIR+"/*"))

DOCS_DIR = "./docs"

from datetime import datetime
index = ""
with open(DOCS_DIR + "/index.md", "r") as handle:
    index += handle.read()

with open(DOCS_DIR + "/index.md", "w") as handle:
    index += "\n\n" + f"current version from {datetime.now()}"#.strftime("%Y-%m-%d")}"

    handle.write(index)