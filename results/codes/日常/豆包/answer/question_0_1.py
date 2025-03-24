import ast

input_string = "[[498,248,125,36,-76],[332,484,123,28,-81],[338,580,202,48,-79]]"

try:
    result_list = ast.literal_eval(input_string)
    print(result_list)
except SyntaxError:
    print("输入的字符串格式有误，请检查。")
    