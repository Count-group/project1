import numpy as np


def calculate_eigen(matrix):
    try:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors
    except np.linalg.LinAlgError:
        print("矩阵特征值计算失败，请检查矩阵是否为方阵。")
        return None, None


if __name__ == "__main__":
    # 定义一个示例矩阵
    matrix = np.array([[1, 2], [2, 1]])
    eigenvalues, eigenvectors = calculate_eigen(matrix)
    if eigenvalues is not None and eigenvectors is not None:
        print("特征值：")
        print(eigenvalues)
        print("特征向量：")
        print(eigenvectors)
    