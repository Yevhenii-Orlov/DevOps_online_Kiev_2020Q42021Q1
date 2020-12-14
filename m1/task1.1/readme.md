DevOps is a combination of knowledge of administration, programming, knowledge of network, cloud and other technologies for synchronization and coordination over all areas of the development of a large team, but, first of all, it is a methodology, a kind of standardized production cycle-approach.
DevOps bring stability and control to the development team, testers and admins, which is invaluable when developing complex working systems, as well as a DevOps engineer will create a powerful preventive barrier to the emergence of bugs and communication problems in the team.

##### After installing GIT on my machine.
##### I cloned the repo from the GitHub service to my machine.
##### And I started working locally.
##### I created the folders "m1","m1/task1.1" "m2" and move to the /m1/task1.1.
`$ cd m1/task1.1/`.
##### I created the text file readme.txt in 'main' branch and commit it.
`$ git add .`.
`$ git commit -m "Create readme.txt"`.
##### My next step was to create a new branch 'develop' and checkout to it.
`$ git checkout -b develop`.
##### In this branch were created empty index.html file and commit this action.
`$ vi index.html`.
`$ git add index.html`.
`$ git commit -m "Create index.html"`.
##### My next step was to create a new branch 'images' and checkout to it.
`$ git checkout -b images`.
##### The images folder was created in this branch. 
##### An image has been added to it.
##### After that the index.html file was changed.
##### The changes have been committed.
`$ mkdir images`.
`$ nano index.html`.
`$ git add index.html`.
`$ git commit -m "Changed index.html"`.
##### My next step was to create a new branch 'styles' and checkout to it.
`$ git checkout -b styles`.
##### The styles folder was created in this branch. 
##### An styles has been added to it.
##### After that the index.html file was changed.
##### The changes have been committed.
`$ mkdir styles`.
`$ nano index.html`.
`$ git add index.html`.
`$ git commit -m "Changed index.html"`.
##### My next step was to merged images and develop branchs.
`$ git merge images` - while being on the develop branch.
##### My next step was to merged styles and develop branchs. 
`$ git merge styles` - while being on the develop branch.
##### After successfully merging branches, I merged branches main and develop.
`$ git merge develop` - while being on the main branch.
##### After successfully merging branches main and develop, I check origin repo.
`$ git remote -v`.
##### I pushed my local repo to the repo in the GitHub.
`$ git push origin --all`.
##### Using command 'git reflog', I brought out the repo logs and wrote them to a file.
