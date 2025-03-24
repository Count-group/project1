#include <iostream>

// 合并两个已排序的子数组
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // 创建临时数组
    int* L = new int[n1];
    int* R = new int[n2];

    // 复制数据到临时数组 L[] 和 R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // 归并临时数组到 arr[left..right]
    int i = 0;
    int j = 0;
    int k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // 复制 L[] 的剩余元素
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // 复制 R[] 的剩余元素
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    // 释放临时数组
    delete[] L;
    delete[] R;
}

// 归并排序函数
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        // 找到中间点
        int mid = left + (right - left) / 2;

        // 递归排序左半部分和右半部分
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // 合并已排序的两部分
        merge(arr, left, mid, right);
    }
}

int main() {
    int N;
    std::cin >> N;

    int* arr = new int[N];

    for (int i = 0; i < N; i++) {
        std::cin >> arr[i];
    }

    mergeSort(arr, 0, N - 1);

    for (int i = 0; i < N; i++) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << arr[i];
    }
    std::cout << std::endl;

    delete[] arr;

    return 0;
}    