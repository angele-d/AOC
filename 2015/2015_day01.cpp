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
    file.open("datas/2015_day01_data");
    string line;
    getline(file, line);

    long long parentheses = 0;
    for(char c : line){
        if(c == '('){
            parentheses++;
        } else if(c == ')'){
            parentheses--;
        }
    }

    cout << "Part 1: " << parentheses << endl;
}

void part2(){
    fstream file;
    file.open("datas/2015_day01_data");
    string line;
    getline(file, line);

    long long parentheses = 0;
    for(size_t i = 0; i < line.size(); i++){
        if(line[i] == '('){
            parentheses++;
        } else if(line[i] == ')'){
            parentheses--;
        }
        if(parentheses < 0){
            cout << "Part 2: " << i + 1 << endl;
            return;
        }
    }
}

int main(){
    part1();
    part2();
    return 0;
}