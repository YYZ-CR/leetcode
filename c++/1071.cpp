#include <string>
#include <algorithm>
using std::string;
#include <numeric> // for std::gcd

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1){
            return "";
        }
        int i = 0;
        std::string g;
        int gcd = std::gcd(str1.length(),str2.length());
        while (str1[i] == str2[i] && i < gcd){
            g+= str1[i];
            i++;
        }
        return g;
    }
};