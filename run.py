import subprocess # python subprocess module to run containers

# prompt for number of desired nodes in the network
print("How many nodes do you want?")
nodes = int(input())
hostPort = 8080

for i in range(1, (nodes + 1)):
    # run host command to launch multiple nodes
    subprocess.Popen(["docker", "run", "-itp", str(hostPort) + ":80", "su-22-327-lab-2-peer-to-peer-networks-gitmarv23_node"])

    #increment host port for availability
    hostPort += 1