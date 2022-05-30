# 정규식 표현. 전화번호, 주민번호 가리기
#phone_jumin.py

data = '''
park 950101-1010101
kim 960202-2020202
lee 901218-2456254
'''

# result=[]
# for line in data.split('\n'):
#     word_result = []
#     for word in line.split(' '):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + '-' + '*******'
#         word_result.append(word)
#     result.append(' '.join(word_result))
# print('\n'.join(result))

import re       # 정규식 표현 하기 위한 re 모듈

data = """
park 800905-1049118
kim 980905-1059119
lee 901218-2456254
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

pat = re.compile("\d{6}[-](\d{7})")
print(pat.sub("******-\g<1>", data))

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7796
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)
print(result)

pat = re.compile("(\d{3})[-](\d{4})[-](\d{4})")
result = pat.sub("\g<1>-####-\g<3>", s)
print(result)

pat = re.compile("(\d{3})[-](\d{4}[-]\d{4})")
result = pat.sub("###-\g<2>", s)
print(result)