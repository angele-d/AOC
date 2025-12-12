#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <regex>

using namespace std;

struct Press{
    vector<int> schematicsPressed;
    vector<bool> lightsState;
};

Press pressButtons(const vector<vector<int>> wiringSchematics, Press currentPos, const vector<bool> lightsObjective, vector<Press> &memo, Press bestPos = {{},{}}){
    if(currentPos.schematicsPressed.size() > wiringSchematics.size()){
        return currentPos;
    }
    if(currentPos.schematicsPressed.size() >= bestPos.schematicsPressed.size() && bestPos.schematicsPressed.size() > 0){
        return bestPos;
    }
    for(auto it = memo.begin(); it != memo.end(); ++it){
        Press &p = *it;
        if(p.lightsState == currentPos.lightsState){
            if (p.schematicsPressed.size() <= currentPos.schematicsPressed.size()){
                return p;
            }
            else{
                memo.erase(it);
                memo.push_back(currentPos);
                return currentPos;
            }
        }
    }
    if(currentPos.lightsState == lightsObjective){
        memo.push_back(currentPos);
        return currentPos;
    }
    for(int i = 0 ; i < wiringSchematics.size(); i++){
        if(currentPos.schematicsPressed.size() > 0 && i == currentPos.schematicsPressed.back()){
            continue;
        }
        Press newPos;
        newPos.schematicsPressed = currentPos.schematicsPressed;
        newPos.schematicsPressed.push_back(i);
        vector<bool> newLightsState = currentPos.lightsState;
        for(int lightIndex : wiringSchematics[i]){
            newLightsState[lightIndex] = !newLightsState[lightIndex];
        }
        newPos.lightsState = newLightsState;
        
        newPos = pressButtons(wiringSchematics, newPos, lightsObjective, memo, bestPos);

        if(bestPos.schematicsPressed.size() == 0 || (newPos.schematicsPressed.size() < bestPos.schematicsPressed.size())){
            bestPos = newPos;
        }
    }
    return bestPos;
}

void part1(){
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


        vector<bool> lights(lightsObjective.size(),0);

        vector<Press> memo;
        Press initialState = {{}, lights};
        Press fewestPress = pressButtons(wiringSchematics, initialState, lightsObjective, memo);
        for(int schem : fewestPress.schematicsPressed){
            cout << schem << " ";
        }
        totalPressed += fewestPress.schematicsPressed.size();
    }
    cout << "Part 1: " << totalPressed << endl;
}

int main(){
    part1();
    cout << "Part 2: Let's see 2025_day10_part2.py" << endl;
    return 0;
}