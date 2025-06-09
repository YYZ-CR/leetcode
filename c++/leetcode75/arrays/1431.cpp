#include <vector>
#include <algorithm>
using std::vector;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_value = *std::max_element(candies.begin(), candies.end());
        vector<bool> output_vector (candies.size());
        for (int i = 0; i < candies.size(); i++){
            output_vector[i] = candies[i] + extraCandies >= max_value;
        }
        return output_vector;
    }
};