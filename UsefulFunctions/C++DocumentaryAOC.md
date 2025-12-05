
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
  - [Vector](#vector)
    - [Order](#order)
    - [End of vector](#end-of-vector)
  - [Array](#array)
    - [Put each element in different variables](#put-each-element-in-different-variables)
  - [Pair](#pair)
    - [Put each element in different variables](#put-each-element-in-different-variables-1)
  - [Queue](#queue)
- [II. Utilities](#ii-utilities)
  - [Search in files](#search-in-files)
  - [String/Char to integer](#stringchar-to-integer)
    - [string To int](#string-to-int)
    - [string To unsigned long long](#string-to-unsigned-long-long)
    - [char To integer](#char-to-integer)
- [III. Math tools](#iii-math-tools)

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


### Length

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

### End of vector

```c++
auto last = elements.back();
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

### char To integer

```c++
char character = %strchar%; 
int number = character - '0';
```

---
---

# III. Math tools

With \<cmath>

```c++
pow(2,%upper%); //2**upper
```