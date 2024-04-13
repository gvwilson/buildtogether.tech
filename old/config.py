"""Ark configuration file."""

import os

# Abbreviation for this document.
abbrev = "btt"

# GitHub repository.
repo = "https://github.com/gvwilson/buildtogether.tech"

# Site settings.
lang = "en"
title = "Building Tech Together"
acronym = "BTT"
tagline = "compassion - evidence - process - tools"
author = "Greg Wilson"
email = "gvwilson@third-bit.com"
domain = "third-bit.com"
plausible = False
archive = f"{abbrev}-examples.zip"
draft = True

# Website.
website = f"https://{domain}/{abbrev}/"

# Chapters.
chapters = {
    "introduction": "Introduction",
    "important": "The Important Stuff",
    "starting": "Starting",
    "teams": "Teams",
    "conflict": "Managing Conflict",
    "git-solo": "Using Git On Your Own",
    "git-team": "Using Git Together",
    "ip": "Intellectual Property",
    "communicate": "Communicating",
    "testing": "Testing",
    "design": "Software Design",
    "security": "Security",
    "errors": "Error Handling",
    "debugging": "Debugging",
    "automation": "Automation",
    "tooling": "Tooling",
    "process": "Process",
    "research": "Research",
    "fairness": "Fair Play",
    "delivery": "Wrapping Up",
    "conclusion": "Conclusion",
}

# Appendices (slugs in order).
appendices = {
    "bibliography": "Bibliography",
    "license": "License",
    "conduct": "Code of Conduct",
    "contrib": "Contributing",
    "glossary": "Glossary",
    "thinking": "Thinking",
    "methods": "Research Methods",
    "onboarding": "Onboarding Checklist",
    "project-eval": "Project Evaluation",
    "personal-eval": "Personal Evaluation",
    "reading": "Further Reading",
    "rules-persuade": "How to Talk People Into Things",
    "rules-comfortable": "How to Make Yourself Comfortable",
    "rules-joining": "How to Join an Existing Project",
    "rules-newcomers": "How to Welcome Newcomers",
    "rules-research": "How to be a Good Research Partner",
    "rules-fired": "How to Handle Being Fired",
    "rules-handover": "How to Hand Over and Move On",
    "rules-freelance": "How to Get Started Freelancing",
    "rules-change": "How to Change the World",
    "contents": "Index",
}

# Debug.
debug = False

# Warn about missing or unused entries.
warnings = False

# ----------------------------------------------------------------------

# Theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

# External files.
acknowledgments = "info/acknowledgments.yml"
bibliography = "info/bibliography.bib"
bibliography_style = "unsrt"
credits = "info/credits.yml"
dom = "lib/mccole/dom.yml"
glossary = "info/glossary.yml"
links = "info/links.yml"
thanks = "info/thanks.yml"

# Input and output directories.
src_dir = "src"
out_dir = os.getenv("MCCOLE", "docs")

# Use "a/" URLs instead of "a.html".
extension = "/"

# Files to copy verbatim.
copy = [
    "*.pdf",
    "*.png",
    "*.svg",
    "*.txt",
]

# Exclusions (don't process).
exclude = [
    "*.pdf",
    "*.png",
    "*.py",
    "*.svg",
    "*.txt",
    "*~",
]

# ----------------------------------------------------------------------

# Display values for LaTeX generation.
if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2, "Expect exactly one argument"
    if sys.argv[1] == "--abbrev":
        print(abbrev)
    elif sys.argv[1] == "--chapters":
        print("\n".join(chapters))
    elif sys.argv[1] == "--latex":
        print(f"\\title{{{title}}}")
        print(f"\\subtitle{{{tagline}}}")
        print(f"\\author{{{author}}}")
    elif sys.argv[1] == "--tagline":
        print(tagline)
    elif sys.argv[1] == "--title":
        print(title)
    else:
        assert False, f"Unknown flag {sys.argv[1]}"
