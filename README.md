# Elevate-Task-2
## 📌 What I Did in This Repository

This repository contains my Python practice and Git workflow learning.

I initially tried to push my Python code to an **already existing GitHub repository**.  
While pushing, I faced errors because the **remote repository already had commit history**, and my local repository history was different.

## ⚠️ Issue Faced

While pushing the code, I encountered the following Git errors:

- `non-fast-forward` error
- `You have not concluded your merge (MERGE_HEAD exists)`

This happened because:
- The remote repository already had commits
- My local branch was behind the remote branch
- Git required me to integrate the remote history first

---

## ✅ Steps I Followed to Fix the Issue

1. Pulled the remote repository history:
   ```bash
   git pull origin main --allow-unrelated-histories
