#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

void part1(){
    fstream file;
    file.open("datas/2025_day5_data");
    string line;
    bool availablePart = false;
    long long freshcount = 0;
    vector<pair<unsigned long long, unsigned long long>> ranges;
    while(getline(file,line)){
        if(line == ""){
            availablePart = true;
        }
        else if(availablePart == false){
            stringstream ss(line);
            string range1S;
            getline(ss,range1S,'-');
            unsigned long long range1 = stoull(range1S);
            string range2S;
            getline(ss,range2S);
            unsigned long long range2 = stoull(range2S);
            ranges.push_back({range1,range2});
        }
        else{
            unsigned long long number = stoull(line);
            for(auto range : ranges){
                if(range.first <= number && range.second >= number){
                    freshcount++;
                    break;
                }
            }
        }
    }
    cout << "Part 1: " << freshcount << endl;
}

void part2(){
    fstream file;
    file.open("datas/2025_day5_data");
    string line;
    bool availablePart = false;
    long long freshcount = 0;
    vector<pair<unsigned long long, unsigned long long>> ranges;
    while(getline(file,line)){
        if(line == ""){
            availablePart = true;
            break;
        }
        else if(availablePart == false){
            stringstream ss(line);
            string range1S;
            getline(ss,range1S,'-');
            unsigned long long range1 = stoull(range1S);
            string range2S;
            getline(ss,range2S);
            unsigned long long range2 = stoull(range2S);
            ranges.push_back({range1,range2});
        }
    }
    sort(ranges.begin(),ranges.end());
    vector<pair<unsigned long long, unsigned long long>> valids;
    for(auto range : ranges){
        if(valids.empty() || valids.back().second < range.first - 1){
            valids.push_back(range);
        }
        else{
            auto& last = valids.back();
            last.second = max(last.second, range.second);
        }
    }
    for(auto range : valids){
        cout << range.first << "-" << range.second << endl;
        freshcount += (range.second - range.first + 1);
    }
    cout << "Part 2: " << freshcount << endl;
}

int main(){
    part1();
    part2();
    return 0;
}