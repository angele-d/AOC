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
    const long long objectiveGift = 29000000;

    const int limit = static_cast<int>(objectiveGift / 10);

    vector<long long> presentsPerHouse(limit + 1, 0);

    for(int elf = 1; elf <= limit; ++elf){
        for(int house = elf; house <= limit; house += elf){
            presentsPerHouse[house] += static_cast<long long>(elf) * 10;
        }
    }

    for(int house = 1; house <= limit; ++house){
        if(presentsPerHouse[house] >= objectiveGift){
            cout << "Part 1: " << house << endl;
            return;
        }
    }

    cout << "Part 1: not found within bound" << endl;
}

void part2(){
    const long long objectiveGift = 29000000;

    const int limit = static_cast<int>(objectiveGift / 11);
    
    vector<long long> presentsPerHouse(limit + 1, 0);

    for(int elf = 1; elf <= limit; ++elf){
        for(int house = elf; house <= limit && house <= elf * 50; house += elf){
            presentsPerHouse[house] += static_cast<long long>(elf) * 11;
        }
    }

    for(int house = 1; house <= limit; ++house){
        if(presentsPerHouse[house] >= objectiveGift){
            cout << "Part 1: " << house << endl;
            return;
        }
    }

    cout << "Part 2: not found within bound" << endl;
}

int main(){
    part1();
    part2();
    return 0;
}