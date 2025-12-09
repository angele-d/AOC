#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <unordered_set>

using namespace std;

struct Point {
    int u, v;

    bool operator==(const Point& other) const {
        return u == other.u && v == other.v;
    }
};

struct PointHash {
    size_t operator()(const Point& p) const noexcept {
        return ((size_t)p.u << 32) ^ (size_t)p.v;
    }
};


unsigned long long surface(pair<int,int> a, pair<int,int> b){
    //cout << "Calculating surface between (" << a.first << "," << a.second << ") and (" << b.first << "," << b.second << ")\n";
    //cout << "Result: " << (abs(a.first - b.first)+1) << " * " << (abs(a.second - b.second)+1) << " = " << (abs(a.first - b.first)+1) * (abs(a.second - b.second)+1) << endl;
    unsigned long long dx = (unsigned long long)abs(a.first - b.first) + 1;
    unsigned long long dy = (unsigned long long)abs(a.second - b.second) + 1;
    return dx * dy;}

void part1(){
    fstream file;
    file.open("datas/2025_day09_data");
    string line;
    vector<pair<int,int>> positions;
    while(getline(file,line)){
        stringstream ss(line);
        string xStr, yStr;
        getline(ss, xStr, ',');
        getline(ss, yStr, ',');
        positions.push_back({stoi(xStr), stoi(yStr)});
    }

    int n = positions.size();

    unsigned long long maxSurface = 0;;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            unsigned long long surf = surface(positions[i], positions[j]);
            if(surf > maxSurface){
                maxSurface = surf;
            }
        }
    }

    cout << "Part 1: " << maxSurface << endl;
}

bool rectangleCrossedBySegment(pair<int,int> a, pair<int,int> b, unordered_set<Point,PointHash>& pointSet){
    int minX = min(a.first, b.first);
    int maxX = max(a.first, b.first);
    int minY = min(a.second, b.second);
    int maxY = max(a.second, b.second);

    for(Point point: pointSet){
        if(point.u > minX && point.u < maxX && point.v > minY && point.v < maxY){
            return true;
        }
    }
    return false;
}

void part2(){
    fstream file;
    file.open("datas/2025_day09_data");
    string line;
    vector<pair<int,int>> positions;
    while(getline(file,line)){
        stringstream ss(line);
        string xStr, yStr;
        getline(ss, xStr, ',');
        getline(ss, yStr, ',');
        positions.push_back({stoi(xStr), stoi(yStr)});
    }

    int n = positions.size();

    unordered_set<Point,PointHash> pointSet;
    for(int i = 0 ; i < n; i++){
        int j = (i+1)%n;
        int minX = min(positions[i].first, positions[j].first);
        int maxX = max(positions[i].first, positions[j].first);
        int minY = min(positions[i].second, positions[j].second);
        int maxY = max(positions[i].second, positions[j].second);
        for(int x = minX; x <= maxX; x++){
            for(int y = minY; y <= maxY; y++){
                    pointSet.insert({x,y});
            }
        }
    }

    unsigned long long maxSurface = 0;;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            unsigned long long surf = surface(positions[i], positions[j]);
                if(surf > maxSurface){
                    if(!rectangleCrossedBySegment(positions[i], positions[j], pointSet)){
                        maxSurface = surf;
                    }
                }
        }
    }

    cout << "Part 2: " << maxSurface << endl;
}

int main(){
    part1();
    part2();
    return 0;
}