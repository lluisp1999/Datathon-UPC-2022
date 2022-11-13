import pandas as pd

clusters = pd.DataFrame(columns= ['cluster_label', 'c1x','c1y'])
clusters.loc[0] = ['1',0,0]
clusters.loc[1] = ['2',1,0]
clusters.loc[2] = ['3',1,1]
clusters.loc[3] = ['4',0,1]

driver_pairs =  pd.DataFrame(columns= ['d_out', 'd_in','inx','iny','outx','outy'])
driver_pairs.loc[0] = [1,0,0,0,0,1]

number_of_paths= 2#len(driver_pairs)
number_of_clusters = len(clusters)
number_of_clusters_per_path = int(number_of_clusters/number_of_paths)
clusters = clusters.sort_values(by=['c1y'],ascending=False)



driver_pairs['cluster_path_index'] = -1
driver_pairs = driver_pairs.sort_values(by=['outy'],ascending=False)
print(driver_pairs)
cluster_paths = []
cluster_paths_index = 0
for i in range(number_of_paths):
    # print(clusters[(i*number_of_clusters_per_path):((i+1)*number_of_clusters_per_path)]['cluster_label'].to_list())
    cluster_paths.append(clusters[(i*number_of_clusters_per_path):((i+1)*number_of_clusters_per_path)]['cluster_label'].to_list())
    driver_pairs.loc[0,'cluster_path'] = i
print(driver_pairs)
print(cluster_paths)

