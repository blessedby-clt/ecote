n = int(input())
student_info = []
for info in range(n):
    student_info.append(input().split())

student_info.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for name in student_info:
    print(name[0])