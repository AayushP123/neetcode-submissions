class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> se;
        unordered_map<char, int> te;

        for(int i = 0; i < s.length(); i++){
            se[s[i]]++;
            te[t[i]]++;
        }
    return se == te;
    }
};
