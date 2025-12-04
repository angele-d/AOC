#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int rollsAround(vector<string> input, int i, int j){
    int nbRollsAround = 0;
    if(i > 0 && j > 0 && input[i-1][j-1] == '@'){
        nbRollsAround += 1;
    }
    if(i > 0 && input[i-1][j] == '@'){
        nbRollsAround += 1;
    }
    if(i > 0 && j < input[0].size()-1 && input[i-1][j+1] == '@'){
        nbRollsAround += 1;
    }
    if(j > 0 && input[i][j-1] == '@'){
        nbRollsAround += 1;
    }
    if(j < input[0].size()-1 && input[i][j+1] == '@'){
        nbRollsAround += 1;
    }
    if(i < input.size()-1 && j > 0 && input[i+1][j-1] == '@'){
        nbRollsAround += 1;
    }
    if(i < input.size()-1 && input[i+1][j] == '@'){
        nbRollsAround += 1;
    }
    if(i < input.size()-1 && j < input[0].size()-1 && input[i+1][j+1] == '@'){
        nbRollsAround += 1;
    }
    return nbRollsAround;
} 

void part1(){
    fstream file;
    file.open("datas/2025_day4_data");
    if (!file.is_open()){
        cout << "Error opening file" << endl;
        return;
    }
    string line;
    vector<string> input;
    int rollsAccessed = 0;
    while(getline(file,line)){
        input.push_back(line);
    }
    for(int i = 0; i < input.size(); i++ ){
        for(int j = 0; j < input[0].size(); j++){
            if(input[i][j] == '@'){
                int rollsAroundCount = rollsAround(input,i,j);
                if (rollsAroundCount < 4){
                    rollsAccessed += 1;
                } 
            }
        }
    }
    cout << "Part 1: " << rollsAccessed << endl;
}

void part2(){
    fstream file;
    file.open("datas/2025_day4_data");
    if (!file.is_open()){
        cout << "Error opening file" << endl;
        return;
    }
    string line;
    vector<string> input;
    int rollsAccessed = 0;
    while(getline(file,line)){
        input.push_back(line);
    }
    bool newRollsAccessed = false;
    do{
        newRollsAccessed = false;
        for(int i = 0; i < input.size(); i++ ){
            for(int j = 0; j < input[0].size(); j++){
                if(input[i][j] == '@'){
                    int rollsAroundCount = rollsAround(input,i,j);
                    if (rollsAroundCount < 4){
                        rollsAccessed += 1;
                        input[i][j] = '.';
                        newRollsAccessed = true;
                    } 
                }
            }
        }
    }while(newRollsAccessed);

    for(int i = 0; i < input.size(); i++ ){
        for(int j = 0; j < input[0].size(); j++){
            if(input[i][j] == '@'){
                int rollsAroundCount = rollsAround(input,i,j);
                if (rollsAroundCount < 4){
                    rollsAccessed += 1;
                    input[i][j] = '.';
                } 
            }
        }
    }
    cout << "Part 2: " << rollsAccessed << endl;
}

int main(){
    part1();
    part2();
    return 0;
}