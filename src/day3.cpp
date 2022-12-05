#include <iostream>
#include <vector>


std::vector<std::string> parse_input(std::string filename) {
    std::ifstream input(filename);
    std::string input_line;
    std::vector<std::string> vec_input;
    while(std::getline(input, input_line)) {
        vec_input.push_back(input_line);
    }
    return vec_input;
}

void problem1() {
    auto input = parse_input("input_day3.txt");
}
