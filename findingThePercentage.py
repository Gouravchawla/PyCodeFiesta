"""HackerRank link : https://www.hackerrank.com/challenges/finding-the-percentage"""
stuRecords = {}
#n = eval(input())
for i in range(eval(input())):
    inp = input().split()
    stuRecords[inp[0]] = sum(map(float,inp[1:]))/3
#searchKey = input()
print("%.2f" %stuRecords[input()])
#print("%.2f" %result)
#print(format((eval(result[0])+eval(result[1])+eval(result[2]))/3,'.2f'))
