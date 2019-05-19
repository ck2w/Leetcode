/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 * unordered_map records elements' hash value
 */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mapping;
        vector<int> result;
        for(int i=0; i<nums.size(); i++){
            if (mapping.find(nums[i]) == mapping.end()){
                mapping[nums[i]] = i;
            }
            if (mapping.find(target-nums[i]) != mapping.end() && mapping[target-nums[i]]<i){
                result.push_back(mapping[target-nums[i]]);
                result.push_back(i);
                break;
            }
        }
        return result;
    }
};


