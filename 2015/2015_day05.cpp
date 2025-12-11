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
    file.open("datas/2015_day05_data");
    string line;

    long long correctCount = 0;

    while(getline(file, line)){
        int treatVowels = 0;
        bool treatDouble = false;
        bool treatBad = true;

        for(int i = 0; i < line.size()-1; ++i){
            if(line[i] == line[i+1]){
                treatDouble = true;
            }
            if((line[i] == 'a' && line[i+1] == 'b') ||
               (line[i] == 'c' && line[i+1] == 'd') ||
               (line[i] == 'p' && line[i+1] == 'q') ||
               (line[i] == 'x' && line[i+1] == 'y')){
                treatBad = false;
                break;
            }
            if(line[i] == 'a' || line[i] == 'e' || line[i] == 'i' ||
               line[i] == 'o' || line[i] == 'u'){
                ++treatVowels;
            }
        }
        if(line[line.size()-1] == 'a' || line[line.size()-1] == 'e' || line[line.size()-1] == 'i' ||
           line[line.size()-1] == 'o' || line[line.size()-1] == 'u'){
            ++treatVowels;
        }
        if(treatBad && treatDouble && treatVowels >= 3){
            correctCount++;
        }
    }

    cout << "Part 1: " << correctCount<< endl;
}

int main(){
    part1();
    return 0;
}