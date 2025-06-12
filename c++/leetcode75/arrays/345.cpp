// LeetCode problem number: 345
// LeetCode problem name: Reverse Vowels of a String
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    string reverseVowels(string s) {
        vector<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        vector<char> word = {};
        vector<char> svowels = {};
        for (int i = 0; i < s.length(); i++){
            if (find(vowels.begin(), vowels.end(), s[i]) != vowels.end()) {
                svowels.push_back(s[i]);
                word.push_back('_');
            }
            else{
                word.push_back(s[i]);
            }
        }
        string newstring;
        int count = 0;
        for (int j = 0; j < s.length(); j++){
            if (word[j] != '_'){
                newstring += word[j];
            }
            else{
                newstring += svowels[svowels.size()-1-count];
                count++;
            }
        }
        return newstring;
    }
};