# TextSummarizer
Quick, free, open-source text-summarizer for personal usage.

## Quick tips

### Shell alias (quick access):

Enter something similar in your shell start-up file (example: ~/.bashrc for BASH on Linux):

```
# Shorthand directories
export TOOLS_LOCATION="~/TOOLS_AND_ASSISTANTS/"
export SUMMARIZER_LOCATION="${TOOLS_LOCATION}TextSummarizer"

# Shortcuts
alias TOOLS="cd ~/TOOLS_AND_ASSISTANTS/"
alias TEXT_SUMMARIZER="cd ${SUMMARIZER_LOCATION} && echo \"Type 'textSum' to su>

# Commands
alias textSum="python ${SUMMARIZER_LOCATION}text-summarizer.py"
alias sum_file="nano ${SUMMARIZER_LOCATION}sumy-input.txt"
alias sum_file_clear="echo '' > ${SUMMARIZER_LOCATION}sumy-input.txt"
```
