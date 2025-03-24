import numpy as np
import csv


def csv_to_numpy(file_path):
    try:
        data = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    # 尝试将每行数据转换为浮点数
                    float_row = [float(val) for val in row]
                    data.append(float_row)
                except ValueError:
                    print(f"错误: 无法将行 {row} 转换为浮点数。")
        return np.array(data)
    except FileNotFoundError:
        print("错误: 文件未找到。")
    except Exception as e:
        print(f"错误: 发生了未知错误: {e}")
    return None


if __name__ == "__main__":
    file_path = 'example.csv'
    result = csv_to_numpy(file_path)
    if result is not None:
        print("转换后的 NumPy 数组:")
        print(result)
    