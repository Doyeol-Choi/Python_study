prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """  # """은 여러줄의 문자열을 입력할때"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())   # input() 임의의 수 키보드 입력
    