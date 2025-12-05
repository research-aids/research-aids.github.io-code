# research-aids.github.io-code
Helper and code repository for the research-aids.github.io repository. The latter is a fork that automatically gets overridden by its parent repo at https://github.com/colonial-heritage/research-guides-dev/, which is why helper functions are stored here.

research-aids.github.io will automatically pull files and scripts to run from here, so precise locations and names are crucial. The idea is that (as much as that's possible), the research-aids.github.io is created fully automatically with the contents of its parents and the contents of this repository.
--> DON'T TOUCH ANYTHING IF YOU DON'T KNOW WHAT YOU'RE DOING

## contents

 - `docs/`, the folder which contains the Just-the-Docs setup:
   - `Gemfile` & `Gemfile.lock` (part of Just-the-Docs)
   - `_config.yml` (part of Just-the-Docs, _edited_)
   - `setup_just-the-docs.py` (script that sets up the Just-the-Docs template for the repo by distrubting files
 - ~~scipt which adds buttons to the markdown (./EXPORTS/MD) versions of the RAs~~ -> this happens already in the exports script in research-guides-dev
 - GitHub Action files:
   - `sync-fork.yml` (cleans up (and restructures) the fork after syncing with --force)
   - `pages.yml` (part of Just-the-Docs, builds and deploys the page; _edited_)
   - `ci.yml` (part of Just-the-Docs)
   


## sync-fork

The below strategy works because:

 - commits to the forked repo are only overridden by a sync if they clash with the parent's commits -> therefore, files that are exclusive to the fork are untouched (in this case the file `./github/workflows/sync-fork.yml`, which does the sync itself)
 - the `--force` strategy is used, which discards all commits from the fork and basically turns the fork into an exact copy of its parent -> the scripts of this repository then rearrange the fork from scratch

Does the following:

 - syncs `research-aids/research-aids.github.io` with its parent `colonial-heritage/research-guides-dev` using the `--force` strategy, which overrides all commits in this repo (that conflict with the parent's commits)
 - copies the files from this repo itself over to the repository it was run in and distributes them accordingly; **including**
   -  **the sync-fork script itself**, thus ensuring it will continue to run
   -  the Just-the-Docs action YAML files -> does that affect deployment?
 - 



## (automatically) setting up just-the-docs

(main tutorial for setting up in an existing repo here: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md#hosting-your-docs-from-an-existing-project-repo)

 1. get the .zip template file
 2. add `pages.yml` to `.github/workflows` (-> this tells GitHub to create 'Actions');  
    edit `pages.yml` acc. to https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md#modify-the-github-actions-workflow
 3. make a `docs` folder and copy all remaining files from the .zip into it
 4. edit the `_cofig.yml` like so: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md#publishing-your-site-on-github-pages
 5. `index.html` is the landing page of the research-aids.github.io


## one-time set up 
_(when the website  repo is created)_

 1. go to the Settings tab -> Pages -> Build and deployment, then select "Source: GitHub Actions" (as mentioned in https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md#publishing-your-site-on-github-pages)
 2. add `sync-fork.yml` from this repo to the repo's `.github/workflows` folder -> this creates the corresponding action which runs on a schedule



## TODOs

**exporting**
 - "Related Aids" table -- ".md" extension instead of ".yml"
  


**website content**
 - links should open in new tab (HTML link target="_blank" behaviour)
 - Dutch version is main version (and only item in navigation bar); Dutch version contains link to English version
 - download buttons for PDF and DOCX are hideous
 - make colonial-heritage/research-aids/REAMDE.md landing page of website (i.e. add to research-aids.github.io/docs/ and add front-matter
 - add colonial-heritage/research-aids/handbook.md to website
 - add colonial-heritage/research-aids/LICENSE to website
 - titles in navbar are in English -> replace with actual title
