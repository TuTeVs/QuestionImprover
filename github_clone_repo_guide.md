# How to Fork a github repo, clone it and make my own changes to it, while updating it with the original repository

- Fork original github repository
Click fork on the original github repository

- Clone the forked repository to a directory in my own computer
git clone ForkedRepoURL

- Link the VS Code project to the original repository by adding a remote "upstream"
    - Go to source control and click on the "..."
    - Remote -> "Add Remote"
    - paste in the URL of the original repository
        - if prompted to select a repo, select my own forked github repo
    - write "upstream" as the name of the remote, for conventional purposes

- To pull changes, go to source control and select the "..."
    - select "Push, Pull" -> "Pull from"
    - select upstream

- Whenever I push changes in VS code, they will go to my own repository called "origin"

NOTE: fetch is different from pull, as it allows me to view changes to a repository without committing them to my own

NOTE: Difference between "..." Source control and "..." Source control repositories is that the former
    applies to only the currently selected repository, while the latter applies to all repo's that are open in VS code
