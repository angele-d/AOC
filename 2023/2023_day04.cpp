#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>


void part1(){
    std::ifstream file("datas/aoc2023_day4_data");
    if(!file){
        std::cerr << "Error opening file!" << std::endl;
        return ;
    }

    std::string line;
    int totalWinners = 0;
    while(getline(file,line)){ // Get a line from the file
        line = line.substr(9); // Skip "Card x :"
        std::stringstream ss(line);
        std::string temp;
        std::vector<std::string> sections;
        while(getline(ss,temp,'|')){ // Split the line by '|'
            sections.push_back(temp);
        }
        std::vector<int> winners;
        std::stringstream ss0(sections[0]);
        while(getline(ss0,temp,' ')){ // Split the first section by ' '
            if(temp == "") continue; // Skip empty strings
            winners.push_back(std::stoi(temp));
        }
        std::vector<int> numbers;
        std::stringstream ss1(sections[1]);
        while(getline(ss1,temp,' ')){ // Split the second section by ' '
            if(temp == "") continue; // Skip empty strings
            numbers.push_back(std::stoi(temp));
        }
        int nbwinners = 0;
        for(int number : numbers){
            for(int winner : winners){
                if(number == winner){
                    nbwinners++;
                }
            }
        }
        totalWinners += std::pow(2,nbwinners-1);
    }
    std::cout << "Total Winners Part 1: " << totalWinners << std::endl;
    file.close();
}

void part2(){
    std::ifstream file0("datas/aoc2023_day4_data");
    if(!file0){
        std::cerr << "Error opening file!" << std::endl;
        return ;
    }


    int nbLignes = std::count(std::istreambuf_iterator<char>(file0), std::istreambuf_iterator<char>(), '\n');
    int copies[nbLignes];
    for(int i = 0; i < nbLignes; i++){copies[i]=1;}

    int cardnb = 0;

    file0.close();
    std::ifstream file("datas/aoc2023_day4_data");
    if(!file){
        std::cerr << "Error opening file!" << std::endl;
        return ;
    }
    std::string line;

    while(getline(file,line)){ // Get a line from the file
        line = line.substr(9); // Skip "Card x :"
        std::stringstream ss(line);
        std::string temp;
        std::vector<std::string> sections;
        while(getline(ss,temp,'|')){ // Split the line by '|'
            sections.push_back(temp);
        }
        std::vector<int> winners;
        std::stringstream ss0(sections[0]);
        while(getline(ss0,temp,' ')){ // Split the first section by ' '
            if(temp == "") continue; // Skip empty strings
            winners.push_back(std::stoi(temp));
        }
        std::vector<int> numbers;
        std::stringstream ss1(sections[1]);
        while(getline(ss1,temp,' ')){ // Split the second section by ' '
            if(temp == "") continue; // Skip empty strings
            numbers.push_back(std::stoi(temp));
        }
        int nbwinners = 0;
        for(int number : numbers){
            for(int winner : winners){
                if(number == winner){
                    nbwinners++;
                }
            }
        }
        // Register the copies to make
        for(int i = 0; i < nbwinners; i++){
            copies[cardnb+i+1] = copies[cardnb+i+1] + copies[cardnb];
        }
        cardnb++;
    }
    int scratchcards = 0;
    for(int elt : copies){
        scratchcards += elt;
    }
    std::cout << "Result Part 2: " << scratchcards << std::endl;
    file.close();
}

int main(){
    part1();
    part2();
    return 0;
}