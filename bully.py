p = {}
n = int(input("Enter the number of processes initially - "))
for i in range(n):
    p[i] = True

print("Processes are - ", list(p.keys()))
print(f"The co-ordinator is process {n-1}")
input("Press Enter to kill the coordinator process...")
p[n-1] = False
d = int(input("Enter the process that detects the failure - "))
for i in range(d, len(p)):
    if(p[i]):
        print()
        for j in range(i+1, len(p)):
            print(f"Process {i} sends election message to process {j}")
            if(p[j]):
                print(f"Process {j} sends reply message to process {i}")
                break


print(f"\nProcess {i-1} is elected as the new coordinator")

input("Press enter to revive old coordinator...")
p[n-1] = True

print(f"Process {n-1} sends coordinator message to processes - ", list(p.keys())[:n-1])

print(f"Process {n-1} is the new coordinator by bullying")