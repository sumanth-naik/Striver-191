# Quick Start - Get Your Website URL

## 🎯 Goal: Get a simple website URL your friend can visit

## Steps:

### 1. Push to GitHub

```bash
# Make sure you're in the repo directory
cd /Users/sumanth.naik/Documents/Personal/Striver-191

# Add files
git add Python_DSA_Syntax_Notebook.ipynb requirements.txt runtime.txt

# Commit
git commit -m "Add Python DSA syntax notebook for teaching"

# Push to your branch (replace 'main' with your branch name if different)
git push origin main
```

### 2. Get Your Website URL

After pushing, replace `YOUR_USERNAME` and `YOUR_REPO_NAME` in this URL:

**Interactive Website (Binder):**
```
https://mybinder.org/v2/gh/YOUR_USERNAME/YOUR_REPO_NAME/main
```

**Example:**
If your GitHub username is `sumanth` and repo is `Striver-191`:
```
https://mybinder.org/v2/gh/sumanth/Striver-191/main
```

### 3. Share the Link!

That's it! Your friend can:
- Click the link
- Wait ~2 minutes for first load
- Start learning interactively!

---

## Alternative: Static View (Faster, Read-Only)

If you want instant viewing (but can't run code):

```
https://nbviewer.org/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/Python_DSA_Syntax_Notebook.ipynb
```

---

## Troubleshooting

**Q: Binder says "Building..." for too long?**
- First build takes 2-5 minutes. Be patient!
- Subsequent visits are much faster (cached)

**Q: Want to update the notebook?**
- Just edit, commit, and push again
- Binder will rebuild automatically

**Q: Which branch should I use?**
- Use `main` or `master` (whatever your default branch is)
- Or specify the branch: `.../gh/USER/REPO/BRANCH_NAME`

