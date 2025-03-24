以下是一个将嵌套字典和列表的Python对象保存为JSON文件的示例程序：

```python
import json

# 创建嵌套字典和列表的示例数据
data = {
    "name": "张三",
    "age": 30,
    "hobbies": ["阅读", "编程", "游泳"],
    "address": {
        "city": "北京",
        "district": "海淀区",
        "postcode": 100080
    },
    "scores": [
        {"math": 90, "english": 85},
        {"math": 88, "english": 92}
    ]
}

def save_to_json(data, filename):
    """
    将嵌套字典/列表的Python对象保存为JSON文件
    
    参数:
    data: 要保存的Python数据结构
    filename: 输出的JSON文件名
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"数据已成功保存到 {filename}")
    except Exception as e:
        print(f"保存文件时出错: {str(e)}")

# 使用示例
save_to_json(data, "output.json")
```

### 关键点说明：
1. **json模块**：使用Python标准库中的json模块处理JSON格式的序列化
2. **ensure_ascii参数**：
   - 设为`False`可以正常显示中文等非ASCII字符
   - 设为`True`（默认）时非ASCII字符会被转义为Unicode码
3. **indent参数**：设置缩进量（这里设为4）可以使生成的JSON文件更易读
4. **文件编码**：始终明确指定utf-8编码以避免编码问题
5. **异常处理**：使用try-except块捕获可能发生的I/O错误

### 生成的文件内容示例（output.json）：
```json
{
    "name": "张三",
    "age": 30,
    "hobbies": [
        "阅读",
        "编程",
        "游泳"
    ],
    "address": {
        "city": "北京",
        "district": "海淀区",
        "postcode": 100080
    },
    "scores": [
        {
            "math": 90,
            "english": 85
        },
        {
            "math": 88,
            "english": 92
        }
    ]
}
```

### 扩展说明：
- 如果需要处理日期时间等特殊对象，可以自定义`default`参数来处理无法序列化的对象
- 可以使用`json.dumps()`先转换为JSON字符串再进行其他操作
- 支持的数据类型对应关系：
  - Python字典 ↔ JSON对象
  - Python列表 ↔ JSON数组
  - Python字符串 ↔ JSON字符串
  - Python数字类型 ↔ JSON数字
  - `True`/`False` ↔ `true`/`false`
  - `None` ↔ `null`