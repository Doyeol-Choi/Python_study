import re

# 파이썬에서는 문자열 '', "", """ """, ''' ''' 4가지가 혼용됨
# 여러줄로 할땐 반드시 """, ''' 로 묶어준다.

# data = """
# park 800905-1049118
# kim  980905-1059119
# lee  901218-1456254
# """

# pat1 = re.compile("(\d{6})[-](\d{7})")
# print(pat1.sub("\g<1>-*******", data))

# pat2 = re.compile("(\d{6})[-](\d{7})")
# print(pat2.sub("******-\g<2>", data))

# s = """
# park 010-9999-9988
# kim  010-9909-7789
# lee  010-8789-7796
# """

# pat3 = re.compile("(\d{3}[-]\d{4})[-](\d{4})")
# result1 = (pat3.sub("\g<1>-####", s))
# print(result1)

# pat4 = re.compile("(\d{3})[-](\d{4})[-](\d{4})")
# print(pat4.sub("\g<1>-####-\g<3>", s))

# pat5 = re.compile("(\d{3})[-](\d{4}[-]\d{4})")
# result2 = pat5.sub("$$$-\g<2>", s)
# print(result2)

data = '''
1110-12-27-4428
1157-45-33-9875
3568-98-01-8854
'''

pat = re.compile("(\d{1})\d{3}[-]\d{2}[-]\d{2}[-](\d{4})")
print(pat.sub("\g<1>***-**-**-\g<2>", data))

pat = re.compile("\d{4}[-](\d{2}[-]\d{2})[-]\d{4}")
print(pat.sub("****-\g<1>-****", data))

pat = re.compile("(\d{4}[-]\d{2}[-]\d{2})[-]\d{4}")
print(pat.sub("\g<1>-****", data))


data_2 = data.splitlines()  # split(" ") 따옴표 안을 기준으로 나누어 리스트에 담는다.
                            # splitlines() 줄별로 나누어 리스트에 담는다.
                            # 위의 괄호안에 True가 들어가면 \n도 표기해서 리스트에 담는다.
# data_2 = data.split("\n")

pat = re.compile("(\d{4})[-]\d{2}[-]\d{2}[-](\d{4})")
print(pat.sub("\g<1>-**-**-\g<2>", data_2[1]))

pat = re.compile("\d{4}[-](\d{2}[-]\d{2})[-]\d{4}")
print(pat.sub("****-\g<1>-****", data_2[2]))

pat = re.compile("(\d{4}[-]\d{2}[-]\d{2})[-]\d{4}")
print(pat.sub("\g<1>-****", data_2[3]))