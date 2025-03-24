#include <iostream>
#include <vector>
using namespace std;

vector<int> heap;

// 上浮操作，维护堆的性质
void heapify_up(int index) {
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap[parent] > heap[index]) {
            swap(heap[parent], heap[index]);
            index = parent;
        } else {
            break;
        }
    }
}

// 下沉操作，维护堆的性质
void heapify_down(int index) {
    int n = heap.size();
    while (true) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int smallest = index;
        if (left < n && heap[left] < heap[smallest]) {
            smallest = left;
        }
        if (right < n && heap[right] < heap[smallest]) {
            smallest = right;
        }
        if (smallest != index) {
            swap(heap[index], heap[smallest]);
            index = smallest;
        } else {
            break;
        }
    }
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        int op;
        cin >> op;
        if (op == 1) {
            int x;
            cin >> x;
            heap.push_back(x);
            heapify_up(heap.size() - 1);
        } else if (op == 2) {
            cout << heap[0] << endl;
        } else if (op == 3) {
            if (heap.empty()) continue; // 题目假设操作合法，无需处理空情况
            swap(heap[0], heap.back());
            heap.pop_back();
            if (!heap.empty()) {
                heapify_down(0);
            }
        }
    }
    return 0;
}