def compare(s1,s2):
    ngrams = [ s1[i:i+3] for i in range (len(s1)) ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1),len(s2))

st1='string'
st2='strong'
print(compare(st1,st2))
