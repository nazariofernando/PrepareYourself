fi = open('input.txt', 'r')

days = int(fi.readline())
practice = map(int, fi.readline().split())
theory = map(int, fi.readline().split())

diff = []

for day in range(0,days):
    diff.append(abs(practice[day]-theory[day]))

practiceDays = 0
theoryDays = 0

solutionList = []

for day in range(0,days):
    if theory[day] >= practice[day]:
        solutionList.append(theory[day])
        theoryDays +=1
    else:
        solutionList.append(practice[day])
        practiceDays += 1

solution = sum(solutionList)

if theoryDays >= days or practiceDays>=days :
    solution -= min(diff)

fo = open('./output.txt', 'w')
fo.write(str(solution))
