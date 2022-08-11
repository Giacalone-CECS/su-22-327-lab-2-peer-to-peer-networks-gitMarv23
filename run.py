import subprocess

print("Enter the number of desired nodes for your network:") # prompt for number of desired nodes in the network
totalNodes = int(input())
hostPort = 8080 # desired start port number
nodeNum = 1 # starting node number

# write total nodes in our system to file
f = open('./node/totalNodes.txt', mode='w')
print(str(totalNodes), file = f)
f.close()

f = open('./docker-compose.yml', mode='a')

# edit docker-compose.yml to make node count scalable
for i in range(1, (totalNodes + 1)):
    print(' node' + str(nodeNum) + ':', file = f) # node service declaration
    print('  build: ./node', file = f) # Dockerfile location for build
    print('  command: python3 ./node.py', file = f) # command on docker compose container launch
#    print('  command: sh -c /bin/sh', file = f) # test run docker features
    print('  ports:', file = f) # declare ports
    print('   - \"' + str(hostPort) + ':80\"', file = f)
    print('  volumes:', file=f) #container can interact with my host file directory
    print('   - ' + './nodes'+ str(nodeNum) + ':' + '/file', file = f) #declare volumes
    nodeNum += 1 # increment
    hostPort += 1 #increment host port for availability
f.close() # close the file

# run docker compose file
subprocess.run(["docker", "compose", "up", "--build"])


# clean up docker-compose.yml
f = open('./docker-compose.yml', mode='w') # open file for cleanup
print('version: \"3.9\"\nservices:', file = f) # print standard lines onto file
f.close() # close file and terminate system
