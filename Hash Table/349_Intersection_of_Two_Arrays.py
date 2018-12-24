
set_s = set()
set_t = set()
res = []
for i in len(set_s):
    if set_s[i] in set_t:
        res.append(set_s[i])
return res