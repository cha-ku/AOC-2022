#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <numeric>

void problem1() {
    std::ifstream input("input_day1.txt");
    std::string input_line;
    auto global_max = 0;
    auto curr_sum = 0;
    while(std::getline(input, input_line)) {
        if (!input_line.empty())
            curr_sum += std::stoi(input_line);
        else {
            if (curr_sum > global_max)
                global_max = curr_sum;
            curr_sum = 0;
        }
    }
    std::cout << global_max << std::endl;
}

void problem2() {
    std::ifstream input("input_day1.txt");
    std::string input_line;
    std::vector<uint64_t> group_total;
    auto curr_sum = 0;
    while(std::getline(input, input_line)) {
        if (!input_line.empty())
            curr_sum += std::stoi(input_line);
        else {
            group_total.push_back(curr_sum);
            curr_sum = 0;
        }
    }
    std::partial_sort(group_total.begin(), group_total.begin() + 3, group_total.end(), std::greater<int>());
    std::vector<uint64_t> subvec(group_total.begin(), group_total.begin() + 3);
    std::cout << std::accumulate(subvec.begin(), subvec.end(), 0) << "\n";
}

int main() {
    problem1();
    problem2();
}
