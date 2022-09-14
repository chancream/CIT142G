print("Welcome to the First Come First Serve Scheduling")
inp = int(input("Enter number of processes : "))
d = dict()

for i in range(inp):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process " + str(i + 1) + " : "))
    b = int(input("Enter burst time of process " + str(i + 1) + " : "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l

d = sorted(d.items(), key=lambda item: item[1][0])

ET = []
for i in range(len(d)):
    # first process
    if (i == 0):
        ET.append(d[i][1][1])

    # get prevET + newBT
    else:
        ET.append(ET[i - 1] + d[i][1][1])

TAT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])

WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])

avg_WT = 0
for i in WT:
    avg_WT += i
avg_WT = (avg_WT / inp)

print("Process | Arrival | Burst | Exit  | Turn Around | Wait |")
for i in range(inp):
    print("   ", d[i][0], "   |   ", d[i][1][0], " |    ", d[i][1][1], " |    ", ET[i], "  |    ", TAT[i], "  |   ",
          WT[i], "   |  ")
print("Average Waiting Time: ", avg_WT)




