import subprocess # python subprocess module to run containers

print("How many nodes do you want?") # prompt for number of desired nodes in the network
nodes = int(input())
hostPort = 8080 # desired start port number

for i in range(1, (nodes + 1)):
    subprocess.Popen(["docker", "run", "-itp", str(hostPort) + ":80", "su-22-327-lab-2-peer-to-peer-networks-gitmarv23_node"]) # run host command to launch multiple nodes
    hostPort += 1 #increment host port for availability