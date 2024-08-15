# SOURCES: 
# 1.
#	https://github.com/miso-belica/sumy?tab=readme-ov-file
# 2.
# 	https://www.pythontutorial.net/python-basics/python-read-text-file/
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
#----------------------------
# Text
# 	- Input text to be
#	  summarized
#----------------------------
# Static input
input_text = """
Hi, I need you to summarize this please. 
My name is Ashton Hamm and I am X years old. 
"""

# File input
file_input = open('sumy-input.txt', 'r')
with open('sumy-input.txt', 'r') as f:
    text = f.readlines()
# User input
input_text = input("Enter the text to summarize:\n") or text
#print(text)

#----------------------------
# Lines
# 	- Summary type/amount
# 	- You can adjust the
# 	  number of sentences
# 	  in the summary.
#----------------------------
# User input
number_lines = int(input("Summary length 1-10:\n").strip() or "3")

# Parse the input text
parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

# Create an LSA summarizer
summarizer = LsaSummarizer()

# Generate the summary
summary = summarizer(parser.document, sentences_count=number_lines)

# Output the summary
#print("Original Text:")
#print(input_text)
print("\nSummary:")
for sentence in summary:
    print(sentence)

# Cleanup
file_input.close()
