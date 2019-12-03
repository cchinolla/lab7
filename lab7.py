from nltk import edit_distance


def edit_dist(word1, word2):
    a = len(word1)+1
    b = len(word2)+1
    lists = {}
    for i in range(a):
        lists[i,0]=i
    for j in range(b):
        lists[0,j]=j
    for i in range(1, a):
        for j in range(1, b):
            dist = 0 if word1[i-1] == word2[j-1] else 1
            lists[i,j] = min(lists[i, j-1]+1, lists[i-1, j]+1, lists[i-1, j-1]+dist)
    return lists[i,j]


str1 = input("please enter your first word:\n")
str2 = input("please enter your second word:\n")

print("The Edit Distance is: %d" % (edit_distance(str1, str2)))
