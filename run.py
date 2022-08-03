# prompt for number of desired nodes in the network
print("How many nodes do you want?")
nodes = int(input())

for i in range(1, nodes):
    # run host command to launch multiple nodes
    print("loop iteration success")