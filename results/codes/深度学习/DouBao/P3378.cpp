#include <iostream>
#include <vector>

// 交换两个元素的值
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// 最小堆类
class MinHeap {
private:
    std::vector<int> heap;

    // 向上调整堆
    void siftUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[parent] <= heap[index]) break;
            swap(heap[parent], heap[index]);
            index = parent;
        }
    }

    // 向下调整堆
    void siftDown(int index) {
        int size = heap.size();
        while (true) {
            int leftChild = 2 * index + 1;
            int rightChild = 2 * index + 2;
            int smallest = index;

            if (leftChild < size && heap[leftChild] < heap[smallest]) {
                smallest = leftChild;
            }
            if (rightChild < size && heap[rightChild] < heap[smallest]) {
                smallest = rightChild;
            }

            if (smallest == index) break;
            swap(heap[index], heap[smallest]);
            index = smallest;
        }
    }

public:
    // 插入元素到堆中
    void push(int value) {
        heap.push_back(value);
        siftUp(heap.size() - 1);
    }

    // 获取堆顶元素
    int top() {
        return heap[0];
    }

    // 删除堆顶元素
    void pop() {
        if (heap.empty()) return;
        swap(heap[0], heap[heap.size() - 1]);
        heap.pop_back();
        siftDown(0);
    }

    // 检查堆是否为空
    bool empty() {
        return heap.empty();
    }
};

int main() {
    int n;
    std::cin >> n;

    MinHeap minHeap;

    for (int i = 0; i < n; ++i) {
        int op;
        std::cin >> op;

        if (op == 1) {
            int x;
            std::cin >> x;
            minHeap.push(x);
        } else if (op == 2) {
            if (!minHeap.empty()) {
                std::cout << minHeap.top() << std::endl;
            }
        } else if (op == 3) {
            if (!minHeap.empty()) {
                minHeap.pop();
            }
        }
    }

    return 0;
}    