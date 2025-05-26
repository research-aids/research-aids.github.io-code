# research-aids.github.io-code
Helper and code repository for the research-aids.github.io repository. The latter is a fork that automatically gets overridden by its parent repo at https://github.com/colonial-heritage/research-guides-dev/, which is why helper functions are stored here.

research-aids.github.io will automatically pull files and scripts to run from here, so precise locations and names are crucial. The idea is that (as much as that's possible), the research-aids.github.io is created fully automatically with the contents of its parents and the contents of this repository.
--> DON'T TOUCH ANYTHING IF YOU DON'T KNOW WHAT YOU'RE DOING

## contents

 - script which cleans up (and restructures) the fork after syncing
 - scipt which adds buttons to the markdown (./EXPORTS/MD) versions of the RAs
 - GitHub action files:
   - sync-fork.yml
   - ci.yml -- part of Just-the-Docs
   - pages.yml -- part of Just-the-Docs
