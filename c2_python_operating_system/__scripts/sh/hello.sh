#!/usr/bin/env bash

echo "KR: annyeong chingus & yeorobun!!"
echo "ENG: hello friends & everyone!!"


# NOTES (linux specific):
# 1) first line is called shebang, it tells the system which interpreter to use
# 2) adding shebang allows you to run the script directly from the terminal without specifying the python interpreter
# 3) in general, we can use shebang to specify the interpreter for any script, not just bash (e.g. python3, perl, ruby, etc)
# 4) never add comments before or after the shebang, otherwise it will not work
# 5) make the script executable using 'chmod +x hello.sh'
# 6) run the script directly using './hello.sh'

# NOTES (wsl specific):
# 1) line endings are important, make sure to use LF instead of CRLF, otherwise you will get error
# 2) use 'dos2unix' command to convert line endings [if you have set 'autocrlf=true' (in git config or in .gitattributes)]
