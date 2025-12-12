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

vector<pair<int,int>> rotateVector(const vector<pair<int,int>> vec) {
    /*Rotation to the right*/
    vector<pair<int,int>> result;
    for(auto& p : vec) {
        int x = p.first;
        int y = p.second;
        pair<int,int> temp = p;
        if(x == 0 && y == 0) temp = {0,2};
        else if(x == 0 && y == 1) temp = {1,2};
        else if(x == 0 && y == 2) temp = {2,2};
        else if(x == 1 && y == 0) temp = {0,1};
        else if(x == 1 && y == 1) temp = {1,1};
        else if(x == 1 && y == 2) temp = {2,1};
        else if(x == 2 && y == 0) temp = {0,0};
        else if(x == 2 && y == 1) temp = {1,0};
        else if(x == 2 && y == 2) temp = {2,0};
        result.push_back(temp);
    }
    return result;
}

vector<pair<int,int>> flipVector(const vector<pair<int,int>> vec) {
    /*Horizontal flip*/
    vector<pair<int,int>> result;
    for(auto& p : vec) {
        int x = p.first;
        int y = p.second;
        pair<int,int> temp = p;
        if(x == 0 && y == 0) temp = {0,2};
        else if(x == 0 && y == 1) temp = {0,1};
        else if(x == 0 && y == 2) temp = {0,0};
        else if(x == 1 && y == 0) temp = {1,2};
        else if(x == 1 && y == 1) temp = {1,1};
        else if(x == 1 && y == 2) temp = {1,0};
        else if(x == 2 && y == 0) temp = {2,2};
        else if(x == 2 && y == 1) temp = {2,1};
        else if(x == 2 && y == 2) temp = {2,0};
        result.push_back(temp);
    }
    return result;
}

bool tryAndPlace(vector<vector<bool>>& grid, unordered_map<int,vector<pair<int,int>>>& shapes, vector<int>& gifts, int indexGift){
    if(indexGift >= gifts.size()){
        return true;
    }
    int numberOfGiftsToPut = gifts[indexGift]; 
    auto shape = shapes[indexGift];
    
    if(numberOfGiftsToPut == 0){
        return tryAndPlace(grid, shapes, gifts, indexGift + 1);
    }
    gifts[indexGift]--;

    vector<vector<pair<int,int>>> transformations;
    transformations.push_back(shape);
    transformations.push_back(rotateVector(shape));
    transformations.push_back(rotateVector(rotateVector(shape)));
    transformations.push_back(rotateVector(rotateVector(rotateVector(shape))));
    transformations.push_back(flipVector(shape));
    transformations.push_back(rotateVector(flipVector(shape)));
    transformations.push_back(rotateVector(rotateVector(flipVector(shape))));
    transformations.push_back(rotateVector(rotateVector(rotateVector(flipVector(shape)))));

    for(auto& transShape : transformations){
        for(int i = 0; i <= grid.size() - 3; i++){
            for(int j = 0; j <= grid[0].size() - 3; j++){
                bool canPlace = true;
                for(auto& p : transShape){
                    int x = i + p.first;
                    int y = j + p.second;
                    if(grid[x][y]){
                        canPlace = false;
                        break;
                    }
                }
                if(canPlace){
                    for(auto& p : transShape){
                        int x = i + p.first;
                        int y = j + p.second;
                        grid[x][y] = true;
                    }
                    if(tryAndPlace(grid, shapes, gifts, indexGift)){
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

void part1(){
    fstream file;
    file.open("datas/2025_day12_data");
    string line;
    unordered_map<int,vector<pair<int,int>>> shapes;
    vector<pair<pair<int,int>,vector<int>>> regions;
    int currentGift = 0;
    while(getline(file, line)){
        if(line.empty()){
            currentGift++;
        }
        else if(line[0] == '#' || line[0] == '.'){
            string line2;
            string line3;
            getline(file, line2);
            getline(file, line3);
            for(int i = 0; i < line.size(); i++){
                if(line[i] == '#'){
                    shapes[currentGift].push_back({0,i});
                }
                if(line2[i] == '#'){
                    shapes[currentGift].push_back({1,i});
                }
                if(line3[i] == '#'){
                    shapes[currentGift].push_back({2,i});
                }
            }
        }
        else if(find(line.begin(), line.end(), 'x') != line.end()){
            stringstream ss(line);
            string token;
            int x, y;
            getline(ss, token, 'x');
            x = stoi(token);
            getline(ss, token, ':');
            y = stoi(token);
            vector<int> giftNumbers;
            while(getline(ss, token, ' ')){
                if(!token.empty()){
                    int giftNumber = stoi(token);
                    giftNumbers.push_back(giftNumber);
                }
            }
            regions.push_back({{y,x}, giftNumbers});
        }
    }

    unsigned long long regionsValid = 0;

    for(auto& region : regions){
        auto& length = region.first;
        auto& gifts = region.second;
        vector<vector<bool>> grid(length.first, vector<bool>(length.second, false));
        if(tryAndPlace(grid, shapes, gifts, 0)){
            regionsValid++;
        }
    }


    cout << "Part 1: " << regionsValid << endl;
}

int main(){
    part1();
    return 0;
}