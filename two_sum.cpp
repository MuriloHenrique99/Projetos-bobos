#include <iostream>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    for(int i = 0; i < nums.size(); ++i){
        for(int j = i + 1; j < nums.size(); ++j){
            if(nums[i] + nums[j] == target){
                return {i, j};
            }
        }
    }
    return {};
}

int main(){

    vector<int> num = {2,7,11,15};
    int target = 22;

    vector<int> res = twoSum(num, target);

    for(int checando : res){
        cout << checando << endl;
    }

    return 0;

}