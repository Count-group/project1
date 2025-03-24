#include <iostream>
using namespace std;

const int MAX_SIZE = 1000005;  // 最大可能插入元素数量
int heap[MAX_SIZE];            // 下标从 1 开始使用
int heapSize = 0;

// 将 x 插入堆中，并调整堆结构
void push(int x) {
    heap[++heapSize] = x;
    int i = heapSize;
    // 上浮操作：当当前节点比父节点小时交换
    while (i > 1 && heap[i] < heap[i / 2]) {
        int temp = heap[i];
        heap[i] = heap[i / 2];
        heap[i / 2] = temp;
        i /= 2;
    }
}

// 删除堆顶元素，即删除最小值
void pop() {
    if (heapSize == 0) return;  // 安全判断
    // 将最后一个元素移到堆顶
    heap[1] = heap[heapSize--];
    int i = 1;
    // 下沉操作：与较小的子节点交换，保持小根堆性质
    while (2 * i <= heapSize) {
        int child = 2 * i;
        if (child + 1 <= heapSize && heap[child + 1] < heap[child]) {
            child++;
        }
        if (heap[i] <= heap[child]) break;
        int temp = heap[i];
        heap[i] = heap[child];
        heap[child] = temp;
        i = child;
    }
}

// 返回堆顶元素（最小值）
int top() {
    return heap[1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    while (n--) {
        int op;
        cin >> op;
        if (op == 1) {  // 插入操作
            int x;
            cin >> x;
            push(x);
        } else if (op == 2) {  // 输出最小值
            cout << top() << "\n";
        } else if (op == 3) {  // 删除最小值
            pop();
        }
    }
    return 0;
}
