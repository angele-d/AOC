#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>

using namespace std;


bool onlySpaces(string& s) {
    for (char c : s) {
        if (c != ' ') return false;
    }
    return true;
}

string removeSpaces(string& s) {
    string result;
    for (char c : s) {
        if (c != ' ') {
            result += c;
        }
    }
    return result;
}

void part1(){
    unsigned long long result = 0;
    fstream file;
    file.open("datas/2025_day6_data");
    string line;
    vector<vector<int>> numbers;
    vector<string> operators;
    while(getline(file,line)){
        bool isLastLine = (file.peek() == EOF);
        if(!isLastLine){
            stringstream ss(line);
            vector<int> elementI;
            string eltS;
            while (getline(ss,eltS,' ')){
                if(!onlySpaces(eltS)){
                    int eltI = stoi(eltS);
                    elementI.push_back(eltI);
                }
            }
            numbers.push_back(elementI);
        }
        else{
            stringstream ss(line);
            string elt;
            while (getline(ss,elt,' ')){
                if(!onlySpaces(elt)){
                    elt = removeSpaces(elt);
                    operators.push_back(elt);
                }
            }
        }
    }
    for(int j = 0; j < numbers[0].size(); j++){
        char op = operators[j][0];
        unsigned long long calc = 0;
        if (op == '*'){
            calc = 1;
        }
        for(int i = 0; i < numbers.size(); i++){
            switch (op){
            case '+':
                calc = calc + numbers[i][j];
                break;
            case '*':
                calc = calc * numbers[i][j];
                break;
            default:
                cout << "Problem at " << i << " " << j << ": " << op << endl;
                break;
            }
        }
        result = result + calc;
    }

    cout << "Part 1: " << result << endl;
}

void part2(){
    unsigned long long result = 0;
    fstream file;
    file.open("datas/2025_day6_data");
    string line;
    vector<string> lines;
    while(getline(file,line)){
        lines.push_back(line);
    }
    vector<string> numbers;
    vector<char> op;
    for(int j = 0; j < lines[0].size(); j++){
        string number = "";
        for(int i = 0; i < lines.size(); i++){
            if(isdigit(lines[i][j])){
                number = number + lines[i][j];
            }
            else if (lines[i][j] == '+' || lines[i][j] == '*'){
                op.push_back(lines[i][j]);
            }
        }
        numbers.push_back(number);        
    }
    int opIndice = 0;
    unsigned long long calc = 0;
    if(op[opIndice] == '*'){
        calc = 1;
    }
    for(auto s: numbers){
        if(onlySpaces(s)){
            result = result + calc;
            opIndice += 1;
            if(op[opIndice] == '*'){
                calc = 1;
            }
            else{
                calc = 0;
            }
        }
        else{
            switch(op[opIndice]){
                case '+':
                    calc = calc + stoull(s);
                    break;
                case '*':
                    calc = calc * stoull(s);
                    break;
            }
        }
    }
    result = result + calc;

    cout << "Part 2: " << result << endl;
}

int main(){
    part1();
    part2();
    return 0;
}