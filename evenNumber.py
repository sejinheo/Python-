num = input("숫자를 입력하세요: ").split()
num = list(map(int, num))
even_count = sum(1 for n in num if n % 2 == 0)
print(even_count)
