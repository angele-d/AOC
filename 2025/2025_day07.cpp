#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>

using namespace  std;

int findS(vector<string> lines){
    for(int j = 0; j < lines[0].size(); j++){
        if(lines[0][j] == 'S'){
            return j;
        }
    }
    return -1;
}

void part1(){
    fstream file;
    file.open("datas/2025_day07_data");
    string line;
    vector<string> lines;
    while(getline(file,line)){
        lines.push_back(line);
    }

    int splitNumber = 0;

    int S = findS(lines);
    queue<pair<int,int>> beamsPos;
    int i = 0;
    beamsPos.push({i,S});
    
    while(true){
        int i = beamsPos.front().first;
        int j = beamsPos.front().second;
        beamsPos.pop();
        if(i+1 >= lines.size()) break;
        if(lines[i+1][j] == '^' && (lines[i+1][j-1] != '|' || lines[i+1][j+1] != '|')){
            splitNumber++;
            if(j-1 >= 0 && lines[i+1][j-1] != '|'){
                lines[i+1][j-1] = '|';
                beamsPos.push({i+1,j-1});
            }
            if(j+1 < lines[0].size() && lines[i+1][j+1] != '|'){
                lines[i+1][j+1] = '|';
                beamsPos.push({i+1,j+1});
            }
        }
        else{
            lines[i+1][j] = '|';
            beamsPos.push({i+1,j});
        }
    }

    cout << "Part 1 : " << splitNumber << endl;
}

unsigned long long goDown(vector<string> lines, int i, int j, vector<vector<unsigned long long>> &memo){
    if(i+1 >= lines.size()) return 1;
    if(memo[i][j] != -1) return memo[i][j];

    unsigned long long count = 0;
    if(lines[i+1][j] == '^'){
        if(j-1 >= 0){
            count += goDown(lines,i+1,j-1,memo);
        }
        if(j+1 < lines[0].size()){
            count += goDown(lines,i+1,j+1,memo);
        }
    }
    else{
        count = goDown(lines,i+1,j,memo);
    }
    memo[i][j] = count;
    return count;
}


void part2(){
    fstream file;
    file.open("datas/2025_day07_data");
    string line;
    vector<string> lines;
    while(getline(file,line)){
        lines.push_back(line);
    }

    unsigned long long timelineNumber = 0;

    int S = findS(lines);
    
    vector<vector<unsigned long long>> memo(lines.size(), vector<unsigned long long>(lines[0].size(), -1));
    timelineNumber = goDown(lines,0,S,memo);

    cout << "Part 2 : " << timelineNumber << endl;
}

int main(){
    part1();
    part2();
    return 0;
}