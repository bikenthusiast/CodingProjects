# Add current folder to git repository

Adding a current repository on your laptop loosely adhering to this [tutorial](https://www.softwarelab.it/2018/10/12/adding-an-existing-project-to-github-using-the-command-line/).
1. Create a new repository on GitHub. You can also add a gitignore file, a readme and a licence if you want to.
2. Open Git Bash
3. Change the current working directory to your local project.
4. Initialize the local directory as a Git repository.
5. Enter `git init`
6. Add the files in your new local repository. This stages them for the first commit.
7. Enter `git add` .
8. Commit the files that you’ve staged in your local repository.
9. `git commit -m "initial commit"`
10. Copy the <https url> of your newly created repository
11. In the Command prompt, add the <URL> for the remote repository where your local repository will be pushed.
12. `git remote add origin remote repository <URL>`
13. `git remote -v`
14. Push the changes in your local repository to GitHub. by entering `git push -f origin master`

# Configurate .gitignore files

1. Navigate to the location of your Git repository.
2. Create a `.gitignore` file for your repository by
```bash
touch .gitignore 
```
3. `git rm --cached FILENAME`

# Perform a `git rebase`
   ```bash
    # Get latest develop branch.
    git checkout develop
    git pull
    # Get latest feature branch.
    git checkout feature/My_Awesom_Feature_Branch
    git pull
    # Find the common merge base of the two branches.
    git merge-base feature/My_Awesom_Feature_Branch develop
    # This will print a hash value, called HASH_VALUE in the following, to the console that has to be used in the following.
    git rebase -i HASH_VALUE
    # Text editor will open and print propose something like the following:
    # pick 1fc6c95 do something
    # pick 6b2481b do something else
    # pick dd1475d changed some things
    # pick c619268 fixing typos
    #
    # Change the proposed output so that the commits will be squashed. I.e. replace all but the first "pick" with "squash":
    # pick 1fc6c95 do something
    # squash 6b2481b do something else
    # squash dd1475d changed some things
    # squash c619268 fixing typos
    #
    # Perform the rebase
    git rebase develop
    # Push the changes.
    git push origin [feature-branch] --force-with-lease
    ```