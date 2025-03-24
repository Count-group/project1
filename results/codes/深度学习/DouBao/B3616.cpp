#include <iostream>

const int MAX_SIZE = 100000;

class Queue {
private:
    int data[MAX_SIZE];
    int front;
    int rear;
    int size_;

public:
    Queue() : front(0), rear(0), size_(0) {}

    void push(int x) {
        if (size_ < MAX_SIZE) {
            data[rear] = x;
            rear = (rear + 1) % MAX_SIZE;
            size_++;
        }
    }

    void pop() {
        if (size_ > 0) {
            front = (front + 1) % MAX_SIZE;
            size_--;
        } else {
            std::cout << "ERR_CANNOT_POP" << std::endl;
        }
    }

    void query() {
        if (size_ > 0) {
            std::cout << data[front] << std::endl;
        } else {
            std::cout << "ERR_CANNOT_QUERY" << std::endl;
        }
    }

    void size() {
        std::cout << size_ << std::endl;
    }
};

int main() {
    int n;
    std::cin >> n;

    Queue queue;

    for (int i = 0; i < n; i++) {
        int op;
        std::cin >> op;

        if (op == 1) {
            int x;
            std::cin >> x;
            queue.push(x);
        } else if (op == 2) {
            queue.pop();
        } else if (op == 3) {
            queue.query();
        } else if (op == 4) {
            queue.size();
        }
    }

    return 0;
}    