import networkx as nx
import numpy as np

def init_distances(G, dist):
	for i, u in enumerate(nodes):
		for j, v in enumerate(nodes):
			dist[i][j] = nx.shortest_path_length(G, u, v)
	
	
def find_medico(G, dist,medico_test):
	nodes = G.nodes
	for i, u in enumerate(nodes):
		for j, v in enumerate(nodes):
			if i < j:
				continue
			for k, w in enumerate(nodes):
				if j < k:
					continue
				count_medians = 0
				for putative_med, rho_v in enumerate(nodes):
					if (i != j and i != k and j!=k and
                		dist[i][j] == dist[i][putative_med] + dist[putative_med][j] and
                		dist[i][k] == dist[i][putative_med] + dist[putative_med][k] and
						dist[j][k] == dist[j][putative_med] + dist[putative_med][k]):

						count_medians+=1

				if(count_medians ==0): 				
					if (i != j and i != k and j!=k):
						print("I(u,v,w) for ",u , v,  w, " empty") 

				if(count_medians >1): 
					if (i != j and i != k and j!=k):
						print("I(u,v,w) for ",u , v,  w, " >1") 

				if(count_medians ==1): 
					if (i != j and i != k and j!=k):
						print("I(u,v,w) for ",u , v,  w, " =1") 

				if(count_medians ==1): 
					medico_test[i]+=1
					medico_test[j]+=1
					medico_test[k]+=1                	   					


############ certain graphs """""""""""""""""
G = nx.Graph()





###Q4
#G.add_edge(0, 1)
#G.add_edge(1, 2)
#G.add_edge(2, 3)
#G.add_edge(3, 0)
#G.add_edge(4, 5)
#G.add_edge(5, 6)
#G.add_edge(6, 7)
#G.add_edge(7, 4)
#G.add_edge(0, 4)
#G.add_edge(1, 5)
#G.add_edge(2, 6)
#G.add_edge(3, 7)
#G.add_edge(10, 11)
#G.add_edge(11, 12)
#G.add_edge(12, 13)
#G.add_edge(13, 10)
#G.add_edge(14, 15)
#G.add_edge(15, 16)
#G.add_edge(16, 17)
#G.add_edge(17, 14)
#G.add_edge(10, 14)
#G.add_edge(11, 15)
#G.add_edge(12, 16)
#G.add_edge(13, 17)
#G.add_edge(0, 10)
#G.add_edge(1, 11)
#G.add_edge(2, 12)
#G.add_edge(3, 13)
#G.add_edge(4, 14)
#G.add_edge(5, 15)
#G.add_edge(6, 16)
#G.add_edge(7, 17)

####	  4 --- 5 
####	  |\   /| 
####	  |	0-1 |
####	  |	| | |
####	  |	3-2 |
####	  |/   \|
####	  7	---	6
#### copy in Q4 via (add +10)

#Q3-
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 0)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(0, 4)
G.add_edge(1, 5)
G.add_edge(2, 6)


#	  4 --- 5 
#	   \   /| 
#		0-1 |
#		| | |
#		3-2 |
#		   \|
#	  		6
  		
  		 



##K_23
#G.add_edge(0, 1)
#G.add_edge(0, 2)
#G.add_edge(0, 3)
#G.add_edge(4, 1)
#G.add_edge(4, 2)
#G.add_edge(4, 3)

############ certain graphs """""""""""""""""




if(not(nx.is_connected(G))): 
	print("G not connected and, thus, no k-median graph")

else:
	nodes = G.nodes
	num_nodes = len(nodes)
	dist = np.zeros((len(nodes), len(nodes)), dtype=int)
	init_distances(G,dist)

	medico_test = np.zeros((len(nodes)), dtype=int)
	for i, u in enumerate(nodes):
		medico_test[i] = 0

	find_medico(G, dist, medico_test)

	count_medico_vertices=0
	print(" ** medico vertices are: **")
	for i, u in enumerate(nodes):
		if(medico_test[i] == (num_nodes-1)*(num_nodes-2)/2): # for i, u  |I(u,v,w)|=1 for all pairs v,w
			count_medico_vertices += 1
			print(u)

	if(count_medico_vertices == num_nodes):
		print("G is median graph")

	elif(count_medico_vertices == 0):
		print("G is no k-median graph, k>0")

	else: 
		print("G is proper", count_medico_vertices,"-median graph (but no median graph)")	



