import numpy as np

def calculate(values):
    try:
        matrix = np.array(values).reshape(3,3)
    except ValueError as ve:
        print("List must contain nine numbers.")
        return()
    j = 0
    di = {'mean':[], 'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]}
    axis1 = [[],[],[],[],[],[]]
    axis2 = [[],[],[],[],[],[]]
    flattened = []

    for i in range(matrix.shape[0]):
        axis1[0].append(matrix[:,i].mean())
        axis1[1].append(matrix[:,i].var())   
        axis1[2].append(matrix[:,i].std())
        axis1[3].append(matrix[:,i].max())
        axis1[4].append(matrix[:,i].min())
        axis1[5].append(matrix[:,i].sum())

        axis2[0].append(matrix[i,:].mean())
        axis2[1].append(matrix[i,:].var())   
        axis2[2].append(matrix[i,:].std())
        axis2[3].append(matrix[i,:].max())
        axis2[4].append(matrix[i,:].min())
        axis2[5].append(matrix[i,:].sum())  

        flattened.append(matrix.mean())
        flattened.append(matrix.var())   
        flattened.append(matrix.std())
        flattened.append(matrix.max())
        flattened.append(matrix.min())
        flattened.append(matrix.sum())      

    for key in di:
        di[key].append(axis1[j])
        di[key].append(axis2[j])
        di[key].append(flattened[j])
        j += 1  
    print(di)       


calculate([0,1,2,3,4,5,6,7,8])