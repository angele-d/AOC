#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

unsigned long long find_sequence_twice(unsigned long min, unsigned long long max){
    unsigned long long doubles = 0;
    for(unsigned long long i = min; i <= max; i++){
        // Check if the sequence appears twice
        string numberS = to_string(i);
        bool isDouble = true;
        if(numberS.length() % 2 == 0){
            int middle = numberS.length()/2;
            for(int j = 0; j < middle; j++){
                if(numberS[j] == numberS[j+middle]){
                    continue;
                } else {
                    isDouble = false;
                    break;
                }
            }
        }
        else{
            isDouble = false;
        }
        
        if(isDouble){
            doubles = doubles + i;
        }
    }
    return doubles;
}

void part1(){    
    unsigned long long totalDoubles = 0;
    fstream file;
    file.open("datas/2025_day2_data");
    string line;
    getline(file,line);
    stringstream ss(line);
    string temp;
    vector<string> ranges;
    while(getline(ss,temp,',')){
        ranges.push_back(temp);
    }
    for(string range : ranges){
        stringstream ss0(range);
        string minS,maxS;
        getline(ss0,minS,'-');
        getline(ss0,maxS);
        unsigned long long min = stoull(minS);
        unsigned long long max = stoull(maxS);
        unsigned long long doubles = find_sequence_twice(min,max);
        totalDoubles = totalDoubles + doubles;
    }
    cout << "Part 1: " << totalDoubles << endl;
}

unsigned long long find_sequence_invalids(unsigned long long min, unsigned long long max){
    unsigned long long invalids = 0;
    for(unsigned long long i = min; i <= max; i++){
        string numberS = to_string(i);
        bool isInvalid = true;
        int indice = 1;
        size_t pos = numberS.find(numberS[0],1);
        while(indice < numberS.length()){
            while(pos != string::npos){
                pos = numberS.find(numberS[indice],indice+1);
                indice ++;
            }
            if(numberS[indice] = numberS[0]){
                continue;
            }
            else{
                isInvalid = false;
            }
        }
        

        if (isInvalid){
            invalids = invalids + i;
            cout << "invalid sequence: " << i << endl;
        }
    }
    return invalids;
}

void part2(){
    unsigned long long totalInvalids = 0;
    fstream file;
    file.open("datas/2025_day2_exemple");
    string line;
    getline(file,line);
    stringstream ss(line);
    string temp;
    vector<string> ranges;
    while(getline(ss,temp,',')){
        ranges.push_back(temp);
    }
    for(string range : ranges){
        stringstream ss0(range);
        string minS,maxS;
        getline(ss0,minS,'-');
        getline(ss0,maxS);
        cout << minS << " " << maxS << endl;
        unsigned long long min = stoull(minS);
        unsigned long long max = stoull(maxS);
        cout << "Range: " << min << " to " << max << endl;
        unsigned long long doubles = find_sequence_twice(min,max);
        totalInvalids = totalInvalids + doubles;
    }
    cout << "Part 2: " << totalInvalids << endl;
}

int main(){
    part1();
    part2();
    return 0;
}