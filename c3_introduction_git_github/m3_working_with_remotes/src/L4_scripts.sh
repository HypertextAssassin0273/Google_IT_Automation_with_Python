## Video: Rebasing your changes ##
git checkout master # switch to master branch
git pull # get the latest changes from the remote repository
git log --graph --oneline --all # view the commits in log which we want to rebase
git checkout refactor # switch to the branch we want to rebase
git rebase master # rebase the branch on top of master
git log --graph --oneline --all # view the commits in log after rebasing
git checkout master # switch to master branch
git merge refactor # merge the branch into master
git push --delete origin refactor # delete the remote branch
git branch -d refactor # delete the local branch
git push # push the changes to the remote repository

## Video: Another Rebasing example ##
# NOTE: working on small changes, hence no need to create a new branch
code all_checks.py # modify file
git commit -a -m 'Add a simple network connectivity check'
git fetch # fetch the changes from the remote repository (to see if our colleagues have made any changes, but doesn't merge them)
git rebase origin/master # rebase the local changes on top of the remote changes (NOTE: creates conflict here)
code health_checks.py # fix the conflict
./health_checks.py # test the code (NOTE:gives error here)
code health_checks.py # fix the error
./health_checks.py # test the code
git add health_checks.py
git rebase --continue # continue the rebase process
git log --graph --oneline # view the commits in log after rebasing completely
git push
