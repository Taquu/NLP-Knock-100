def n_gram(target, n):
    return [target[num:num+n] for num in range (len(target) - n + 1)]

target = "I am an NLPer"
words = target.split(" ")

#文字のn_gram, n=1
print(n_gram(target, 1))
#単語のn_gram, n=1
print(n_gram(words, 1))
#文字のn_gram, n=2
print(n_gram(target, 2))
#単語のn_gram, n=2
print(n_gram(words, 2))
