#include <algorithm>
#include <string>
using std::string;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string outputstring; 
        for(int i = 0; i < std::min(word1.length(), word2.length()); i++){
            outputstring += word1[i];
            outputstring += word2[i];
        }
        if(word1.length() > word2.length()){
            outputstring += word1.substr(word2.length());
            return outputstring;
        }
        outputstring += word2.substr(word1.length());
        return outputstring;
        
    }
};