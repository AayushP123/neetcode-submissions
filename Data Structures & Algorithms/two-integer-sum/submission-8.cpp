class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ruff;
        for(int i = 0; i < nums.size(); i++){
            ruff[nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i++){
            int ans = target - nums[i];
            if(ruff.count(nums[i]) && ruff[ans] != i){
                return {i, ruff[ans]};
            }
        }
        return {};
    }
};
