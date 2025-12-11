#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <queue>
#include <algorithm>

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

int explore(vector<Device> devices, string target, pair<bool, bool> necessaryDevices = {false, false}){
    int paths = 0;
    find_if(devices.begin(), devices.end(), [&](Device& d){
        if(d.current == target){
            for(auto& t : d.targets){
                if(t == "out" && necessaryDevices.first && necessaryDevices.second){
                    paths += 1;
                }
                else{
                    if(t == "dac"){
                        necessaryDevices.first = true;
                    }
                    else if(t == "fft"){
                        necessaryDevices.second = true;
                    }
                    paths += explore(devices, t, necessaryDevices);
                }
            }
            return true;
        }
        return false;
    });
    return paths;
}

void part2(){
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
    /*
    find_if(devices.begin(), devices.end(), [&](Device& d){
        if(d.current == "svr"){
            for(auto& target : d.targets){
                paths += explore(devices, target);
            }
            return true;
        }
        return false;
    });
    */

    queue<pair<string, pair<bool, bool>>> queue; 
    find_if(devices.begin(), devices.end(), [&](Device& d){
        if(d.current == "svr"){
            for(auto& target : d.targets){
                queue.push({target, {false, false}});
            }
            return true;
        }
        return false;
    });
    vector<pair<string, pair<bool, bool>>> visited;
    visited.push_back({"svr", {false, false}});

    while(!queue.empty()){
        string target = queue.front().first;
        pair<bool, bool> necessaryDevices = queue.front().second;
        cout << "Visiting: " << target << " | DAC: " << necessaryDevices.first << " | FFT: " << necessaryDevices.second << endl;
        queue.pop();
        if(target == "out" && necessaryDevices.first && necessaryDevices.second){
            paths++;
        }
        else{
            find_if(devices.begin(), devices.end(), [&](Device& d){
                if(d.current == target){
                    for(auto& t : d.targets){
                        if(t == "dac"){
                            necessaryDevices.first = true;
                        }
                        else if(t == "fft"){
                            necessaryDevices.second = true;
                        }
                        //cout << "  Considering: " << t << " | DAC: " << necessaryDevices.first << " | FFT: " << necessaryDevices.second << endl;
                        if(find_if(visited.begin(), visited.end(), [&](pair<string, pair<bool, bool>>& v){
                            if(v.first == t){
                                if((v.second.first > necessaryDevices.first) || (v.second.second > necessaryDevices.second)){
                                    return true;
                                }
                            }
                            return false;
                        }) != visited.end()){
                            //cout << "Better find" << endl;
                            continue;
                        }
                        else{
                            if(find(visited.begin(), visited.end(), make_pair(t, necessaryDevices)) != visited.end()){
                                queue.push({t, necessaryDevices});
                            }
                            else{
                                visited.push_back({t, necessaryDevices});
                                queue.push({t, necessaryDevices});
                            }
                        }
                    }
                    return true;
                }
                return false;
            });
        }
    }

    cout << "Part 2: " << paths << endl;
}

int main(){
    part1();
    part2();
    return 0;
}