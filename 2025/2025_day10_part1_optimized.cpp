#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <map>

using namespace std;

// Hash function for vector<bool>
struct VectorBoolHash {
    size_t operator()(const vector<bool>& v) const {
        size_t hash = 0;
        for (size_t i = 0; i < v.size(); ++i) {
            if (v[i]) {
                hash ^= (1ULL << (i % 64));
            }
        }
        return hash;
    }
};

int findFewestPresses(const vector<vector<int>>& wiringSchematics, const vector<bool>& lightsObjective) {
    int numLights = lightsObjective.size();
    int numButtons = wiringSchematics.size();
    
    // BFS approach with state = current lights configuration
    queue<pair<vector<bool>, int>> q; // (state, num_presses)
    unordered_map<vector<bool>, int, VectorBoolHash> visited; // state -> min presses to reach it
    
    vector<bool> initialState(numLights, false);
    q.push({initialState, 0});
    visited[initialState] = 0;
    
    while (!q.empty()) {
        auto [currentState, presses] = q.front();
        q.pop();
        
        // Check if we reached the goal
        if (currentState == lightsObjective) {
            return presses;
        }
        
        // Try pressing each button
        for (int button = 0; button < numButtons; ++button) {
            vector<bool> newState = currentState;
            
            // Toggle the lights affected by this button
            for (int lightIndex : wiringSchematics[button]) {
                newState[lightIndex] = !newState[lightIndex];
            }
            
            // Only explore if we haven't seen this state or found a shorter path
            if (visited.find(newState) == visited.end() || visited[newState] > presses + 1) {
                visited[newState] = presses + 1;
                q.push({newState, presses + 1});
            }
        }
    }
    
    return -1; // No solution found
}

void part1() {
    fstream file;
    file.open("datas/2025_day10_data");
    string line;
    
    int totalPressed = 0;

    while(getline(file,line)){
        string lightS;
        
        size_t open = line.find('[');
        size_t close = line.find(']');
        lightS = line.substr(open + 1, close - open - 1);
        vector<bool> lightsObjective;
        for(char s : lightS){
            if(s == '.') lightsObjective.push_back(0);
            else if(s == '#') lightsObjective.push_back(1);
            else cout << "Issue in lightS" << endl;
        }

        vector<vector<int>> wiringSchematics; 
        string temp;
        size_t start = close+1;
        while(true){
            open = line.find('(',start);
            if(open == string::npos)break;
            close = line.find(')',open+1);
            if(close == string::npos)break;
            temp = line.substr(open + 1, close - open - 1);
            stringstream ss(temp);
            string numberS;
            vector<int> wiring;
            while(getline(ss,numberS,',')){
                wiring.push_back(stoi(numberS));
            }
            wiringSchematics.push_back(wiring);
            start = close+1;
        }


        // Find minimum presses using BFS
        int fewestPresses = findFewestPresses(wiringSchematics, lightsObjective);
        
        totalPressed += fewestPresses;
    }
    cout << "Part 1: " << totalPressed << endl;
}


int main(){
    part1();
    return 0;
}