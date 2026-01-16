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
# Git Rollback Practice

This repository is created to practice Git fundamentals.

## What I practiced
- Git initialization
- Creating commits
- Understanding commit history
- Rollback using:
  - git checkout
  - git reset --soft
  - git reset --hard

## Key Learning
- `git checkout` is used to view old versions safely
- `git reset --soft` removes commits but keeps file changes
- `git reset --hard` removes commits and file changes completely

This practice helped me clearly understand how Git rollback works in real scenarios.
