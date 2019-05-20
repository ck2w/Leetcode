/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 * 
 * https://leetcode.com/problems/two-sum/description/
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * 
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
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


