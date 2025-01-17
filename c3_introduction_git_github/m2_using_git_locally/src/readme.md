##  Notes

<br>

* Branch: A pointer to a particular commit.
* The default branch that git creates for you when a new repository is initialized is called **master**.
* We can use the git branch command to list, create, delete, and manipulate branches.
* Merging: The term that Git uses for combining branched data and history together.
* Git uses two different algorithms to perform a merge: fast-forward and three-way merge.
* Git uses HEAD alias to represent the currently checked-out snapshot of your project
* .gitignore file: Ignore file that get automatically generated by our scripts that we don't want in our repo
* `git commit -a` : A shortcut to stage any changes to tracked files and commit them in one step, if the modified file has never been committed to the repo, we'll still need to use `git add` to track it first
* `git log -p`: `-p = patch`, gives us the patch that was created
* `git show`: Display the information about the commit and the associated path
* `git log --stat`: Show stats about the changes in the commit, like whick file were changed and how many lines were added/removed
* `git diff --staged`: See the changes that are staged but not commited
* `git rm`: Remove files from your repository, will stop the file from being tracked by git 
* `git mv`: Rename files in the repository
* `git checkout`:  reverts changes to modified files before they are staged.
* We can also use git checkout to check out the latest snapshot for both files and for branches.
* `git add *`: the star is a file glob pattern, that expands to all files
* `git commit --ammend`: overwrite the previous commit
* Avoid amending commits that have already been made public
* `git revert`: creates a commit that contains the inverse of all the changes made in the bad commit in order to cancel them out
