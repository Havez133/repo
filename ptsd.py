import os
from datetime import datetime, timedelta
from random import randint as ri

total_day = 365 
commit_freq = 5 
variablity = True 
repo_link = "https://github.com/Havez133/repo.git"

now = datetime(2025, 7, 13)
pointer = 0
tl = total_day
ctr = 1

# Init git
os.system("rm -rf .git") 
os.system("git init")

while tl > 0:
    ct = ri(1, commit_freq) if variablity else commit_freq
    while ct > 0:
        commit_date = now - timedelta(days=pointer)
        formatdate = commit_date.strftime("%Y-%m-%d")
        with open("commit.txt", "a") as f:
            f.write(f"commit ke {ctr}: {formatdate}\n")
        os.system("git add .")
        os.system(f'git commit --date="{formatdate} 12:00:00" -m "commit ke {ctr}"')
        print(f"commit ke {ctr}: {formatdate}")
        ct -= 1
        ctr += 1
    pointer += 1
    tl -= 1

# Push sur ton repo
os.system(f"git remote remove origin || true")
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
