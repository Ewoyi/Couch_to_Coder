# OPEN SOURCE

# pyhton -m pip install wikipedia :- for windows systems

# pyhton3 -m pip3 install wikipedia :- for macOS

import wikipedia

# print(wikipedia.search("london"))

london = wikipedia.page("london")
# print(london.images)

# find every sentence on london's wikipedia page wher ethe word population is mentioned.
# print(type(london.content))
# split_sentences = london.content.split(".")
# for sentence in split_sentences:
#     if("population" in sentence):
#         print(sentence)
# print(split_sentences)


sentences_with_substring = []

split_sentences = london.content.split(".")

for sentence in split_sentences:
    if("population" in sentence):
        sentences_with_substring.append(sentence)
print(sentences_with_substring)
