## Video: Basic Interaction with GitHub ##
git clone <url> # get local copy to your computer
code README.md # create readme file (in VS Code editor)
# NOTE: here you can use any other text editor (like 'atom', 'gedit', 'nano', etc)
git add -a -m "Add one more line to README.md"
git push # push modified README.md to GitHub
git config --global credential.helper cache # caches our credentials for a time window (so we don't need to enter our password with every interaction)
git pull # retrieve new changes from the repository
