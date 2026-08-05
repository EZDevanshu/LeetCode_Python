st = "fgbecdfebacfgebefcbagfdcefdbebfagdcfhbceia"

freq = {}

for ch in st:
    freq[ch] = freq.get(ch, 0) + 1

sorted_di = sorted(freq.items() , key = lambda x : x[1])
print(sorted_di)