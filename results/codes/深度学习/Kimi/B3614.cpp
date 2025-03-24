#include <iostream>
using namespace std;

class Stack {
private:
    unsigned long long* data;
    int topIndex;
    int capacity;

    void expandCapacity() {
        capacity *= 2;
        unsigned long long* newData = new unsigned long long[capacity];
        for (int i = 0; i <= topIndex; ++i) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }

public:
    Stack() : capacity(4), topIndex(-1) {
        data = new unsigned long long[capacity];
    }

    ~Stack() {
        delete[] data;
    }

    void push(unsigned long long x) {
        if (topIndex + 1 >= capacity) {
            expandCapacity();
        }
        data[++topIndex] = x;
    }

    void pop() {
        if (isEmpty()) {
            cout << "Empty" << '\n';
        } else {
            --topIndex;
        }
    }

    unsigned long long query() {
        if (isEmpty()) {
            cout << "Anguei!" << '\n';
            return 0; // 返回值无意义，仅为了编译通过
        } else {
            cout << data[topIndex] << '\n';
            return data[topIndex];
        }
    }

    int size() {
        cout << (topIndex + 1) << '\n';
        return topIndex + 1;
    }

    bool isEmpty() {
        return topIndex == -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        Stack s;
        while (n--) {
            string op;
            cin >> op;
            if (op == "push") {
                unsigned long long x;
                cin >> x;
                s.push(x);
            } else if (op == "pop") {
                s.pop();
            } else if (op == "query") {
                s.query();
            } else if (op == "size") {
                s.size();
            }
        }
    }
    return 0;
}