# NOTE: in all scripts, we are using 'code' as the text editor. You can use any text editor of your choice like 'atom', 'vim', 'gedit', etc

# Video: Basic Interaction with GitHub
git clone <url> # get local copy to your computer
code README.md # create readme file (in VS Code editor) 
git add -a -m "Add one more line to README.md"
git push # push modified README.md to GitHub
git config --global credential.helper cache # caches our credentials for a time window so that we don't need to enter our password with every interaction
git pull # retrieve new changes from the repository
