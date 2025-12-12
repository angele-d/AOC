
<h1> Useful C++ tools used in AOC </h1>

```c++
using namespace std;
```

>[!NOTE] Information  
> `%...%` means "Insert a correct value here"

<h2> Summary </h2>

- [I. Types](#i-types)
  - [String](#string)
    - [Separate](#separate)
    - [Search element](#search-element)
    - [Skip the beginning](#skip-the-beginning)
    - [Length](#length)
  - [Vector](#vector)
    - [Order](#order)
    - [End of vector](#end-of-vector)
    - [Vector of -1 numbers](#vector-of--1-numbers)
  - [Array](#array)
    - [Put each element in different variables](#put-each-element-in-different-variables)
  - [Pair](#pair)
    - [Put each element in different variables](#put-each-element-in-different-variables-1)
  - [Queue](#queue)
  - [Map](#map)
  - [unordered\_map](#unordered_map)
- [II. Utilities](#ii-utilities)
  - [Search in files](#search-in-files)
    - [Check if the next is EOF](#check-if-the-next-is-eof)
  - [String/Char to integer](#stringchar-to-integer)
    - [string To int](#string-to-int)
    - [string To unsigned long long](#string-to-unsigned-long-long)
    - [string To char](#string-to-char)
    - [char To integer](#char-to-integer)
- [III. Math tools](#iii-math-tools)
  - [Pow](#pow)
  - [sqrt](#sqrt)
- [IV. Optimization](#iv-optimization)
  - [Memoization](#memoization)
    - [(i,j) exploration](#ij-exploration)
    - [infos in DFS](#infos-in-dfs)
- [V. Prepared Structure](#v-prepared-structure)
  - [Union-find](#union-find)
  - [Edges: with distance between 2 edges](#edges-with-distance-between-2-edges)
  - [Point (+PointHash)](#point-pointhash)
  - [Hash Structures](#hash-structures)
    - [vector\<bool\>](#vectorbool)
- [VI. Prepared Functions](#vi-prepared-functions)
  - [On string](#on-string)
    - [containsOnlySpaces](#containsonlyspaces)
    - [removeSpaces](#removespaces)
  - [On int-\>double](#on-int-double)
    - [straightLineDistance *Distance euclidienne*](#straightlinedistance-distance-euclidienne)

---
---
# I. Types

---
## String

With \<string>

### Separate

With \<sstream>

```c++
stringstream ss(line);
string element;
getline(ss,element,'%separator%');
```

### Search element

```c++
size_t pos = line.find(%element%);
```

```c++
size_t pos = line.find(%element%,%start%); //from a start position
```

### Skip the beginning

```c++
line = line.substr(9); //to skip the 8 first letters

element = line.substr(i,nbOfElt) //keep element from i to i+nbOfElt
```


### Length

```c++
size_t length = line.length();
```

---
## Vector

With \<vector>

```c++
vector<int> elements; 
[...]
elements.push_back(%integer%);
```

```c++
vector<pair<int,int>> ranges;
ranges.push_back({%integer%,%integer%});
```

### Order

With \<algorithm>

```c++
sort(ranges.begin(),ranges.end()); //ASC from ranges.begin()
```

```c++
sort(edges.begin(), edges.end(), []( Edge a, Edge b){return a.dist < b.dist;}); //According to the dist of 2 edges
```

### End of vector

```c++
auto last = elements.back();
```

### Vector of -1 numbers

```c++
vector<vector<unsigned long long>> memo($lineSize$, vector<unsigned long long>($ColumnSize$, -1));
```

---
## Array

With \<array>

```c++
array<int,4> tup = {-1,-1,-1,-1};
```

Can check/change the elements with `tup[%indice%]`

### Put each element in different variables

```c++
auto [i1,i2,i3,i4] = tup;
```

---
## Pair

```c++
pair<int,int> range = {integer,integer};
```

### Put each element in different variables

```c++
int first = range.first;
int second = range.second;
```
OR
```c++
auto [i1,i2] = range;
```

---
## Queue

With \<queue>

```c++
queue<int> file;

//Push an element in the queue
file.push($integer$);

//Take the first element
int element = file.front();

//Drop an element
file.pop()
```

--- 
## Map

With \<map>

Init: 
```c++
map<tuple<string, bool, bool>, long long> memo;
```

Search in:
```c++
memo.count({target, hasDAC, hasFFT})
```

Add:
```c++
memo[{target, hasDAC, hasFFT}] = paths;
```

*See 2025_day11_optimized.cpp*

---
## unordered_map

With \<unordered_map>

Init:
```c++
unordered_map<string, vector<string>> devices;
```

Search in:
```c++
if(devices.count(target)){
    for(auto& t : devices[target]){
        %...%
    }
}
```

Add:
```c++
devices[token] = %vector<string>%;

devices[token].push_back(%string%);
```

*See 2025_day11_optimized.cpp*

---
---
# II. Utilities

---
## Search in files

With \<fstream> and \<string>

```c++
fstream file;
file.open(...);
if(!file){
    cerr << "Error opening file!" << endl;
    return ;
}
string line;
while (getline(file,line)){
    %...%
}
```

### Check if the next is EOF

```c++
bool isLastLine = (file.peek() == EOF);
```

---
## String/Char to integer

### string To int

```c++
int elementInt = stoi(elementString); //Gives a error number if it's not possible
```

### string To unsigned long long

```c++
unsigned long long elementInt = stoull(elementString);
```

### string To char

```c++
char c = str[0];
```

### char To integer

```c++
char character = %strchar%; 
int number = character - '0';
```

---
---

# III. Math tools

With \<cmath>

## Pow

```c++
pow(2,%upper%); //2**upper
```

## sqrt

```c++
sqrt(sum); //float, double, long double
```

---
---

# IV. Optimization

## Memoization

### (i,j) exploration

Use a `vector<vector<unsigned long long>>` initialized at `-1`

```c++
vector<vector<unsigned long long>> memo(%lineSize%, vector<unsigned long long>(%columnSize%, -1));
```

In the **recursive** function, add as parameter the *memo* with `&` to modify *memo* in all iterations

```c++
unsigned long long goDown(%parameters%, vector<vector<unsigned long long>> &memo){
  %...%
}
```

*See 2025_day07.cpp*

### infos in DFS

```c++
map<tuple<string, bool, bool>, long long> memo;
```

In the **recursive** function, add as parameter the *memo* with `&` to modify *memo* in all iterations

*See 2025_day11_optimized.cpp*

---
---

# V. Prepared Structure

## Union-find

```c++
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
```
*See 2025_day08_optimized.cpp*

## Edges: with distance between 2 edges

u,v = index *(for example: index in a vector\<vector\<int>> grid)*

```c++
struct Edge {
    int u, v;
    double dist;
};
```
*See 2025_day08_optimized.cpp*

---
## Point (+PointHash)

u,v = index of the Point

**PointHash:** Hash function to optimize the code

```c++
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
```

*See 2025_day09.cpp*

---
## Hash Structures

>[!NOTE] Already implemented Hash  
> For usual types *(such as int)*, the hash is already implemented when using `unordered_map`  

### vector\<bool>

```c++
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
```

*See 2025_day10_part1_optimized.cpp*

---
---

# VI. Prepared Functions

## On string

### containsOnlySpaces

Check if a `string` contains only `' '` 

```c++
bool containsOnlySpaces(string& s) {
    for (char c : s) {
        if (c != ' ') return false;
    }
    return true;
}
```

### removeSpaces

Remove all spaces from a `string` element

```c++
string removeSpaces(string& s) {
    string result;
    for (char c : s) {
        if (c != ' ') {
            result += c;
        }
    }
    return result;
}
```

## On int->double

### straightLineDistance *Distance euclidienne*

```c++
double straightLineDistance(vector<int> a, vector<int> b) {
    double sum = pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2);
    return sqrt(sum);
}
```

