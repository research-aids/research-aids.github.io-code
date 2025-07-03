from glob import glob
import yaml
import json
import re

import os
from pathlib import Path
import shutil


#############################################
### REMOVE UNCESSARY FILES FROM PARENT
#############################################


Path.unlink("directory_tree.md")
Path.unlink("README.md")
Path.unlink("handbook.md")

shutil.rmtree("forKinsukAndSjors")
shutil.rmtree("offline")
# shutil.rmtree("review")



#############################################
### MOVE MARKDOWN FILES TO DOCS
#############################################

MD_DIR = "./EXPORTS/WEBSITE"
DOCS_DIR = "./docs"

# os.makedirs(DOCS_DIR)

md_files = glob(MD_DIR + "/*/Dutch/*.md") + glob(MD_DIR + "/*/English/*.md")

for f in md_files:
    # with open(f) as handle:
    print(f"copying {f} to {f.replace(MD_DIR, DOCS_DIR)}")
    shutil.copy2(f, f.replace(MD_DIR, DOCS_DIR))


#############################################
### 
#############################################

