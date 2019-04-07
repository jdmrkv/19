#Вариант 2 Маркова
import re
with open('Леннон, Джон — Википедия.html', encoding='utf-8') as fh:
    page = fh.read()

findAll = re.findall(
    r"""<table class="wikitable"[\s\S\w\W\d\D\n]+?</table>$""",
    page,
    re.MULTILINE
)

num_columns = re.findall(
    r'<tr>',
    findAll[0],
    re.MULTILINE
)
num_c = len(num_columns)

num_rows = re.findall(
    r'<th>',
    findAll[0],
    re.MULTILINE
)
num_r = len(num_rows)

clean = re.findall(
    r'>([^<>\n]+)<',
    findAll[0],
    re.MULTILINE
)
print(clean)

for i in range(num_c):
    #print()
    for j in range(num_r):
        #print(clean, end=' ');
        if(j==4):
            print('|', end=' ')
    
"""with open('Леннон Джон.txt', 'w', encoding='utf-8') as f:
    f.write(page)"""
