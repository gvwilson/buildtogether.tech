# Tutorial information
title = "Building Tech Together"
repo = "https://github.com/gvwilson/buildtogether.tech"
author = {
    "name": "Greg Wilson",
    "email": "gvwilson@third-bit.com",
    "site": "https://third-bit.com/",
}
lang = "en"
highlight = "tango.css"
slug = "btt"

chapters = [
    "intro",
    "important",
    "starting",
    "teams",
    "conflict",
    "git-solo",
    "git-team",
    "ip",
    "communicate",
    "testing",
    "design",
    "security",
    "errors",
    "debugging",
    "automation",
    "tooling",
    "process",
    "research",
    "fairness",
    "delivery",
    "finale",
]

appendices = [
    "thinking",
    "methods",
    "onboarding",
    "eval-project",
    "eval-personal",
    "reading",
    "rules-persuade",
    "rules-comfortable",
    "rules-joining",
    "rules-newcomers",
    "rules-research",
    "rules-fired",
    "rules-handover",
    "rules-freelance",
    "rules-change",
    "license",
    "conduct",
    "contrib",
    "bib",
    "glossary",
    "colophon",
    "contents",
]

# What to copy.
copy = [
    "*.svg",
]

# Files and directories to skip.
exclude = {}

# Theme information.
theme = "mccole"
src_dir = "src"
out_dir = "docs"
extension = "/"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
