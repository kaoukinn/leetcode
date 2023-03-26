sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
ans = []
for sentence in sentences:
    a = sentence.split()
    ans.append(len(a))
print(max(ans))


    