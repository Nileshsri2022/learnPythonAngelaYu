#!/usr/bin/env bash
#
# Day 70 practice script: walks through the whole Git workflow from the lesson
# (init -> add -> commit -> branch -> merge -> ignore -> inspect) in a throwaway
# repository, so you can watch each command's effect on the real history.
#
# Usage:  bash git_practice.sh
# Nothing in your own project is touched - everything happens in a temp folder.

set -e

WORKDIR="$(mktemp -d)/story"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

echo "Practice repository: $WORKDIR"
echo

step() { printf '\n\033[1m=== %s ===\033[0m\n' "$1"; }

step "git init — create the repository"
git init -q
ls -a | grep -q '.git' && echo "Hidden .git folder created."

step "Create chapter1.txt and commit it"
echo "It was a dark and stormy night." > chapter1.txt
git status --short
git add chapter1.txt
git commit -q -m "Add chapter 1"
git log --oneline

step "Make a second commit"
echo "The plot thickens." >> chapter1.txt
git commit -aqm "Extend chapter 1" || git commit -q -m "Extend chapter 1" -- chapter1.txt
git log --oneline

step "Branch, change something, merge back"
git checkout -q -b chapter-two
echo "Chapter two: the dog arrives." > chapter2.txt
git add chapter2.txt
git commit -q -m "Add chapter 2"
git checkout -q main 2>/dev/null || git checkout -q master
git merge -q chapter-two
git log --oneline

step ".gitignore — keep secrets out"
if [ ! -f .gitignore ]; then
    printf 'secrets.txt\n.DS_Store\n__pycache__/\n*.pyc\n' > .gitignore
    touch secrets.txt
    git add .gitignore
    git commit -q -m "Ignore secrets and OS files"
fi
git status --short
echo "Note: secrets.txt is absent from git status - the ignore rule works."
git check-ignore -v secrets.txt || true

step "Inspect the history"
git log --oneline --graph --all
echo
echo "Files tracked by Git:"
git ls-files

step "Done"
echo "Delete the practice repo whenever you like: rm -rf \"$(dirname "$WORKDIR")\""
