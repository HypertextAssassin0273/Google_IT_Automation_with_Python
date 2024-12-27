## Video: Typical Pull Request Workflow on GitHub ##
git clone https://github.com/redquinoa/rearrange.git # dummy url
cd rearrange
ls -l
git log
git checkout -b add-readme
code README.md
git add README.md
git commit -m 'Add a simple README.md file'
git push -u origin add-readme # push the changes to (new) remote branch
# now go to GitHub and create a pull request
# once the pull request is merged, you can delete the branch (both locally and remotely)

## Video: Updating an Existing Pull Request ##
code README.md
git commit -a -m 'Add more information to the README'
git push
# now go to GitHub and see the changes in same pull request
