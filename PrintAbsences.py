n = int(input("학생 수를 입력하세요: "))
daylist = []

for i in range(n):
    att = input("출석 데이터를 입력하세요: ").split()
    daylist.append(att)

count = 0
for student in daylist:
    count += student.count('1')

print(count)
