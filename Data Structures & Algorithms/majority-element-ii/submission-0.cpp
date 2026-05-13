class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> mrow;
        for(int num : nums){
            mrow[num]++;
        }

        vector<int> res;
        for(auto& s : mrow){
            if(s.second > (nums.size()/3)){
                res.push_back(s.first);
            }
        }
        return res;
    }
};