# Enter your code here. Read input from STDIN. Print output to STDOUT
re_day, re_month, re_year = map(int, input().split())
ex_day, ex_month, ex_year = map(int, input().split())

if (re_year, re_month, re_day) <= (ex_year, ex_month, ex_day):
    print(0)
elif (re_year, re_month) == (ex_year, ex_month):
    print((re_day - ex_day) * 15)
elif (re_year == ex_year):
    print((re_month - ex_month) * 500)
else :
    print(10000)