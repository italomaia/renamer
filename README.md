Do you like pyrenamer? Would like a command line tool that allows you to rename your files just like pyrenamer does?
Well, search no more! Renamer does exactly that. Most of the code core is from pyrenamer anyway.

## Supported patterns
* {#} Numbers
* {L} Letters
* {C} Characters (Numbers & letters, not spaces)
* {X} Numbers, letters, and spaces
* {@} Trash


Usage
=====
    > ls
    >> 1.txt
    >> 2.txt
    >> foo.bar
    > ./renamer.py {X}.txt {1}.c
    >> 1.txt -> 1.c
    >> 2.txt -> 2.c
    > ls
    >> 1.txt
    >> 2.txt
    > ./renamer.py {X}.txt {1}.c -p
    > ls
    >> 1.c
    >> 2.c

