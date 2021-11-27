import networkx as nx
import statistics


##### 1 graph #####
'''
# input_path = "./data/edgeweighted_edit.csv"
input_path = "./data/agykapocs_1000_1p.csv"

with open(input_path, 'r') as input_file:
    graph = nx.read_weighted_edgelist(input_file, "\"", ";")
    print(nx.info(graph))
    edges = []
    for edge in graph.edges():
        edges.append(float(str(graph.get_edge_data(edge[0], edge[1])).split(":")[1][1:-1]))
    print("Average edgeweight: " + str(statistics.mean(edges)))
'''


##########################################################################################################


##### Multiple graphs #####

filecount = 1080

nodecount = 0
degreecount = 0
edges = []

for i in range(1, filecount + 1):
    print("file: " + str(i))
    # input_path = "./data/grafok/" + str(i) + "/edgeweighted_edit.csv"
    input_path = "./data/simulation/sim_inf_" + str(i) + ".csv"
    with open(input_path, 'r') as input_file:
        next(input_file) # skip first line
        graph = nx.read_weighted_edgelist(input_file, "\"", ";")
        # print(nx.info(graph))
        nodecount += len(graph.nodes())
        degree_list = graph.degree()
        for degree in degree_list:
            degreecount += degree[1]
        for edge in graph.edges():
            edges.append(float(str(graph.get_edge_data(edge[0], edge[1])).split(":")[1][1:-1]))

print("###############")
print("Average number of nodes: " + str(nodecount / filecount))
print("Average number of edges: " + str(len(edges) / filecount))
print("Average node degree: " + str(degreecount / filecount / 1000))
print("Average edgeweight: " + str(statistics.mean(edges)))
