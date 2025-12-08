#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

double straightLineDistance(vector<int> a, vector<int> b) {
    double sum = pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2);
    return sqrt(sum);
}

// Union-Find structure
struct UnionFind {
    vector<int> parent;
    vector<int> size;
    UnionFind(int n) : parent(n), size(n, 1) {
        for(int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if(a == b) return false;
        if(size[a] < size[b]) swap(a,b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};

struct Edge {
    int u, v;
    double dist;
};

void part1() {
    fstream file("datas/2025_day8_data");
    string line;
    vector<vector<int>> grid;
    while(getline(file, line)){
        stringstream ss(line);
        string number;
        vector<int> row;
        while(getline(ss, number, ',')){
            row.push_back(stoi(number));
        }
        grid.push_back(row);
    }

    int n = grid.size();

    vector<Edge> edges;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            edges.push_back({i, j, straightLineDistance(grid[i], grid[j])});
        }
    }

    sort(edges.begin(), edges.end(), []( Edge a, Edge b){return a.dist < b.dist;});

    UnionFind unionFind(n);
    pair<int,int> lastMerge = {-1,-1};

    int mergeDone = 0;
    for(auto &e : edges){
        if(unionFind.unite(e.u, e.v)){
            lastMerge = {e.u, e.v};
        }
        mergeDone++;
        if(mergeDone == 1000) break;
    }

    vector<int> largestCircuit = {-1, -1, -1};
    for(size_t i = 0; i < n; i++){
        if(largestCircuit[0] == -1){
            largestCircuit[0] = unionFind.size[i];
        } else if(largestCircuit[1] == -1){
            largestCircuit[1] = unionFind.size[i];
        } else if(largestCircuit[2] == -1){
            largestCircuit[2] = unionFind.size[i];
        }
        else{
            sort(largestCircuit.begin(), largestCircuit.end(), greater<int>());
            if(unionFind.size[i] > largestCircuit[0]){
                largestCircuit[2] = largestCircuit[1];
                largestCircuit[1] = largestCircuit[0];
                largestCircuit[0] = unionFind.size[i];
            } else if(unionFind.size[i] > largestCircuit[1]){
                largestCircuit[2] = largestCircuit[1];
                largestCircuit[1] = unionFind.size[i];
            } else if(unionFind.size[i] > largestCircuit[2]){
                largestCircuit[2] = unionFind.size[i];
            }
        }
    }
    int product = largestCircuit[0] * largestCircuit[1] * largestCircuit[2];
    cout << "Part 1: " << product << endl;
}

void part2() {
    fstream file("datas/2025_day8_data");
    string line;
    vector<vector<int>> grid;
    while(getline(file, line)){
        stringstream ss(line);
        string number;
        vector<int> row;
        while(getline(ss, number, ',')){
            row.push_back(stoi(number));
        }
        grid.push_back(row);
    }

    int n = grid.size();

    vector<Edge> edges;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            edges.push_back({i, j, straightLineDistance(grid[i], grid[j])});
        }
    }

    sort(edges.begin(), edges.end(), []( Edge a, Edge b){return a.dist < b.dist;});

    UnionFind unionFind(n);
    pair<int,int> lastMerge = {-1,-1};

    // --- Merge edges until one circuit remains ---
    for(auto &e : edges){
        if(unionFind.unite(e.u, e.v)){
            lastMerge = {e.u, e.v};
            if(unionFind.size[unionFind.find(e.u)] == n) break; // all points connected
        }
    }

    unsigned long long product = static_cast<unsigned long long>(grid[lastMerge.first][0]) * static_cast<unsigned long long>(grid[lastMerge.second][0]);
    cout << "Part 2: " << product << endl;
}

int main() {
    part1();
    part2();
    return 0; 
}
