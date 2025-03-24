#include <iostream>
#include <string>

// 定义栈的最大容量
const int MAX_SIZE = 1000000;

// 自定义栈类
class Stack {
private:
    unsigned long long data[MAX_SIZE];
    int top;

public:
    // 构造函数，初始化栈顶指针
    Stack() : top(-1) {}

    // 入栈操作
    void push(unsigned long long x) {
        if (top < MAX_SIZE - 1) {
            data[++top] = x;
        }
    }

    // 出栈操作
    void pop() {
        if (top == -1) {
            std::cout << "Empty" << std::endl;
        } else {
            top--;
        }
    }

    // 查询栈顶元素
    void query() {
        if (top == -1) {
            std::cout << "Anguei!" << std::endl;
        } else {
            std::cout << data[top] << std::endl;
        }
    }

    // 获取栈内元素个数
    int size() {
        return top + 1;
    }
};

int main() {
    int T;
    std::cin >> T;

    for (int t = 0; t < T; ++t) {
        int n;
        std::cin >> n;
        Stack st;

        for (int i = 0; i < n; ++i) {
            std::string operation;
            std::cin >> operation;

            if (operation == "push") {
                unsigned long long x;
                std::cin >> x;
                st.push(x);
            } else if (operation == "pop") {
                st.pop();
            } else if (operation == "query") {
                st.query();
            } else if (operation == "size") {
                std::cout << st.size() << std::endl;
            }
        }
    }

    return 0;
}