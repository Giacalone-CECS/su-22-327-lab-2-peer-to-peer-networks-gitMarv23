# prompt for number of desired nodes in the network
print("How many nodes do you want?")
nodes = int(input())

for i in range(1, nodes):
    # run host command to launch multiple nodes
<<<<<<< Updated upstream
    print("loop iteration success")
=======
    subproceses.Popen(["docker", "run", "-it", "su-22-327-lab-2-peer-to-peer-networks-gitmarv23_node"])
>>>>>>> Stashed changes
