class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> test;
        for(int num : nums){
            if(test.count(num)){
                return true;
            }
            else{
                test.insert(num);
            }
        }
        return false;
    }
};