#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    
    // 构造图及统计每个顶点的入度和出度
    vector<vector<int>> graph(n + 1);
    vector<int> outdeg(n + 1, 0), indeg(n + 1, 0);
    for (int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        outdeg[u]++;
        indeg[v]++;
    }
    
    // 对每个顶点的出边按升序排序
    for (int i = 1; i <= n; i++){
        sort(graph[i].begin(), graph[i].end());
    }
    
    // 判断欧拉路径存在性，确定起点
    int startCount = 0, endCount = 0;
    int startVertex = -1;
    for (int i = 1; i <= n; i++){
        if(outdeg[i] - indeg[i] == 1){
            startCount++;
            startVertex = i;  // 候选起点
        }
        else if(indeg[i] - outdeg[i] == 1){
            endCount++;
        }
        else if(outdeg[i] != indeg[i]){
            cout << "No" << "\n";
            return 0;
        }
    }
    
    // 如果为欧拉环路，则选择出边非空的最小顶点作为起点
    if(startCount == 0 && endCount == 0){
        for(int i = 1; i <= n; i++){
            if(outdeg[i] > 0){
                startVertex = i;
                break;
            }
        }
        // 若图中没有任何边（m == 0），此时可输出任一顶点（例如1）
        if(startVertex == -1) startVertex = 1;
    }
    // 如果不满足欧拉路径的度数条件
    else if(!(startCount == 1 && endCount == 1)){
        cout << "No" << "\n";
        return 0;
    }
    
    // Hierholzer 算法求欧拉路径（非递归实现）
    vector<int> result;          // 存放最终的路径
    vector<int> idx(n + 1, 0);     // 对每个顶点，记录当前遍历到哪条边
    vector<int> stack;
    stack.push_back(startVertex);
    
    while(!stack.empty()){
        int u = stack.back();
        // 若当前顶点还有未用的边，则继续沿最小边走
        if(idx[u] < graph[u].size()){
            int v = graph[u][idx[u]];
            idx[u]++;
            stack.push_back(v);
        } else {
            // 无可走边，则回溯，记录顶点
            result.push_back(u);
            stack.pop_back();
        }
    }
    
    // 检查是否所有边都使用完
    if(result.size() != m + 1){
        cout << "No" << "\n";
        return 0;
    }
    
    // 因为得到的 result 序列是逆序，所以需要反转
    reverse(result.begin(), result.end());
    for (int i = 0; i < result.size(); i++){
        cout << result[i] << (i + 1 == result.size() ? "\n" : " ");
    }
    
    return 0;
}
