## Video: Squashing Changes ##
# NOTE: this squashing process is done for an existing pull request
git rebase -i master # opens an editor with a list of commits (in interactive mode)

# in the editor, change the word "pick" to "squash" for the commits you want to squash:
pick 736d754 Add a simple README file
squash 01231b0 Add more information to the README # pick -> squash
(...)

# after saving, you will be prompted with another editor screen to edit the commit message:
# This is a combination of 2 commits. 
# This is the 1st commit message:
Add a simple README file
# This is the commit message #2:
Add more information to the README
(...)

# after saving and closing the editor, the commits will be squashed
git show # see the squashed commit
git status # tells us that our local branch has diverged from the remote branch
git log --graph --oneline --all -4 # shows us that both branches are on different paths

git push # this will get rejected (since it can't be fast-forwarded)
git push -f # force push to the remote branch
git log --graph --oneline --all -4 # the squashed commit is now at the top and commit history is linear
# now go to GitHub and see the changes in the pull request
