#!/bin/bash

# Script to push notebook to GitHub and get website URL

echo "🚀 Pushing Python DSA Notebook to GitHub..."
echo ""

# Add files
git add Python_DSA_Syntax_Notebook.ipynb requirements.txt runtime.txt QUICK_START.md WEBSITE_SETUP.md

# Commit
git commit -m "Add Python DSA syntax notebook for interactive learning"

# Push to master branch
git push origin master

echo ""
echo "✅ Successfully pushed to GitHub!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 YOUR WEBSITE URLs:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📚 INTERACTIVE (Recommended - Can run code):"
echo "https://mybinder.org/v2/gh/sumanth-naik/Striver-191/master"
echo ""
echo "📖 STATIC VIEW (Fast - Read only):"
echo "https://nbviewer.org/github/sumanth-naik/Striver-191/blob/master/Python_DSA_Syntax_Notebook.ipynb"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💡 Share the INTERACTIVE URL with your friend!"
echo "   (First load takes ~2 minutes, then it's fast)"
echo ""

