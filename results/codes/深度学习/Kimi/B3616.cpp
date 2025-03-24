#include <iostream>
using namespace std;

class Queue {
private:
    int* data;       // 动态数组存储队列元素
    int capacity;    // 队列容量
    int frontIndex;  // 队首索引
    int rearIndex;   // 队尾索引（下一个元素将插入的位置）
    int count;       // 当前队列中的元素个数

    // 动态扩展数组容量
    void expandCapacity() {
        int newCapacity = capacity == 0 ? 1 : capacity * 2;
        int* newData = new int[newCapacity];
        
        // 将原有元素复制到新数组
        for (int i = 0; i < count; ++i) {
            newData[i] = data[(frontIndex + i) % capacity];
        }
        
        // 释放旧数组，更新指针和容量
        delete[] data;
        data = newData;
        frontIndex = 0;
        rearIndex = count;
        capacity = newCapacity;
    }

public:
    Queue() : capacity(0), frontIndex(0), rearIndex(0), count(0), data(nullptr) {}

    // 向队列中加入一个数 x
    void push(int x) {
        if (count == capacity) {
            expandCapacity();
        }
        data[rearIndex] = x;
        rearIndex = (rearIndex + 1) % capacity;
        count++;
    }

    // 将队首弹出
    void pop() {
        if (count == 0) {
            cout << "ERR_CANNOT_POP" << endl;
            return;
        }
        frontIndex = (frontIndex + 1) % capacity;
        count--;
    }

    // 输出队首元素
    void query() {
        if (count == 0) {
            cout << "ERR_CANNOT_QUERY" << endl;
            return;
        }
        cout << data[frontIndex] << endl;
    }

    // 输出此时队列内元素个数
    void size() {
        cout << count << endl;
    }

    ~Queue() {
        delete[] data;
    }
};

int main() {
    int n;
    cin >> n;

    Queue q;

    for (int i = 0; i < n; ++i) {
        int op;
        cin >> op;

        if (op == 1) {
            int x;
            cin >> x;
            q.push(x);
        } else if (op == 2) {
            q.pop();
        } else if (op == 3) {
            q.query();
        } else if (op == 4) {
            q.size();
        }
    }

    return 0;
}