def calculateMaxProcessingThroughput(serverTasks):
    # Write your code here
    # [0: 0, 4: 3, 2: 2, 1: 0, 3: 1] [0:0, 1:0, 3:1, 2:2, 4:3]
    # [3:2, 0:3, 1:0,2:1] [1:0, 2:1, 3:2, 0:3]
    n = len(serverTasks)
    total_throughput = 0
    server_dict = {}

    for i in range(n):
        server_dict[serverTasks[i]] = serverTasks[serverTasks[i]]

    sorted_dict = sorted(server_dict.items(), key=lambda item: item[1])

    sorted_dict = [list(item) for item in sorted_dict]

    visited = set()

    for i in range(len(sorted_dict)):
        if sorted_dict[i][0] in visited:
            continue
        else:
            total_throughput += sorted_dict[i][0]
            visited.add(sorted_dict[i][1])
    return total_throughput




# 示例调用
# serverTasks = [3, 0, 1, 0, 2, 1]
# print(calculateMaxProcessingThroughput(serverTasks))  # 应输出任务的不重复数量

serverTasks = [2,1,0]
print(calculateMaxProcessingThroughput(serverTasks))

serverTasks = [3,0,1,2]
print(calculateMaxProcessingThroughput(serverTasks))

serverTasks = [0,4,2,1,3] # 9
print(calculateMaxProcessingThroughput(serverTasks))


# In ByteDance's vast network of data centers, millions of interconnected servers process content requests, handle user interactions, and deliver data to users globally. Each server is part of a dynamic task execution flow, represented by an array serverTasks, where each entry in the array indicates the next server in the chain that will handle a task.
# Optimizing the data pipeline requires careful management of these task handoffs. Once a task is picked up by server i, it triggers a dependency on server serverTasks[i], transferring the load there. However, this data transfer disables both servers i and serverTasks[i] from participating in any further task handoffs, as they are locked due to processing the current load. Therefore, selecting the right servers and managing the chain reactions of these task handoffs is crucial for maximizing throughput.
# Each server at index i points to the next server server Tasks[i], where the task is transferred. Once this transfer occurs, both the sending server and the receiving server become unavailable for subsequent tasks. Your challenge is to select servers in such a way that maximizes the overall throughput score. The throughput score is determined by the sum of the indices of the servers where tasks are successfully handed off.
# Your task is to analyze this network of server-to-server task handoffs, navigate the dependencies, and determine the maximum possible throughput score that can be achieved by optimally choosing the task handoffs.
# Given the array serverTasks, calculate the maximum throughput score achievable by performing these operations in the most efficient way.
# Example
# n = 3
# serverTasks = [0, 1, 2]
# We first select the server at index 0. It points to itself (server 0), and its throughput is 0. So, the current total throughput is 0. Note that server 0 is now blocked.
# Next, we select the server at index 1. It points to itself (server 1), and its throughput is 1. So, the current total throughput becomes 0 + 1 = 1. Note that both servers 0 and 1 are now blocked.
# Then, we select the server at index 2. It points to itself (server 2), and its throughput is 2. So, the current total throughput becomes 0 + 1 + 2 = 3.
# All servers are now blocked.
# Thus, the maximum achievable throughput score is 3.
#
# server Tasks = [3, 0, 1, 2】
# We first select the server at index 2(serverTasks[i] = 1), which points to index 1(serverTasks[1] = 0)
# and its throughput is equal to 1. So, the current total throughput is 1. Note that both i = 1 and i = 2
# are now blocked.
# Next, we select the server at index 3(server Tasks[i] = 2), which points to index 1 but index 1 is
# blocked. So, the current total throughput becomes 1 + 2 = 3. Note that now i = 1, 2, 3 are now
# blocked.
# Finally, we select the server at index 0((server Tasks[i] = 3), which points to index 3 but index 3 is
# blocked. So, the current total throughput becomes 1 + 2 + 3 = 6.
# All servers have been blocked now.
# Thus, the maximum achievable throughput score is 6.
# For more clarity, we show one more way of choosing indices for same sample:
# serverTasks = [3, 0, 1, 2]
# We first select the server at index 0(server Tasks[i] = 3), which points to index 3(serverTasks[3] = 2)
# and its throughput is equal to 3. So, the current total throughput is 3. Note that both i = 0 and i = 3 have been blocked now.
# Next, we select the server at index 2(serverTasks[i] = 1), which points to index 1 and blocks both i = 1 and i = 2.
# Since the throughput at index 2 is equal to 1, the total current throughput becomes 3 + 1 = 4.
# All servers are now blocked. However, note that this achievable throughput score is 4, although it is not optimal.
#
# Function Description
# Complete the function calculateMaxProcessingThroughput in the editor below
# calculateMaxProcessingThroughput has the following parameters):
# serverTasks[n]: An array of integers where each element indicates the next server where the task is to be transferred.
# Returns
# long: The maximum throughput score achievable.
#
# def calculateMaxProcessingThroughput(serverTasks):