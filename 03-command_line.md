# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > * The 'ls' command lists all of the contents of a directory.
* 'ls -a' lists all contents, including hidden files (files with names that begin with '.')
* 'ls -l' lists all contents in the long format. This means that instead of just listing directory or file names, the command also returns information about the directories/files: permissions, element type, owner, group the user belongs to, timestamp of last modification, and directory/file name.
* 'ls -lh' is a combination of using the '-l' and '-h' options. Adding the '-h' to 'ls -l' modifies the way the directory/file size is displayed as output so that the suffixes Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, and Petabyte are used to reduce the number of digits displayed for file size to 3 or less. For example, where 'ls -l' would display 2210, 'ls -lh' would display 2.2K
* The following combinations are meaningful: 'ls -al' (provide long format for all contents of directory, including those with dot names), 'ls -alh' (same as 'ls -al' except for changing the way directory/file sizes are displayed). It is not meaningful to use -h without -l, so 'ls -h' and 'ls -ah' would not be meaningful combinations.

---


---

What does `xargs` do? Give an example of how to use it.

> > The 'xargs' command reads input (space, tab, newline and end-of-file delimited strings from the standard input) and executes commands with those strings as arguments:
* By default 'xargs' takes an input and executes /bin/echo on it. For example, entering 'xargs' alone will prompt the user to provide an input. If a user were to input the text 'hello' followed by 'ctrl + d', the output returned would be 'hello'.
* The 'xargs' command is most commonly combined with other commands from which the output is a list of file names. In these cases 'xargs' is placed to the right of a '|' after a command and takes the list of file names produced as output from the command to the left of the '|' as input and executes a command across all of those files.
* **Example:** 'xargs' can be combined with the 'find' command to perform an action (such as deleting or copying) that applies to all files meeting certain criteria. If I wanted to remove all files with a '.wav' extension, I could use the following command to acheive this: find . -name "*.wav" | xargs rm
* **Note:** if any file names have whitespace in them (i.e. My File Is Here.wav), then -print0 and -0 need to be added as follows to include these files in the execution of the commands: find . -name "*.wav" -print0 | xargs -0 rm

---

