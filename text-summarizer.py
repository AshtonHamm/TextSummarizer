#----------------------------
# Imports
#----------------------------
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

#----------------------------
# Fast/full setup
#----------------------------

fast_or_full_setup = int(input("Enter 1 (Fast) or 2 (Full) for full prompts (blank defaults to fast):\n").strip() or "1")

#----------------------------
# Defaults
#----------------------------
# Text File input
file_input = open('sumy-input.txt', 'r')
with open('sumy-input.txt', 'r') as f:
    input_text = f.readlines()

# Lines output
number_lines = 3

if (fast_or_full_setup == 1):
    # Text input
    input_text = """
    Hi, I need you to summarize this please. 
    My name is Ashton Hamm and I am X years old. 
    """
    # Text File input
    file_input = open('sumy-input.txt', 'r')
    with open('sumy-input.txt', 'r') as f:
        text = f.readlines()
    #print(text)
    # User Text input
    input_text = input("Enter the text to summarize:\n") or text
    # Lines output
    number_lines = int(input("Summary length 1-10:\n").strip() or "3")

# Parse the input text
parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
# Create an LSA summarizer
summarizer = LsaSummarizer()
# Generate the summary
summary = summarizer(parser.document, sentences_count=number_lines)
# Output the summary
# print("Original Text:")
# print(input_text)
print("\nSummary:")
for sentence in summary:
    print(sentence)

# Cleanup
file_input.close()

#----------------------------
# SOURCES: 
#----------------------------
#
# 1.SUMY SUMMARIZER
#	https://github.com/miso-belica/sumy?tab=readme-ov-file
#
#
# 2.FILE I/O
# 	https://www.pythontutorial.net/python-basics/python-read-text-file/
#
#----------------------------
