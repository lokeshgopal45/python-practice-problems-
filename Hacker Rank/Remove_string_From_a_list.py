test_list = ["bad", "GeeksforGeeks", "bad", "is", "best", "bad"]
target="bad"
for i in test_list:
    if i==target:
        test_list.remove(i)
print(test_list)
