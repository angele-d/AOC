#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void part1(){
    fstream file;
    file.open("datas/2025_day03_data");
    string line;
    int totalJoltage = 0;
    while(getline(file,line)){
        char firstNumber = '9';
        size_t pos = line.find(firstNumber);
        while(pos == string::npos || pos >= line.length()-1){
            firstNumber -= 1;
            pos = line.find(firstNumber);
        }
        char secondNumber = '9';
        size_t pos2 = line.find(secondNumber,pos+1);
        while(pos2 == string::npos || pos2 >= line.length()){
            secondNumber -= 1;
            pos2 = line.find(secondNumber,pos+1);
        }
        int firstNumberI = firstNumber - '0';
        int secondNumberI = secondNumber - '0';
        int voltage = firstNumberI*10+secondNumberI;
        totalJoltage += voltage;
    }
    cout << "Part 1: " << totalJoltage << endl;
}

pair<char,size_t> nextPos(string line, int start, int digitRemaining){
    char highestNumber = '9';
    size_t pos = line.find(highestNumber,start);
    while(pos == string::npos || line.length()-pos < digitRemaining){
        highestNumber -= 1;
        pos = line.find(highestNumber,start);
    }
    return {highestNumber,pos};
} 

void part2(){
    fstream file;
    file.open("datas/2025_day03_data");
    string line;
    unsigned long long totalJoltage = 0;
    while(getline(file,line)){
        unsigned long long voltage = 0;
        int digitRemaining = 12;
        size_t pos = 0;
        while(digitRemaining > 0 && pos < line.length()){
            auto [number,start] = nextPos(line,pos,digitRemaining);
            int numberI = number - '0';
            voltage = voltage*10+numberI;
            pos = start + 1;
            digitRemaining -= 1;
        }
        totalJoltage += voltage;
    }
    cout << "Part 2: " << totalJoltage << endl;
}

int main(){
    part1();
    part2();
    return 0;
}