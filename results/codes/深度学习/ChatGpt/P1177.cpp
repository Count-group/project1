#include <cstdio>

// 调整堆，使以 i 为根的子树满足最大堆性质
void heapify(int arr[], int n, int i) {
    int largest = i;            // 当前根节点
    int left = 2 * i + 1;         // 左子节点索引
    int right = 2 * i + 2;        // 右子节点索引

    // 找出当前根节点与左右子节点中值最大的节点
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }
    // 如果最大的节点不是根节点，则交换，并递归调整子树
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

// 堆排序函数
void heapSort(int arr[], int n) {
    // 构建初始最大堆
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    // 依次取出堆顶元素，将其放到数组末尾，并调整剩余部分为最大堆
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int *arr = new int[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    heapSort(arr, n);
    
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i != n - 1)
            printf(" ");
    }
    printf("\n");
    
    delete[] arr;
    return 0;
}
