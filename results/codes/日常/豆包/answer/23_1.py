class ID:
    def __init__(self):
        self.name_to_id = {}
        self.id_to_name = {}

    def add(self, name, id):
        self.name_to_id[name] = id
        self.id_to_name[id] = name

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.name_to_id.get(key)
        elif isinstance(key, int):
            return self.id_to_name.get(key)
        return None


# 测试代码
if __name__ == "__main__":
    id_manager = ID()
    id_manager.add("Alice", 1)
    id_manager.add("Bob", 2)

    print(id_manager["Alice"])
    print(id_manager[2])
    