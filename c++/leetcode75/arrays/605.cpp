#include <vector>
using std::vector;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);

        int count = 0, total = 0;
        for (int i = 0; i < flowerbed.size(); i++) {
            if (flowerbed[i] == 0) {
                count++;
            } else {
                if (count >= 3) {
                    total += (count - 1) / 2;
                }
                count = 0;
            }
        }

        if (count >= 3) {
            total += (count - 1) / 2;
        }

        return total >= n;
    }
};
