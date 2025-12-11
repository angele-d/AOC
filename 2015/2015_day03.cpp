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

struct PairHash {
    size_t operator()(const pair<int,int>& p) const {
        return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
    }
};

void part1(){
    fstream file;
    file.open("datas/2015_day03_data");
    string line;
    getline(file, line);
    cout << line << endl;

    unordered_map<pair<int,int>,int,PairHash> locations;
    locations[{0,0}] = 1;
    pair<int,int> previousPos = {0,0};
    for(char c : line){
        cout << "Processing " << c << endl;
        pair<int,int> pos;
        if(c == '^'){
            pos = {previousPos.first - 1, previousPos.second};
        } else if(c == 'v'){
            pos = {previousPos.first + 1, previousPos.second};
        } else if(c == '>'){
            pos = {previousPos.first, previousPos.second + 1};
        } else if(c == '<'){
            pos = {previousPos.first, previousPos.second - 1};
        }
        if(locations.find(pos) != locations.end()){
            cout << "Add present at " << pos.first << "," << pos.second << endl;
            locations[pos]++;
        } else {
            cout << "First present at " << pos.first << "," << pos.second << endl;
            locations[pos] = 1;
        }
        previousPos = pos;
    }

    long long onePresentHouses = 0;
    for(const auto& loc : locations){
        if(loc.second >= 1){
            onePresentHouses++;
        }
    }

    cout << "Part 1: " << onePresentHouses << endl;
}

void part2(){
    fstream file;
    file.open("datas/2015_day03_data");
    string line;
    getline(file, line);
    cout << line << endl;

    unordered_map<pair<int,int>,int,PairHash> locations;
    locations[{0,0}] = 1;
    pair<int,int> previousPosRobot = {0,0};
    pair<int,int> previousPosSanta = {0,0};
    int turn = 0;
    for(char c : line){
        cout << "Processing " << c << " Robot" << turn << endl;
        pair<int,int> pos;
        switch (turn){
            case 0:
                if(c == '^'){
                    pos = {previousPosRobot.first - 1, previousPosRobot.second};
                } else if(c == 'v'){
                    pos = {previousPosRobot.first + 1, previousPosRobot.second};
                } else if(c == '>'){
                    pos = {previousPosRobot.first, previousPosRobot.second + 1};
                } else if(c == '<'){
                    pos = {previousPosRobot.first, previousPosRobot.second - 1};
                }
                break;
            case 1:
                if(c == '^'){
                    pos = {previousPosSanta.first - 1, previousPosSanta.second};
                } else if(c == 'v'){
                    pos = {previousPosSanta.first + 1, previousPosSanta.second};
                } else if(c == '>'){
                    pos = {previousPosSanta.first, previousPosSanta.second + 1};
                } else if(c == '<'){
                    pos = {previousPosSanta.first, previousPosSanta.second - 1};
                }
                break;
        }
        if(locations.find(pos) != locations.end()){
            cout << "Add present at " << pos.first << "," << pos.second << endl;
            locations[pos]++;
        } else {
            cout << "First present at " << pos.first << "," << pos.second << endl;
            locations[pos] = 1;
        }
        if(turn == 0){
            previousPosRobot = pos;
            turn = 1;
        } else {
            previousPosSanta = pos;
            turn = 0;
        }
    }

    long long onePresentHouses = 0;
    for(const auto& loc : locations){
        if(loc.second >= 1){
            onePresentHouses++;
        }
    }

    cout << "Part 2: " << onePresentHouses << endl;
}

int main(){
    part1();
    part2();
    return 0;
}