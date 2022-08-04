import subprocess

print("How many nodes do you want?") # prompt for number of desired nodes in the network
totalNodes = int(input())
hostPort = 8080 # desired start port number
nodeNum = 1 # starting node number

f = open('./docker-compose.yml', mode='a')

# edit docker-compose.yml to make node count scalable
for i in range(1, (totalNodes + 1)):
    print(' node' + str(nodeNum) + ':', file=f) # node service declaration
    print('  build: ./node', file=f) # Dockerfile location for build
    print('  command: python3 ./node.py', file=f) # command on docker compose container launch
    print('  ports:', file=f) # declare ports
    print('   - \"' + str(hostPort) + ':80\"', file=f)
    nodeNum += 1 # increment
    hostPort += 1 #increment host port for availability
f.close() # close the file

# run docker compose file
subprocess.run(["docker", "compose", "up"])

# clean up docker-compose.yml
f = open('./docker-compose.yml', mode='w') # open file for cleanup
print('version: \"3.9\"\nservices:', file=f) # prtint standard lines onto file
f.close() # close file and terminate system