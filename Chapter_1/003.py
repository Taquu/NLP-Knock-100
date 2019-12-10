s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = s.split(" ")
words_sum = []
for word in words:
    words_sum.append(len(word)-word.count(",")-word.count("."))
print(words_sum)
