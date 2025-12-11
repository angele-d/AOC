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

struct Device{
    string current;
    vector<string> targets;
};

void part1(){
    fstream file;
    file.open("datas/2025_day11_data");
    string line;
    vector<Device> devices;
    while(getline(file, line)){
        stringstream ss(line);
        string token;
        getline(ss, token, ':');
        string temp;
        vector<string> targets;
        while(getline(ss, temp, ' ')){
            if(temp != ""){
                targets.push_back(temp);
            }
        }
        Device device;
        device.current = token;
        device.targets = targets;
        devices.push_back(device);
    }
    int paths = 0;
    queue<string> queue; 
    find_if(devices.begin(), devices.end(), [&](Device& d){
        if(d.current == "you"){
            for(auto& target : d.targets){
                queue.push(target);
            }
            return true;
        }
        return false;
    });
    while(!queue.empty()){
        string target = queue.front();
        queue.pop();
        if(target == "out"){
            paths++;
        }
        else{
            find_if(devices.begin(), devices.end(), [&](Device& d){
                if(d.current == target){
                    for(auto& t : d.targets){
                        queue.push(t);
                    }
                    return true;
                }
                return false;
            });
        }
    }

    cout << "Part 1: " << paths << endl;
}

long long explore(string target, bool hasDAC, bool hasFFT, unordered_map<string, vector<string>>& devices, map<tuple<string, bool, bool>, long long>& memo){
    if(target == "out"){
        return (hasDAC && hasFFT);
    }
    if(target == "dac"){
        hasDAC = true;
    }
    else if(target == "fft"){
        hasFFT = true;
    }
    if(memo.count({target, hasDAC, hasFFT})){
        return memo[{target, hasDAC, hasFFT}];
    }
    long long paths = 0;
    if(devices.count(target)){
        for(auto& t : devices[target]){
            paths += explore(t, hasDAC, hasFFT, devices, memo);
        }
    }
    memo[{target, hasDAC, hasFFT}] = paths;
    return paths;
}

void part2(){
    fstream file;
    file.open("datas/2025_day11_data");
    string line;
    unordered_map<string, vector<string>> devices;
    while(getline(file, line)){
        stringstream ss(line);
        string token;
        getline(ss, token, ':');
        string temp;
        while(getline(ss, temp, ' ')){
            if(temp != ""){
                devices[token].push_back(temp);
            }
        }
    }

    map<tuple<string, bool, bool>, long long> memo;
    
    long long paths = explore("svr", false, false, devices, memo);

    cout << "Part 2: " << paths << endl;
}

int main(){
    part1();
    part2();
    return 0;
}