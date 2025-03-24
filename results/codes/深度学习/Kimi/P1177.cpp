#include <iostream>
using namespace std;

void merge(int arr[], int left, int mid, int right, int temp[]) {
    int i = left;   // 左半部分的起始索引
    int j = mid + 1;// 右半部分的起始索引
    int k = 0;      // 临时数组的索引

    // 合并两个有序数组
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }

    // 将左半部分剩余的元素拷贝到临时数组
    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    // 将右半部分剩余的元素拷贝到临时数组
    while (j <= right) {
        temp[k++] = arr[j++];
    }

    // 将临时数组中的元素拷贝回原数组
    for (i = left, k = 0; i <= right; ++i, ++k) {
        arr[i] = temp[k];
    }
}

void mergeSort(int arr[], int left, int right, int temp[]) {
    if (left >= right) {
        return;
    }

    int mid = left + (right - left) / 2; // 防止溢出

    // 递归地对左右两部分进行归并排序
    mergeSort(arr, left, mid, temp);
    mergeSort(arr, mid + 1, right, temp);

    // 合并两个有序子数组
    merge(arr, left, mid, right, temp);
}

int main() {
    int n;
    cin >> n;

    int* arr = new int[n];    // 动态分配原数组
    int* temp = new int[n];   // 动态分配临时数组，用于归并排序

    // 读取输入的N个数
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    // 使用归并排序算法进行排序
    mergeSort(arr, 0, n - 1, temp);

    // 输出排序后的结果
    for (int i = 0; i < n; ++i) {
        if (i > 0) {
            cout << " ";
        }
        cout << arr[i];
    }
    cout << endl;

    // 释放动态分配的内存
    delete[] arr;
    delete[] temp;

    return 0;
}