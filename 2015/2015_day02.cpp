#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <queue>
#include <algorithm>
#include <unordered_map>
#include <map>

using namespace std;

void part1(){
    fstream file;
    file.open("datas/2015_day02_data");
    string line;
    unsigned long long totalSquareFeet = 0;

    while(getline(file, line)){
        stringstream ss(line);
        string number;
        vector<int> dimensions;
        while(getline(ss, number, 'x')){
            dimensions.push_back(stoi(number));
        }
        unsigned long long squareFeet = 0;
        squareFeet += 2 * dimensions[0] * dimensions[1];
        squareFeet += 2 * dimensions[0] * dimensions[2];
        squareFeet += 2 * dimensions[1] * dimensions[2];
        squareFeet += min({dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]});
        totalSquareFeet += squareFeet;
    }

    cout << "Part 1: " << totalSquareFeet<< endl;
}

void part2(){
    fstream file;
    file.open("datas/2015_day02_data");
    string line;
    unsigned long long totalSquareFeet = 0;

    while(getline(file, line)){
        stringstream ss(line);
        string number;
        vector<int> dimensions;
        while(getline(ss, number, 'x')){
            dimensions.push_back(stoi(number));
        }
        int lowestPerimeter = min({2 * (dimensions[0] + dimensions[1]), 2 * (dimensions[0] + dimensions[2]), 2 * (dimensions[1] + dimensions[2])});
        unsigned long long bow = dimensions[0] * dimensions[1] * dimensions[2];
        totalSquareFeet += lowestPerimeter + bow;
    }

    cout << "Part 2: " << totalSquareFeet<< endl;
}

int main(){
    part1();
    part2();
    return 0;
}