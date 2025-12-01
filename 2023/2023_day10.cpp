#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <array>
#include <queue>

std::vector<std::pair<int,int>> coords;

std::pair<int,int> find_S(std::vector<std::string> tab){
    for (int i = 0 ; i < tab.size(); i++){
        for (int j = 0; j < tab[0].size(); j++){
            if(tab[i][j] == 'S'){
                return {i,j};
            }
        }
    }
    return {-1,-1};
}

std::array<int,4> connected_to_S(std::vector<std::string> tab, int iS, int jS){
    std::array<int, 4> tup = {-1,-1,-1,-1};
    int nbligne = tab.size();
    int nbcol = tab[0].size();

    if(iS-1 >= 0 && (tab[iS-1][jS] == '7' || tab[iS-1][jS] == 'F' || tab[iS-1][jS] == '|')){
        if(tup[0] == -1){tup[0] = iS-1; tup[1] = jS;}
    }
    if(iS+1 < nbligne && (tab[iS+1][jS] == 'J' || tab[iS+1][jS] == 'L' || tab[iS+1][jS] == '|')){
        if(tup[0] == -1){tup[0] = iS+1; tup[1] = jS;}
        else if(tup[2] == -1){tup[2] = iS+1; tup[3] = jS;}
    }
    if(jS-1 >= 0 && (tab[iS][jS-1] == 'F' || tab[iS][jS-1] == 'L' || tab[iS][jS-1] == '-')){
        if(tup[0] == -1){tup[0] = iS; tup[1] = jS-1;}
        else if(tup[2] == -1){tup[2] = iS; tup[3] = jS-1;}
    }
    if(jS+1 < nbcol && (tab[iS][jS+1] == 'J' || tab[iS][jS+1] == '7' || tab[iS][jS+1] == '-')){
        if(tup[0] == -1){tup[0] = iS; tup[1] = jS+1;}
        else if(tup[2] == -1){tup[2] = iS; tup[3] = jS+1;}
    }
    return tup;
}

char modifS(int iS,int jS, int i1, int j1, int i2, int j2, std::vector<std::string> tab){

    bool north = false, south = false, east = false, west = false;

    if (i1 == iS-1 && j1 == jS) north = true;
    else if (i1 == iS+1 && j1 == jS) south = true;
    else if (i1 == iS && j1 == jS-1) west = true;
    else if (i1 == iS && j1 == jS+1) east = true;

    if (i2 == iS-1 && j2 == jS) north = true;
    else if (i2 == iS+1 && j2 == jS) south = true;
    else if (i2 == iS && j2 == jS-1) west = true;
    else if (i2 == iS && j2 == jS+1) east = true;

    if (north && south) return '|';
    else if (east && west) return '-';
    else if (north && east) return 'L';
    else if (north && west) return 'J';
    else if (south && east) return 'F';
    else if (south && west) return '7';
    return 'S';
}

