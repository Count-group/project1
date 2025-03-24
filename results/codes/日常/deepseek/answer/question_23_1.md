以下是实现该功能的Python代码：

```python
class IDStore:
    def __init__(self):
        self.name_to_id = {}
        self.id_to_name = {}
    
    def add(self, name, id):
        if name in self.name_to_id:
            raise ValueError(f"Name '{name}' already exists.")
        if id in self.id_to_name:
            raise ValueError(f"ID '{id}' already exists.")
        self.name_to_id[name] = id
        self.id_to_name[id] = name
    
    def __getitem__(self, key):
        # 先尝试作为名字查找
        if key in self.name_to_id:
            return self.name_to_id[key]
        # 再尝试作为ID查找
        elif key in self.id_to_name:
            return self.id_to_name[key]
        else:
            raise KeyError(f"'{key}' not found as name or ID.")
    
    def __contains__(self, key):
        # 支持 in 运算符检查存在性
        return key in self.name_to_id or key in self.id_to_name

# 示例用法
if __name__ == "__main__":
    store = IDStore()
    store.add("Alice", 100)
    store.add("Bob", 200)
    
    print(store["Alice"])  # 输出 100
    print(store[100])      # 输出 Alice
    print(store["Bob"])    # 输出 200
    print(store[200])      # 输出 Bob
    
    # 测试异常情况
    try:
        print(store["Charlie"])
    except KeyError as e:
        print(e)  # 输出 'Charlie' not found as name or ID.
    
    # 测试重复添加
    try:
        store.add("Alice", 300)
    except ValueError as e:
        print(e)  # 输出 Name 'Alice' already exists.
```

### 代码说明：
1. **双向字典存储**：使用两个字典分别保存姓名→ID和ID→姓名的映射关系
2. **添加校验**：在`add`方法中确保姓名和ID的唯一性
3. **灵活访问**：通过重写`__getitem__`方法实现双向查询
4. **包含检查**：实现`__contains__`方法支持`in`运算符
5. **异常处理**：对重复添加和无效查询进行友好的错误提示

该实现可以处理以下情况：
- 通过姓名查询ID
- 通过ID查询姓名
- 自动处理不同类型的键（支持任意可哈希类型）
- 防止重复添加冲突
- 友好的错误提示

你可以通过`add`方法添加新的映射关系，使用方括号`[]`进行双向查询，使用`in`关键字检查是否存在对应的键。