#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

double straightLineDistance(vector<int> pointA, vector<int> pointB){
    double sum = pow((pointA[0] - pointB[0]), 2) + pow((pointA[1] - pointB[1]), 2) + pow((pointA[2] - pointB[2]), 2);
    return sqrt(sum);
}

void part1(){
    fstream file;
    file.open("datas/2025_day8_data");
    string line;
    vector<vector<int>> grid;
    while(getline(file,line)){
        stringstream ss(line);
        string number;
        vector<int> row;
        while(getline(ss, number, ',')){
            row.push_back(stoi(number));
        }
        grid.push_back(row);
    }
    int nbPairs = 0;
    int nbCircuits = 0;
    vector<int> circuitIndexes(grid.size(), -1);
    vector<int> circuitSizes;
    vector<pair<int,int>> indexClosestPoints;
    while (nbPairs < 1000){
        double distmin = straightLineDistance(grid[0],grid[1]);
        vector<int> pointA = grid[0];
        vector<int> pointB = grid[1];
        pair<int,int> tempClosestPoints = make_pair(0, 1);
        for(int i = 0; i < grid.size(); i++){
            for(int j = i+1; j < grid.size(); j++){
                double dist = straightLineDistance(grid[i],grid[j]);
                if (dist < distmin && (find(indexClosestPoints.begin(), indexClosestPoints.end(), make_pair(i,j)) == indexClosestPoints.end())) {
                    distmin = dist;
                    pointA = grid[i];
                    pointB = grid[j];
                    tempClosestPoints = make_pair(i, j);
                }
            }
        }
        if(circuitIndexes[tempClosestPoints.first] == -1 && circuitIndexes[tempClosestPoints.second] == -1){
            //create new circuit
            circuitIndexes[tempClosestPoints.first] = nbCircuits;
            circuitIndexes[tempClosestPoints.second] = nbCircuits;
            circuitSizes.push_back(2);
            nbCircuits++;
        } else if(circuitIndexes[tempClosestPoints.first] != -1 && circuitIndexes[tempClosestPoints.second] == -1){
            //add pointB to pointA circuit
            circuitIndexes[tempClosestPoints.second] = circuitIndexes[tempClosestPoints.first];
            circuitSizes[circuitIndexes[tempClosestPoints.first]]++;
        } else if(circuitIndexes[tempClosestPoints.first] == -1 && circuitIndexes[tempClosestPoints.second] != -1){
            //add pointA to pointB circuit
            circuitIndexes[tempClosestPoints.first] = circuitIndexes[tempClosestPoints.second];
            circuitSizes[circuitIndexes[tempClosestPoints.second]]++;
        } else {
            //merge circuits
            int circuitToKeep = circuitIndexes[tempClosestPoints.first];
            int circuitToRemove = circuitIndexes[tempClosestPoints.second];
            if(circuitToKeep == circuitToRemove){
                indexClosestPoints.push_back(tempClosestPoints);
                nbPairs++;
                continue;
            }
            else{
                for(int i = 0; i < circuitIndexes.size(); i++){
                    if(circuitIndexes[i] == circuitToRemove){
                        circuitIndexes[i] = circuitToKeep;
                    }
                }
                circuitSizes[circuitToKeep] += circuitSizes[circuitToRemove];
                circuitSizes[circuitToRemove] = 0;
            }
        }
        indexClosestPoints.push_back(tempClosestPoints);
        nbPairs++;
    }
    vector<int> largestCircuit = {-1, -1, -1};
    for(size_t i = 0; i < circuitSizes.size(); i++){
        if(largestCircuit[0] == -1){
            largestCircuit[0] = circuitSizes[i];
        } else if(largestCircuit[1] == -1){
            largestCircuit[1] = circuitSizes[i];
        } else if(largestCircuit[2] == -1){
            largestCircuit[2] = circuitSizes[i];
        }
        else{
            sort(largestCircuit.begin(), largestCircuit.end(), greater<int>());
            if(circuitSizes[i] > largestCircuit[0]){
                largestCircuit[2] = largestCircuit[1];
                largestCircuit[1] = largestCircuit[0];
                largestCircuit[0] = circuitSizes[i];
            } else if(circuitSizes[i] > largestCircuit[1]){
                largestCircuit[2] = largestCircuit[1];
                largestCircuit[1] = circuitSizes[i];
            } else if(circuitSizes[i] > largestCircuit[2]){
                largestCircuit[2] = circuitSizes[i];
            }
        }
    }
    int product = largestCircuit[0] * largestCircuit[1] * largestCircuit[2];

    cout << "Part 1: " << product << endl;
}


int main(){
    part1();
    cout << "Part 2: Let's see 2025_day8_optimized.cpp " << endl;
    return 0;
}