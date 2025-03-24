#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

// 插入排序处理小规模数据
void insertionSort(vector<int>& arr, int left, int right) {
    for (int i = left + 1; i <= right; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

// 改进的Hoare划分，三数取中+随机化
int optimizedPartition(vector<int>& arr, int left, int right) {
    // 三数取中法选择基准
    int mid = left + (right - left)/2;
    if (arr[mid] < arr[left]) swap(arr[left], arr[mid]);
    if (arr[right] < arr[left]) swap(arr[left], arr[right]);
    if (arr[right] < arr[mid]) swap(arr[mid], arr[right]);
    
    // 将中间值作为基准，并加入随机因素
    int randIdx = rand()%3;  // 随机选择三个候选值之一
    int pivot = (randIdx == 0) ? arr[left] : 
               (randIdx == 1) ? arr[mid] : arr[right];
    
    // Hoare划分算法
    int i = left - 1;
    int j = right + 1;
    while (true) {
        do { ++i; } while (arr[i] < pivot);
        do { --j; } while (arr[j] > pivot);
        if (i >= j) return j;
        swap(arr[i], arr[j]);
    }
}

// 优化的快速排序主体
void hybridSort(vector<int>& arr, int left, int right) {
    while (left < right) {
        // 小规模数据使用插入排序
        if (right - left < 32) {
            insertionSort(arr, left, right);
            return;
        }
        
        // 进行划分并递归处理
        int p = optimizedPartition(arr, left, right);
        
        // 优先处理较小分区以控制递归深度
        if (p - left < right - p) {
            hybridSort(arr, left, p);
            left = p + 1;
        } else {
            hybridSort(arr, p + 1, right);
            right = p;
        }
    }
}

int main() {
    srand(time(0));  // 初始化随机数生成
    int n;
    cin >> n;
    vector<int> arr(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    
    hybridSort(arr, 0, n-1);
    
    for (const auto& num : arr) {
        cout << num << " ";
    }
    
    return 0;
}