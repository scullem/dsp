# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >* **man:** Calls up the manual for a given command. Note: to exit out of the documentation and return to the prompt, type 'q'. 
* **cd:** Changes the working directory. Typing 'cd ~' will return you to your home directory. Typing 'cd ..' moves you up one directory in the hierarch, and can be modified by adding /.. for every level of directory you want to move up.
* **mkdir:** Creates a new directory. Note that mkdir -p allows you to create multiple intermediate directories in a path in one command without getting the error 'No such file or directory'. If just creating one new directory in a path, it isn’t needed, but if creating multiple new levels it is needed (i.e. if temp/stuff exists, you don’t need -p to create temp/stuff/things but you will need it to create temp/stuff/things/items).
* **touch:** Creates an empty file. Note: it sets the modifications and access times of a file, but if the file doesn't exist it creates it with default permissions.
* **less:** Displays the contents of a file. It is similar to 'more' but allows both backward and forward movement through a file. In addition, it doesn't require reading the full file prior to starting which can make it faster with large input files.
* **find:** Finds files that meet certain criteria. You can use with -print to pass a list of file names to execute additional commands on this set of files (such as | 'less').
* **cat:** You can use cat to insert text as the contents of a file. Using 'cat > [filename]', followed by text, ending with 'ctrl + d' will insert the text into the specified file. You can also use 'cat' for a similar purpose to 'less'; however, in this case it will dump the whole file onto the display screen with no paging or stopping.
* **grep:** Looks for patterns (i.e. words, sentences, regular expressions, etc.) within files and writes each input line that matches at least one of the patterns to the standard output. For example, 'grep new *.txt' will search all text files for contents that match the word 'new'.
* **pushd/popd:** These commands allow you to bookmark a directory you are in, leave it, and come back to it. Using 'pushd' will save the directory location you are in and move you to a new directory. Using 'popd' will then take you back to the last directory you pushed. Using 'pushd' with no other arguments will switch between your current directory and the last one you pushed, creating an easy way to toggle back and forth between two directories.
* **redirection:** This is not a command but is the act of taking a command and changing where its input/output goes. The '|' takes output from the left and directs it to be input for the command on the right. The '<' sends the input from the file on the right to the program on the left. The '>' takes the output of the command on the left, and writes it to the file on the left. The '>>' takes the output of the command on the left and appends it to the file on the right.


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

