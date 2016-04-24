from __future__ import print_function
import codecs
import sys

from enchant.checker import SpellChecker
from enchant.tokenize import HTMLChunker

wordlist = "wordlist.txt"
to_check = "index.html"

spell_checker = SpellChecker("fr_FR", chunkers=[HTMLChunker])

# Add all the words in wordlist.txt to the personal dict
with codecs.open(wordlist, "r", "utf-8") as fp:
    for line in fp:
        spell_checker.add(line.strip())

with open(to_check, "r") as fp:
    text = fp.read()
spell_checker.set_text(text)
errors_found = False
for error in spell_checker:
    errors_found = True
    print("error: ", error.word)
if(errors_found):
    sys.exit(1)
else:
    print("No spelling errors found")
