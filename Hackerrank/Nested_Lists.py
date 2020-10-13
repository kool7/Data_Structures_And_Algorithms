# for _ in range(int(input())):
#     name = input()
#     score = float(input())

n = int(input())
student = [[input(), float(input())] for _ in range (n)]

name, score = zip(*student)

sec_score = sorted(dict.fromkeys(score))[1]

for name, score in sorted(student):
    if score == sec_score:
        print(name)


# score_list = []
# for _ in range(int(input())):
# 	name = input()
# 	score = float(input())v 
# 	mark_sheet.append([name,score])
# 	score_list.append(score)


# second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

# for name,marks in sorted(mark_sheet):
# 	if marks == second_lowest_mark:
# 		print(name)
