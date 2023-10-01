#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // ソートしたい要素が格納されたベクターを作成
    std::vector<int> numbers;
    numbers.push_back(5);
    numbers.push_back(2);
    numbers.push_back(9);
    numbers.push_back(1);
    numbers.push_back(5);
    numbers.push_back(6);

    // ベクター内の要素を昇順にソート
    std::sort(numbers.begin(), numbers.end());

    // ソート後の結果を表示
    for (int num : numbers) {
        std::cout << num << " ";
    }

    return 0;
}