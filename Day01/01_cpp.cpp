#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

void read_and_sort_input(const std::string &fname, std::vector<int> &list1, std::vector<int> &list2) {
    std::ifstream f(fname);

    if (f.is_open()) {
        int x, y;
        while (f >> x >> y) {
            list1.push_back(x);
            list2.push_back(y);
        }
        f.close();
        std::cout << "File opened successfully!\n";
    } else {
        std::cerr << "Unable to open file!\n";
        return;
    }

    std::sort(list1.begin(), list1.end());
    std::sort(list2.begin(), list2.end());
}

void day01_part1(const std::vector<int> &list1, const std::vector<int> &list2) {
    int sum = 0;
    for (size_t i = 0; i < list1.size(); i++) {
        sum += std::abs(list1[i] - list2[i]);
    }
    std::cout << "Part 1: " << sum << "\n";
}

void day01_part2(const std::vector<int> &list1, const std::vector<int> &list2) {
    int answer = 0;
    for (int val1 : list1) {
        for (int val2 : list2) {
            if (val2 == val1) {
                answer += val1;
            }
        }
    }
    std::cout << "Part 2: " << answer << "\n";
}

int main() {
    std::vector<int> list1;
    std::vector<int> list2;

    read_and_sort_input("Day01/01-1_input.txt", list1, list2);

    if (list1.empty() || list2.empty()) {
        std::cerr << "Error: Empty input lists. Exiting program.\n";
        return 1;
    }

    day01_part1(list1, list2);
    day01_part2(list1, list2);

    return 0;
}
