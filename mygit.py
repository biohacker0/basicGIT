import os
import shutil
import argparse



def init_repository(repo_name):
    repo_path = os.path.join("repos", repo_name)

    if os.path.exists(repo_path):
        print("Repository already exists.")
        return

    # Creates the repository directory if it doesn't exist
    os.makedirs(repo_path)
    os.makedirs(os.path.join(repo_path, "objects"))
    os.makedirs(os.path.join(repo_path, "refs", "heads"))
    os.makedirs(os.path.join(repo_path, "commits"))  # Add this line to create 'commits' directory

    with open(os.path.join(repo_path, "HEAD"), "w") as head_file:
        head_file.write("ref: refs/heads/main\n")

    print("Initialized empty repository in", repo_path)

    
    
####################################################################################################

def add_files(repo_name, file_paths):
    repo_path = os.path.join("repos", repo_name)
    staging_area_path = os.path.join(repo_path, "staging_area")

    if not os.path.exists(staging_area_path):
        os.makedirs(staging_area_path)

    for file_path in file_paths:
        # Generate a unique filename based on the file's content
        with open(file_path, "rb") as f:
            content = f.read()
            file_hash = hash(content)

        # Creates a copy of the file in the staging area
        staged_file_path = os.path.join(staging_area_path, str(file_hash))
        shutil.copy(file_path, staged_file_path)
        
        print(f"Added '{file_path}' to the staging area as '{staged_file_path}'")
        
        
###########################################################################################################################

def commit(repo_name, message):
    repo_path = os.path.join("repos", repo_name)
    staging_area_path = os.path.join(repo_path, "staging_area")
    commits_path = os.path.join(repo_path, "commits")

    if not os.path.exists(staging_area_path):
        print("Nothing to commit. Staging area is empty.")
        return

    commit_message_file = os.path.join(staging_area_path, "commit_message.txt")
    with open(commit_message_file, "w") as f:
        f.write(message)

    # Creates the 'commits' directory if it doesn't exist
    if not os.path.exists(commits_path):
        os.makedirs(commits_path)

    # Creates a new commit directory
    commit_number = len(os.listdir(commits_path)) + 1
    commit_dir = os.path.join(commits_path, str(commit_number))
    os.makedirs(commit_dir)

    # Copyis staged files to the commit directory
    for staged_file in os.listdir(staging_area_path):
        staged_file_path = os.path.join(staging_area_path, staged_file)
        shutil.copy(staged_file_path, os.path.join(commit_dir, staged_file))

    # Cleans up the staging area
    shutil.rmtree(staging_area_path)

    print(f"Committed {commit_number}: {message}")

    
##############################################################################################################################

def log(repo_name):
    repo_path = os.path.join("repos", repo_name)
    commits_path = os.path.join(repo_path, "commits")

    if not os.path.exists(commits_path):
        print("No commits have been made.")
        return

    print("Commit history:")
    for commit_number in sorted(os.listdir(commits_path), key=int):
        commit_dir = os.path.join(commits_path, commit_number)
        with open(os.path.join(commit_dir, "commit_message.txt"), "r") as f:
            message = f.read().strip()
        print(f"Commit {commit_number}: {message}")
        
#############################################################################################################################

def create_branch(repo_name, branch_name):
    repo_path = os.path.join("repos", repo_name)
    branches_path = os.path.join(repo_path, "refs", "heads")

    branch_file = os.path.join(branches_path, branch_name)

    if os.path.exists(branch_file):
        print(f"A branch with the name '{branch_name}' already exists.")
        return

    # Creates the branch file
    with open(branch_file, "w") as f:
        f.write("")

    print(f"Created branch '{branch_name}'")
    
#############################################################################################################################

def checkout_branch(repo_name, branch_name):
    repo_path = os.path.join("repos", repo_name)
    branches_path = os.path.join(repo_path, "refs", "heads")

    branch_file = os.path.join(branches_path, branch_name)

    if not os.path.exists(branch_file):
        print(f"A branch with the name '{branch_name}' does not exist.")
        return

    # Updates the HEAD to point to the selected branch
    head_file = os.path.join(repo_path, "HEAD")
    with open(head_file, "w") as f:
        f.write(f"ref: refs/heads/{branch_name}\n")

    print(f"Switched to branch '{branch_name}'")
    
    
