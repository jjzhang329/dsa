# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. 
# Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

# 2491. Divide Players Into Teams of Equal Skill https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

# Example 1:
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
# Example 2:
import collections
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # calculate the number of teams
        teams = len(skill) / 2
        # calculatre the total sum of skills
        target = int(sum(skill) / teams)
        count = collections.Counter(skill)
        pairs = []
        res = 0
        for idx, num in enumerate(skill):
            diff = target - num
            if diff in count and count[num] > 0:
                count[diff] -= 1
                count[num] -= 1
                pairs.append((num, diff))
        
        for k, v in count.items():
            if v != 0:
                return -1
        for a, b in pairs:
            res += a*b

        return res