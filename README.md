# GitHub Repository Summary: Custom Git-Like Tool

## Project Description
I Built a custom Git-like tool implemented in Python. This tool allows users to perform basic version control operations such as initializing a repository, adding files to the staging area, committing changes, viewing commit history, creating branches, switching between branches, and merging branches.
Its not git "git" , more like a fancy file mover which simulates git like features, but its fun to play around , and its more like git that moves files physically.

## How It Works Internally
1. **Initialization (`init`):** Users can initialize a new repository using the `init` command. This creates the necessary directory structure, including `objects`, `refs`, `commits`, and the `HEAD` file.

2. **Adding Files (`add`):** The `add` command allows users to add files to the staging area. A unique filename based on the file's content is generated, and a copy of the file is placed in the staging area.

3. **Committing Changes (`commit`):** Users can commit changes with the `commit` command. A commit message is provided, and a new commit directory is created in the `commits` folder. Staged files are copied to this directory, and the staging area is cleared.

4. **Viewing Commit History (`log`):** The `log` command displays the commit history by iterating through the commit directories in the `commits` folder and showing their commit messages.

5. **Creating Branches (`branch`):** The `branch` command enables users to create new branches. A branch file is created under `refs/heads` with the branch name.

6. **Switching Between Branches (`checkout`):** Users can switch to a different branch using the `checkout` command. The `HEAD` file is updated to reference the selected branch.

7. **Merging Branches (`merge`):** Merging changes from one branch into another is accomplished with the `merge` command. Currently, this command simply displays a message indicating that changes have been merged.

## Instructions to Use
1. Clone the repository to your local machine using `git clone` or by downloading the ZIP file.

2. Navigate to the project directory using your terminal or command prompt.

Here are instructions on how to run your Simple Git project using two different methods: Command Line Interface (CLI) and the interactive menu (print functions).
currently in script the CLI code is commented out so to use that you remove it from commment state and comment the print functions and vice versa:

Method 1: Interactive Menu (Print Functions)
PS C:\Users\biohacker0\Desktop\mygit> python mygit.py

# You will be prompted to enter the repository name
Enter repository name: myrepo

# The interactive menu will be displayed
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: init

# You will be informed that the repository is initialized
Initialized empty repository in repos\myrepo

# The menu continues to be displayed for further actions
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: add

# You will be prompted to enter file paths separated by spaces
Enter file paths (space-separated): file1.txt file2.txt

# You will receive a message that the files are added to the staging area
Added 'file1.txt' to the staging area as 'repos\myrepo\staging_area\<file_hash1>'
Added 'file2.txt' to the staging area as 'repos\myrepo\staging_area\<file_hash2>'

# The menu continues for further actions
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: commit

# You will be prompted to enter a commit message
Enter commit message: First commit

# You will receive a message that the commit is successful
Committed 1: First commit

# The menu continues for further actions
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: log

# You will see the commit history
Commit history:
Commit 1: First commit

# The menu continues for further actions
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: branch

# You will be prompted to enter a branch name
Enter branch name: feature-branch

# You will receive a message that the branch is created
Created branch 'feature-branch'

# The menu continues for further actions
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: checkout

# You will be prompted to enter a branch name to switch to
Enter branch name: feature-branch

# You will receive a message that you've switched to the new branch
Switched to branch 'feature-branch'

# The menu continues for further actions
Available actions:
1. Initialize repository (init)
2. Add files to staging area (add)
3. Commit changes (commit)
4. View commit history (log)
5. Create branch (branch)
6. Switch to branch (checkout)
7. Merge branches (merge)
Enter the action: merge

# You will be prompted to enter the source and target branch names for merging
Enter source branch: feature-branch
Enter target branch: main

# You will receive a message that the changes are merged
Merged changes from 'feature-branch' into 'main'

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##Method 2: Command Line Interface (CLI)

   - Initialize a repository:
     ```bash
     python mygit.py init myrepo
     ```

   - Add files to the staging area:
     ```bash
     python mygit.py add myrepo file1.txt file2.txt
     ```

   - Commit changes:
     ```bash
     python mygit.py commit myrepo "Initial commit"
     ```

   - View commit history:
     ```bash
     python mygit.py log myrepo
     ```

   - Create a branch:
     ```bash
     python mygit.py branch myrepo feature-branch
     ```

   - Switch to a branch:
     ```bash
     python mygit.py checkout myrepo feature-branch
     ```

   - Merge branches (Note: This currently displays a message, but you can extend the code to perform actual merges):
     ```bash
     python mygit.py merge myrepo feature-branch main
     ```

     ```

This custom Git-like tool provides a simplified version control system with a command-line interface for basic version control operations. Feel free to extend and customize it according to your needs.