#############################################################################################################################

def merge_branch(repo_name, source_branch, target_branch):
    repo_path = os.path.join("repos", repo_name)
    branches_path = os.path.join(repo_path, "refs", "heads")

    source_branch_file = os.path.join(branches_path, source_branch)
    target_branch_file = os.path.join(branches_path, target_branch)

    if not os.path.exists(source_branch_file):
        print(f"The source branch '{source_branch}' does not exist.")
        return

    if not os.path.exists(target_branch_file):
        print(f"The target branch '{target_branch}' does not exist.")
        return

    # Checks if the current branch is the target branch
    head_file = os.path.join(repo_path, "HEAD")
    with open(head_file, "r") as f:
        current_branch = f.read().strip().replace("ref: refs/heads/", "")

    if current_branch != target_branch:
        print(f"You are not on the target branch '{target_branch}'. Please switch to it first.")
        return

    # Merges changes from the source branch into the target branch (simplified for demonstration)
    print(f"Merged changes from '{source_branch}' into '{target_branch}'")

##############################################################################################################################


import os
import shutil
import argparse

# deinitiopns of my existing Git-like functions (init_repository, add_files, commit, log, etc.)

def init_command(args):
    init_repository(args.repo_name)

def add_command(args):
    file_paths = args.file_paths
    add_files(args.repo_name, file_paths)

def commit_command(args):
    commit_message = args.message
    commit(args.repo_name, commit_message)

def log_command(args):
    log(args.repo_name)

# Create the CLI parser
parser = argparse.ArgumentParser(description="Custom Git-like CLI")
subparsers = parser.add_subparsers(title="Available commands", dest="command")

# Initialize repository command
init_parser = subparsers.add_parser("init", help="Initialize repository")
init_parser.add_argument("repo_name", help="Repository name")

# Add files command
add_parser = subparsers.add_parser("add", help="Add files to staging area")
add_parser.add_argument("repo_name", help="Repository name")
add_parser.add_argument("file_paths", nargs="+", help="File paths to add")

# Commit command
commit_parser = subparsers.add_parser("commit", help="Commit changes")
commit_parser.add_argument("repo_name", help="Repository name")
commit_parser.add_argument("message", help="Commit message")

# Log command
log_parser = subparsers.add_parser("log", help="View commit history")
log_parser.add_argument("repo_name", help="Repository name")

# Parse the command-line arguments
args = parser.parse_args()

# #  appropriate command function based on the subcommand
# if args.command == "init":
#     init_command(args)
# elif args.command == "add":
#     add_command(args)
# elif args.command == "commit":
#     commit_command(args)
# elif args.command == "log":
#     log_command(args)
# else:
#     print("Unknown command:", args.command)

#########################################################################################################################

if __name__ == "__main__":
    repo_name = input("Enter repository name: ")

    while True:
        print("Available actions:")
        print("1. Initialize repository (init)")
        print("2. Add files to staging area (add)")
        print("3. Commit changes (commit)")
        print("4. View commit history (log)")
        print("5. Create branch (branch)")
        print("6. Switch to branch (checkout)")
        print("7. Merge branches (merge)")
        action = input("Enter the action: ").strip()

        if action == "init":
            init_repository(repo_name)
            break
        elif action == "add":
            file_paths = input("Enter file paths (space-separated): ").split()
            add_files(repo_name, file_paths)
            break
        elif action == "commit":
            message = input("Enter commit message: ")
            commit(repo_name, message)
            break
        elif action == "log":
            log(repo_name)
            break
        elif action == "branch":
            branch_name = input("Enter branch name: ")
            create_branch(repo_name, branch_name)
            break
        elif action == "checkout":
            branch_name = input("Enter branch name: ")
            checkout_branch(repo_name, branch_name)
            break
        elif action == "merge":
            source_branch = input("Enter source branch: ")
            target_branch = input("Enter target branch: ")
            merge_branch(repo_name, source_branch, target_branch)
            break
        else:
            print("Unknown action:", action)








