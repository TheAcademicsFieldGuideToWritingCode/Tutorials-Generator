Welcome, first year computer science students, to the world of using the command line!


Using the command line is like being a chef in a kitchen. Just like how a chef needs to know where all their ingredients are and how to use their tools, you'll need to know where all your files and programs are and how to use the command line tools to interact with them.


Imagine you're making a pizza. You start by gathering all the ingredients you need, like the dough, sauce, cheese, and toppings. In the same way, when you need to work on a project, you start by navigating to the folder where all the files you need are located.


Now, let's say you need to roll out the pizza dough. You'll need to use a rolling pin to flatten it out to the right size and shape. Similarly, when you need to perform a task on your computer, you'll need to use a command line tool to execute the task.


Finally, once you've prepared your pizza, you'll need to put it in the oven and set the temperature and time. In the same way, once you've executed a command, you'll need to wait for the computer to finish the task and give you the results.


So, just like how a chef needs to know how to use their kitchen tools to make a delicious meal, you'll need to know how to use the command line tools to efficiently work on your projects. With practice, you'll become a command line master chef in no time!


Using the Command Line
======================


Introduction
------------


As computer scientists, we often work with the command line interface (CLI) to interact with our computer systems. While it can be intimidating for beginners, using the command line is a powerful tool for managing and manipulating files and directories on our computers. In this lesson, we will learn how to navigate and manipulate files and directories using the command line.


Getting Started
---------------


To get started, we first need to open the terminal on our computer. On a Mac, you can open the terminal by searching for "terminal" in Spotlight Search. On a Windows computer, you can open the command prompt by searching for "command prompt" in the start menu. Once we have the terminal open, we are ready to start using the command line.


Navigating Directories
----------------------


The first thing we need to know how to do is navigate directories in the command line. Directories are like folders on our computer where we can store files. To see what directory we are currently in, we can use the `pwd` command. 


`bash
pwd`


This will print the current working directory to the terminal. To list the contents of the current directory, we can use the `ls` command.


`bash
ls`


This will print a list of all the files and directories in the current directory. To change directories, we can use the `cd` command. For example, if we want to change to a directory called "Documents", we can use the following command:


`bash
cd Documents`


To go back to the previous directory, we can use `cd ..`. This will move us up one level in the directory hierarchy.


Creating and Removing Directories
---------------------------------


To create a new directory, we can use the `mkdir` command. For example, if we want to create a new directory called "Projects", we can use the following command:


`bash
mkdir Projects`


To remove a directory, we can use the `rmdir` command. For example, if we want to remove the "Projects" directory, we can use the following command:


`bash
rmdir Projects`


Note that the `rmdir` command only works on empty directories. To remove a directory and all its contents, we can use the `rm` command with the `-r` flag. For example, if we want to remove the "Projects" directory and all its contents, we can use the following command:


`bash
rm -r Projects`


Creating and Editing Files
--------------------------


To create a new file, we can use the `touch` command. For example, if we want to create a new file called "index.html", we can use the following command:


`bash
touch index.html`


To edit a file, we can use a text editor like `nano` or `vim`. For example, if we want to edit the "index.html" file with `nano`, we can use the following command:


`bash
nano index.html`


This will open the file in the `nano` text editor, where we can make changes to the file. To save the changes and exit `nano`, we can press `ctrl + x`, then `y`, then `enter`.


Conclusion
----------


Using the command line can be a bit intimidating at first, but with practice, it becomes a powerful tool for managing and manipulating files and directories on our computer systems. By learning how to navigate and manipulate files and directories using the command line, we can become more efficient and effective computer scientists.


Using the Command Line: A Beginner's Guide
==========================================


Welcome first year computer science students! Today we are going to talk about using the command line, also known as the command prompt or terminal. The command line is a powerful tool that allows you to interact with your computer in a more direct way than through a graphical user interface. Here are three example use cases for the command line:


1. Navigating the File System
-----------------------------


One of the most common use cases for the command line is navigating the file system. The file system is the way that your computer organizes files and folders. Using the command line, you can navigate through folders, list the contents of a folder, and create or delete files and folders.


For example, to navigate to a folder called "Documents" on your desktop, you would type:


`cd ~/Desktop/Documents`


This command changes the current directory to the "Documents" folder on your desktop. To list the contents of this folder, you would type:


`ls`


This command lists the names of all the files and folders in the current directory. To create a new file called "notes.txt" in this folder, you would type:


`touch notes.txt`


This command creates an empty file called "notes.txt" in the current directory.


2. Installing Software
----------------------


Another common use case for the command line is installing software. Many programming languages and tools require certain software to be installed on your computer in order to work. Using the command line, you can install this software quickly and easily.


For example, to install the Python programming language on your computer, you would open the command line and type:


`sudo apt-get install python3`


This command installs Python 3, the latest version of Python, on your computer. The "sudo" command is used to give yourself administrative privileges, which are required to install software.


3. Automating Tasks
-------------------


Finally, the command line is a powerful tool for automating tasks. Instead of repeating the same set of commands over and over again, you can create scripts that automate these tasks for you. This can save you a lot of time and effort in the long run.


For example, let's say you have a folder with a lot of image files that you need to resize. Instead of manually resizing each image, you can create a script that does it for you. Here is an example of what that script might look like:


```


!/bin/bash
==========


for file in \*.jpg
do
 convert $file -resize 50% resized-$file
done
```


This script uses the "convert" command to resize each image file in the current directory by 50%. It then saves the resized file with a new name, adding "resized-" to the beginning of the file name. You can save this script to a file called "resize.sh" and run it by typing:


`./resize.sh`


This will automatically resize all the image files in the current directory.


I hope this introduction to using the command line has been helpful. Remember, the command line is a powerful tool that can help you navigate your computer, install software, and automate tasks. With a little practice, you'll be using it like a pro in no time!


1. What is the command used to display the contents of a directory?
a) ls
b) cd
c) mkdir
d) touch
2. Which command is used to create a new directory?
a) ls
b) cd
c) mkdir
d) touch
3. How do you navigate to a directory with a space in the name?
a) Use quotation marks around the directory name
b) Use parentheses around the directory name
c) Use curly braces around the directory name
d) Use square brackets around the directory name
4. Which command is used to delete a file?
a) rm
b) cp
c) mv
d) chmod
5. What command is used to move a file from one directory to another?
a) cp
b) mv
c) rm
d) touch


