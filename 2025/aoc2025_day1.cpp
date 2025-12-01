#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int move_right(int number, int value){
    int result = number+value;
    while(result > 99){
        result = result-100;
    }
    return result;
}

int move_left(int number, int value){
    int result = number-value;
    while(result < 0){
        result = result+100;
    }
    return result;
}

void part1(){
    fstream file;
    file.open("datas/aoc2025_day1_data");
    string line;
    int password = 50;
    int count0 = 0;
    while(getline(file,line)){
        char letter = line[0];
        string numberC;
        
        numberC = line.substr(1,3);

        int number = stoi(numberC);
        switch(letter){
            case 'R':
                password = move_right(password,number);
                break;
            case 'L':
                password = move_left(password,number);
                break;
            default:
                cout << "Error in letter" << endl;
        }
        if (password == 0){
            count0 += 1;
        }
    }
    cout << "Part1: " << count0 << endl;
}

void part2(){
    fstream file;
    file.open("datas/aoc2025_day1_data");
    string line;
    int password = 50;
    int count0 = 0;
    while(getline(file,line)){
        char letter = line[0];
        string numberC;
        
        numberC = line.substr(1,3);

        int number = stoi(numberC);

        switch(letter){
            case 'R':
                for(int i = 0; i < number; i++){
                    password += 1;
                    if (password > 99){
                        password = password -100;
                    }
                    if(password == 0){count0 += 1;}
                }
                break;
            case 'L':
                for(int i = 0; i < number; i++){
                    password -= 1;
                    if(password < 0){
                        password = password+100;
                    }
                    if(password == 0){count0 += 1;}
                }
                break;
            default:
                cout << "Error in letter" << endl;
        }
        
    }
    cout << "Part2: " << count0 << endl;
}


int main(){
    part1();
    part2();
    return 0;
}