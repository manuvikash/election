p = {}
n = int(input("Enter the number of processes initially - "))
for i in range(n):
    p[i] = True

print("Processes are - ", list(p.keys()))
print(f"The co-ordinator is process {n-1}")
input("Press Enter to kill the coordinator process...")
p[n-1] = False
d = int(input("Enter the process that detects the failure - "))
act = []
current = d
nxt = current
while True:
    if(current in act):
        break
    if(p[current]):
        act.append(current)
    if(current == n-1):
        nxt = 0
    else:
        nxt += 1
    print(f"Process {current} sends active list to {nxt} - ", act)
    current = nxt
    
print(f"\nProcess {current} has all the active processes - ", act)
print(f"Process {max(act)} is elected as the new coordinator")