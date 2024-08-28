import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Version of data by Git tag and branch")
parser.add_argument("git_tag", type=str, help="The Git tag to check out")
parser.add_argument("branch_name", type=str, help="The main branch name to switch to")
args = parser.parse_args()

# Define variables
data_file = "data_version/categories.csv"
dvc_file = "data_version/categories.csv.dvc"
gitignore_file = "data_version/.gitignore"

branch_name = args.branch_name
git_tag = args.git_tag
commit_message = "went back to " + git_tag

# Run DVC and Git commands
subprocess.run(["git", "checkout", git_tag], check=True)
subprocess.run(["dvc", "checkout"], check=True)
subprocess.run(["git", "checkout", branch_name], check=True)

# ---- those here just if you want to push the checked out version again -------------------
# subprocess.run(["dvc", "add", data_file], check=True)
# subprocess.run(["git", "add", dvc_file, gitignore_file,], check=True)
# subprocess.run(["git", "commit", "-m", commit_message], check=True)
# subprocess.run(["dvc", "push"], check=True)
# subprocess.run(["git", "push"], check=True)
