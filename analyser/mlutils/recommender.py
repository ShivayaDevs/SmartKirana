from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine

#products 
dictionary=['Milk', 'Cardamom', 'Tea', 'Sugar', 'Soap', 'Shampoo', 'Facewash', 'Bodywash', 'Ghee', 'refined oil', 'wheat flour', 'lentils', 'gram flour', 'tomato ketchup', 'Jam']
def find_index(s):
    for i in range(len(dictionary)):
        if dictionary[i]==s:
            return recommend(i)
# prod_array=[[]]
# arr=np.zeros((16,16),dtype='uint8')
# x=0
# for i in range(1,3):
#     for j in range(1,3):
#         for k in range(1,3):
#             for l in range(1,3):
#                 arr[x][12:16]=np.random.permutation(np.array([i,j,k,l]))
#                 arr[x][4:8]=np.random.permutation(np.array([i,j,k,l]))
#                 x=x+1
# print arr
# with open("dataset.txt", "a") as myfile:
#     np.savetxt(myfile, arr,delimiter=',')          
def recommend(index):
    data = pd.read_csv('analyser/mlutils/dataset.txt', sep=",", header=None)

    data_ibs = pd.DataFrame(index=data.columns,columns=data.columns)

    for i in range(0,len(data_ibs.columns)) :
        # Loop through the columns for each column
        for j in range(0,len(data_ibs.columns)) :
          # Fill in placeholder with cosine similarities
          data_ibs.ix[i,j] = 1-cosine(data.ix[:,i],data.ix[:,j])

    # Create a placeholder items for closes neighbours to an item
    data_neighbours = pd.DataFrame(index=data_ibs.columns,columns=range(1,11))

    # Loop through our similarity dataframe and fill in neighbouring item names
    for i in range(0,len(data_ibs.columns)):
        data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=False)[:10].index

    res=data_neighbours.ix[:,2:4]

    bought=index

    numpyMatrix = res.as_matrix()
    return dictionary[numpyMatrix[bought][0]]