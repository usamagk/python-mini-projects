# Automatic File Sorter



A script that looks at a messy folder full of mixed file types and automatically organizes everything into subfolders based on file extension - CSVs go into one folder, code files into another, images into another, and so on. Basically solving the "my Downloads \& Desktop folder is chaos" problem with a few lines of Python instead of doing it by hand.

## How it works

1. Points to a target folder (in this case, a Desktop folder full of mixed files)
2. Lists everything currently inside that folder using `os.listdir()`
3. Defines the destination folders it needs: `csv\\\\\\\_files`, `code\\\\\\\_files`, `png\\\\\\\_files`, `jpg\\\\\\\_files`, `text\\\\\\\_files`
4. Creates any of those folders that don't already exist yet, using `os.makedirs()`
5. Loops through every file in the folder and checks its extension
6. Uses `shutil.move()` to move each file into its matching folder, based on a simple `if`/`elif` chain checking the file extension
7. Includes a check so it won't try to move a file into a folder if a file with the same name already exists there, avoiding overwrite errors

## Why I built it this way

Rather than sorting files by hand or writing one giant nested condition, this breaks the problem into two clear steps: first make sure the destination folders exist, then move each file to where it belongs based on its extension. It's simple, but it's the same core logic real file-organization tools use, checking file type and routing accordingly.

## Tools used

* Python (`os`, `shutil`)
* Jupyter Notebook - Anaconda



## How to run it

Run `automatic\\\_file\\\_sorter.py` and enter your messy folder's path.

\*\*Note:\*\* This script moves real files on your system. Test it on a sample/dummy folder first before pointing it at anything important.

## What I'd improve next

* Make the extension list dynamic instead of hardcoded, so it can handle any file type it encounters, not just the five predefined ones
* Add a "catch-all / other" folder for file types that don't match any known category
* Add basic logging so you can see a summary of what was moved where after running it

\---

\*Part of my Python Mini Projects collection.\*

