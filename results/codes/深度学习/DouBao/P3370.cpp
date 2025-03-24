#include <iostream>
#include <unordered_set>
#include <string>

int main() {
    int N;
    std::cin >> N;
    // 忽略掉第一行之后的换行符
    std::cin.ignore();

    std::unordered_set<std::string> distinctStrings;

    for (int i = 0; i < N; ++i) {
        std::string str;
        std::cin>>str;
        distinctStrings.insert(str);
    }

    std::cout << distinctStrings.size() << std::endl;

    return 0;
}    