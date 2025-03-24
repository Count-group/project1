#include <cstdio>
#include <utility>
using namespace std;

class MinHeap {
private:
    int *arr;      // 动态数组存储堆元素
    int capacity;  // 当前容量
    int size;      // 当前元素个数

    void expandCapacity() {
        // 扩展容量为原来的两倍
        capacity *= 2;
        int *newArr = new int[capacity];
        for (int i = 0; i < size; ++i) {
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
    }

public:
    MinHeap() : capacity(1), size(0) {
        arr = new int[capacity];
    }

    ~MinHeap() {
        delete[] arr;
    }

    void insert(int x) {
        if (size == capacity) {
            expandCapacity();
        }
        arr[size] = x;
        int i = size++;
        // 上浮操作，维护堆的性质
        while (i != 0) {
            int parent = (i - 1) / 2;
            if (arr[i] >= arr[parent]) {
                break;
            }
            swap(arr[i], arr[parent]);
            i = parent;
        }
    }

    void removeMin() {
        if (size == 0) return;
        arr[0] = arr[size - 1];
        size--;
        int i = 0;
        // 下沉操作，维护堆的性质
        while (true) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int smallest = i;
            if (left < size && arr[left] < arr[smallest]) {
                smallest = left;
            }
            if (right < size && arr[right] < arr[smallest]) {
                smallest = right;
            }
            if (smallest == i) break;
            swap(arr[i], arr[smallest]);
            i = smallest;
        }
    }

    int getMin() {
        return arr[0];
    }

    bool empty() {
        return size == 0;
    }
};

int main() {
    int n;
    scanf("%d", &n);
    MinHeap mh;
    while (n--) {
        int op;
        scanf("%d", &op);
        if (op == 1) {
            int x;
            scanf("%d", &x);
            mh.insert(x);
        } else if (op == 2) {
            printf("%d\n", mh.getMin());
        } else if (op == 3) {
            mh.removeMin();
        }
    }
    return 0;
}