std::vector<std::vector<int>> calc_distance_max(std::vector<std::string> tab){
    int nbligne = tab.size();
    int nbcol = tab[0].size();    

    auto [iS,jS] = find_S(tab);
    auto [i1,j1,i2,j2] = connected_to_S(tab,iS,jS);

    std::vector<std::vector<int>> distance;
    
    for (int i = 0; i < nbligne; i++){
        std::vector<int> row;
        for(int j = 0; j < nbcol; j++){
            row.push_back(-1);
        }
        distance.push_back(row);
    }
    distance[iS][jS] = 0;
    distance[i1][j1] = 1;
    distance[i2][j2] = 1;


    std::queue<std::pair<int,int>> file;
    file.push({i1,j1});
    file.push({i2,j2});


    while(!file.empty()){
        auto [i,j] = file.front();
        file.pop();
        switch(tab[i][j]){
            case 'F':
                if(i+1 < nbligne && distance[i+1][j] == -1){ // it's this one
                    distance[i+1][j] = distance[i][j] + 1;
                    coords.push_back({i+1,j});
                    file.push({i+1,j});
                }
                else if (j+1 < nbcol && distance[i][j+1] == -1){
                    distance[i][j+1] = distance[i][j] + 1;
                    coords.push_back({i,j+1});
                    file.push({i,j+1});
                }
                break;
            case '|':
                if (i-1 >=0 && distance[i-1][j]==-1) {
                    distance[i-1][j] = distance[i][j]+1;
                    coords.push_back({i-1,j});
                    file.push({i-1,j});
                }
                else if (i+1 < nbligne && distance[i+1][j]==-1) {
                    distance[i+1][j] = distance[i][j]+1;
                    coords.push_back({i+1,j});
                    file.push({i+1,j});
                }
                break;
            case '-':
                if (j-1 >=0 && distance[i][j-1]==-1) {
                    distance[i][j-1] = distance[i][j]+1;
                    coords.push_back({i,j-1});
                    file.push({i,j-1});
                }
                else if (j+1 < nbcol && distance[i][j+1]==-1) {
                    distance[i][j+1] = distance[i][j]+1;
                    coords.push_back({i,j+1});
                    file.push({i,j+1});
                }
                break;
            case 'J':
                if (i-1 >=0 && distance[i-1][j]==-1) {
                    distance[i-1][j] = distance[i][j]+1;
                    coords.push_back({i-1,j});
                    file.push({i-1,j});
                }
                else if (j-1 >=0 && distance[i][j-1]==-1) {
                    distance[i][j-1] = distance[i][j]+1;
                    coords.push_back({i,j-1});
                    file.push({i,j-1});
                } 
                break;
            case 'L':
                if (i-1 >=0 && distance[i-1][j]==-1) {
                    distance[i-1][j] = distance[i][j]+1;
                    coords.push_back({i-1,j});
                    file.push({i-1,j});
                }
                else if (j+1 < nbcol && distance[i][j+1]==-1) {
                    distance[i][j+1] = distance[i][j]+1;
                    coords.push_back({i,j+1});
                    file.push({i,j+1});
                }
                break;
            case '7':
                if (i+1 < nbligne && distance[i+1][j]==-1) {
                    distance[i+1][j] = distance[i][j]+1;
                    coords.push_back({i+1,j});
                    file.push({i+1,j});
                }
                else if (j-1 >=0 && distance[i][j-1]==-1) {
                    distance[i][j-1] = distance[i][j]+1;
                    coords.push_back({i,j-1});
                    file.push({i,j-1});
                }
                break;
        }   
    }
    return distance;
}

void part1(){
    std::ifstream file("datas/aoc2023_day10_data");
    if (!file){
        std::cerr << "Error opening file!" << std::endl;
        return ;
    }
    std::string line;
    std::vector<std::string> tab;
    while(getline(file,line)){
        tab.push_back(line);
    }

    std::vector<std::vector<int>> distance = calc_distance_max(tab);

    int max_dist = 0;
    for(int i = 0; i < tab.size(); i++){
        for(int j = 0; j < tab[0].size(); j++){
            max_dist = std::max(max_dist,distance[i][j]);
        }
    }

    std::cout << "Part1: " << max_dist << std::endl;
}

void part2(){
    std::ifstream file("datas/aoc2023_day10_data");
    if (!file){
        std::cerr << "Error opening file!" << std::endl;
        return ;
    }
    std::string line;
    std::vector<std::string> tab;
    while(getline(file,line)){
        tab.push_back(line);
    }

    std::vector<std::vector<int>> distance = calc_distance_max(tab);


    int nbligne = distance.size();
    int nbcol = distance[0].size();
    int in = 0; //false

    auto [iS,jS] = find_S(tab);
    auto [i1,j1,i2,j2] = connected_to_S(tab,iS,jS);
    char rep = modifS(iS,jS,i1,j1,i2,j2,tab); //change S
    tab[iS][jS] = rep;

    int enclosedTiles = 0;
    for(int i = 0; i < nbligne; i++){
        for(int j = 0; j < nbcol; j++){
            if (distance[i][j] == -1){ // Not loop
                int contourCount = 0;
                for(int k = j+1; k < nbcol; k++){
                    if (distance[i][k] != -1){ // Is loop
                        switch (tab[i][k])
                        {
                        case '|':
                            contourCount += 1;
                            break;
                        case 'J':    
                            contourCount+=1;
                            break;
                        case 'L':
                            contourCount+=1;
                            break;
                        default:
                            break;
                        } 
                    } 
                }
                if (contourCount % 2 != 0){// impair
                    enclosedTiles +=1;
                }
            }
        }
    }

    std::cout << "Part2: " << enclosedTiles << std::endl;
}

int main(){
    part1();
    part2();
    return 0;
}