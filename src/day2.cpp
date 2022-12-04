#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <array>
#include <vector>
#include <utility>

std::vector<std::string> parse_input(std::string filename) {
    std::ifstream input(filename);
    std::string input_line;
    std::vector<std::string> vec_input;
    while(std::getline(input, input_line)) {
        vec_input.push_back(input_line);
    }
    return vec_input;
}

enum class choice {
    rock, paper, scissors
};

std::ostream& operator<<(std::ostream& os, choice& chs) {
    switch(chs) {
        case choice::rock : os << "Rock"; break;
        case choice::paper : os << "Paper"; break;
        case choice::scissors : os << "Scissors"; break;
    }
    return os;
}

enum class result {
    win, draw, lose
};

std::ostream& operator<<(std::ostream& os, result& res) {
    switch(res) {
        case result::win : os << "Win"; break;
        case result::draw : os << "Draw"; break;
        case result::lose : os << "Lose"; break;
    }
    return os;
}

choice opponent(char c) {
    switch(c) {
        case 'A' : return choice::rock;
        case 'B' : return choice::paper;
        case 'C' : return choice::scissors;
    }
}

choice mine(char c) {
    switch(c) {
        case 'X' : return choice::rock;
        case 'Y' : return choice::paper;
        case 'Z' : return choice::scissors;
    }
}

int calculate_score_from_choice(choice m, choice o) {
    std::array<std::array<int, 3>, 3> score{{
        {3, 0, 6}, //rock
        {6, 3, 0}, //paper
        {0, 6, 3}  //scissors
    }};
    return score[static_cast<int>(m)][static_cast<int>(o)] + static_cast<int>(m) + 1;
}

void problem1() {
    auto v_input = parse_input("input_day2.txt");
    auto final_score{0};
    for (auto ip : v_input) {
        final_score += calculate_score_from_choice(mine(ip[2]), opponent(ip[0]));
    }
    std::cout << final_score << "\n";
}

result get_intended_result(char c) {
    switch(c) {
        case 'X' : return result::lose;
        case 'Y' : return result::draw;
        case 'Z' : return result::win;
    }
}

choice calculate_choice_from_result(choice opp, result r) {
    if (opp == choice::rock) {
        switch(r) {
            case result::lose : return choice::scissors;
            case result::draw : return choice::rock;
            case result::win : return choice::paper;
        }
    }
    if (opp == choice::paper) {
        switch(r) {
            case result::lose : return choice::rock;
            case result::draw : return choice::paper;
            case result::win : return choice::scissors;
        }
    }
    if (opp == choice::scissors) {
        switch(r) {
            case result::lose : return choice::paper;
            case result::draw : return choice::scissors;
            case result::win : return choice::rock;
        }
    }
}

void problem2() {
    auto v_input = parse_input("input_day2.txt");
    auto final_score{0};
    for (auto ip : v_input) {
        auto opp = opponent(ip[0]);
        auto me{calculate_choice_from_result(opp, get_intended_result(ip[2]))};
        final_score += calculate_score_from_choice(me, opp);
    }
    std::cout << final_score << "\n";
}

int main() {
    problem1();
    problem2();
}
