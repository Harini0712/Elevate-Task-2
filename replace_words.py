s1 = 'Gfg is best . Gfg also has Classes now. Classes help understand better .'

rep = {'Gfg': 'It', 'Classes': 'They'}
seen = set()

res = [
    rep[word] if word in rep and word in seen
    else (seen.add(word) or word)
    for word in s1.split()
]

s2 = ' '.join(res)
print(s2)
