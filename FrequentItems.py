from collections import Counter

text = "The key improvement between SimpleText and " \
       "TeachText was the addition of text styling. " \
       "SimpleText could support multiple fonts and " \
       "font sizes, while TeachText supported only a single font per document. " \
       "Adding text styling features made SimpleText WorldScript-savvy, " \
       "meaning that it can use Simplified and Traditional Chinese characters." \
       "Like TeachText, SimpleText was also limit."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)