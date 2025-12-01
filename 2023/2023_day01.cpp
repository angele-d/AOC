#include <iostream>
#include <fstream> // To include file handling

void part1(){
    std::ifstream file("datas/aoc2023_day1_data");
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }
    std::string line;
    
    int calibration = 0;

    while(getline(file,line)){
        int firstnumber = -1;
        int lastnumber = -1;
        for (char c : line){
            if (c >= '0' && c <= '9'){ // Check if it's a number
                if (firstnumber == -1) {
                    firstnumber = c - '0'; // Convert char to int
                }
                lastnumber = c - '0';
            }
        }
        int newnumber = firstnumber*10 + lastnumber;
        calibration += newnumber;
    }

    std::cout << "Calibration part 1: " << calibration << std::endl;
}

int searchNumber(std::string line) {
    int firstnumber = -1;
    int lastnumber = -1;
    for (int i = 0; i < line.length(); i++) {
        char c = line[i];
        if (c >= '0' && c <= '9'){
            if (firstnumber == -1) {
                firstnumber = c - '0';
            }
            lastnumber = c - '0';
        }
        else{
            int possibleNumber = -1;
            switch (c) {
                case 'o':
                    if (i + 2 < line.length() && line[i + 1] == 'n' && line[i + 2] == 'e') {
                        possibleNumber = 1;
                    }
                    break;
                case 't':
                    if (i + 2 < line.length() && line[i + 1] == 'w' && line[i + 2] == 'o') {
                        possibleNumber = 2;
                    }
                    else if (i + 4 < line.length() && line[i + 1] == 'h' && line[i + 2] == 'r' && line[i + 3] == 'e' && line[i + 4] == 'e') {
                        possibleNumber = 3;
                    }
                    break;
                case 'f':
                    if (i + 3 < line.length() && line[i + 1] == 'o' && line[i + 2] == 'u' && line[i + 3] == 'r') {
                        possibleNumber = 4;
                    }
                    else if (i + 3 < line.length() && line[i + 1] == 'i' && line[i + 2] == 'v' && line[i + 3] == 'e') {
                        possibleNumber = 5;
                    }
                    break;
                case 's':
                    if (i + 2 < line.length() && line[i + 1] == 'i' && line[i + 2] == 'x') {
                        possibleNumber = 6;
                    }
                    else if (i + 4 < line.length() && line[i + 1] == 'e' && line[i + 2] == 'v' && line[i + 3] == 'e' && line[i + 4] == 'n') {
                        possibleNumber = 7;
                    }
                    break;
                case 'e':
                    if (i + 4 < line.length() && line[i + 1] == 'i' && line[i + 2] == 'g' && line[i + 3] == 'h' && line[i + 4] == 't') {
                        possibleNumber = 8;
                    }
                    break;
                case 'n':
                    if (i + 3 < line.length() && line[i + 1] == 'i' && line[i + 2] == 'n' && line[i + 3] == 'e') {
                        possibleNumber = 9;
                    }
                    break;
            }
            if (possibleNumber != -1) {
                if (firstnumber == -1) {
                    firstnumber = possibleNumber;
                }
                lastnumber = possibleNumber;
            }
        }
    }
    return firstnumber * 10 + lastnumber;
}

void part2(){
    std::ifstream file("datas/aoc2023_day1_data");
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }
    std::string line;
    
    int calibration = 0;

    while(getline(file,line)){
        int newnumber = searchNumber(line);
        std::cout << newnumber << std::endl;
        calibration += newnumber;
    }

    std::cout << "Calibration Part 2: " << calibration << std::endl;
}

int main(){
    part1();
    part2();
    return 0;
}