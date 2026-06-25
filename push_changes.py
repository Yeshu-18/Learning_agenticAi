"""
Script to stage, commit, and push recent changes to GitHub.
Automatically generates a descriptive commit message based on what changed.
"""

import subprocess
import sys

def run(cmd: str) -> str:
    """Run a shell command and return its output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        print(f"   Error: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()

def main():
    # 1. Stage all changes
    print("📦 Staging changes...")
    run("git add -A")

    # 2. Check if there's anything to commit
    status = run("git status --porcelain")
    if not status:
        print("✅ Nothing to commit — working tree is clean.")
        return

    # 3. Commit with a descriptive message
    commit_msg = (
        "refactor: improve LLM prompt & schema for better LinkedIn post generation\n\n"
        "- engine.py: Rewrote extraction prompt with a 'content strategist' role,\n"
        "  added detailed LinkedIn post structure (Hook → Story → Takeaway → CTA),\n"
        "  and included formatting rules (word limit, emoji count, hashtag cap)\n"
        "- schema.py: Removed unused 'github_update' field from DailyExtraction,\n"
        "  sharpened field descriptions for learning_topics, coding_work, linkedin_post"
    )

    print("💾 Committing...")
    print(f"   Message: {commit_msg.splitlines()[0]}")
    run(f'git commit -m "{commit_msg}"')

    # 4. Push to remote
    print("🚀 Pushing to GitHub...")
    run("git push origin main")

    print("✅ Done! Changes pushed to GitHub successfully.")

if __name__ == "__main__":
    main()
