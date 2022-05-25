import numpy as np

def get_total_number_of_spanning_trees(matrix,nodes_count):
    # B1: thay thế các yếu tố đường chéo bằng độ của các nút
    for i in range(nodes_count):
        sum_of_col =0
        for j in range(nodes_count):
            sum_of_col+=matrix[j][i]
        matrix[i][i]=sum_of_col

    # B2: thay thế tất cả các số 1 không thuộc đường chéo = -1
    for i in range(nodes_count):
        for j in range(nodes_count):
            if i!=j and matrix[i][j]==1:
                matrix[i][j]=-1

    # B3: đầu ra này là đồng hệ số 
    matrix=np.delete(matrix, 0, 0)
    matrix=np.delete(matrix, 0, 1)

    return abs(round(np.linalg.det(matrix)))    


if __name__ == '__main__':

    adjacency_matrix=[]

    # Nhập ma trận kề
    nodes_count=int(input("Nhap so hang va cot : "))
    for i in range(nodes_count):
        row=[]
        print('Nhap values dong '+str(i+1)+' cua ma tran ke : ')
        for j in range(nodes_count):
            row.append(int(input()))

        adjacency_matrix.append(row)

    print('\n Ma tran cua ban co phai la: \n')
    for row in adjacency_matrix:
        print(" ".join(map(str,row)))
    
    print('\n Tong so cay khung trong do thi la:', get_total_number_of_spanning_trees(adjacency_matrix,nodes_count))