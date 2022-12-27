from collections import Counter
from matplotlib import pyplot as plt

f = open('hlm.txt', encoding='utf-8')
txt = f.read()
f.close()

cnt = Counter(txt)
char_list = []
for char in cnt:
    if char in "\u3000\n。，：！ !“?”《》,;——()（）-:？^~`[]|/+":  # 过滤常见的标点符号、空格等
        continue
    char_list.append([cnt[char], char])
char_list.sort(reverse=True)
# for char in char_list:
#     print(char[0], char[1])

x = []
y = []
for i, char_cnt in enumerate(char_list):
    # print(i, char_cnt)
    x.append(i)
    y.append(char_cnt[0])
plt.axis((0, 100, 0, 60000))
plt.bar(x[:100], y[:100], width=1)
plt.show()
