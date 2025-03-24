import json


def save_to_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"数据已成功保存到 {file_path}")
    except Exception as e:
        print(f"保存文件时出现错误: {e}")


if __name__ == "__main__":
    # 示例嵌套对象
    nested_data = {
        "students": [
            {
                "name": "张三",
                "age": 20,
                "courses": ["数学", "英语"]
            },
            {
                "name": "李四",
                "age": 21,
                "courses": ["物理", "化学"]
            }
        ]
    }
    file_path = 'nested_data.json'
    save_to_json(nested_data, file_path)
    