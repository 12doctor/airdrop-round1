
Rules:
    1. Must be twitter follower
       2. Must be discord member
       3. Must complete at least 1 swap

Process:

1. Remove all noise submissions with ETH addresses: 1_remove_eth_addr.py

2. Remove all submissions not following our twitter: 2_remove_twitter_unfollowed.py

3. Remove all submissions not joined our discord: 3_remove_discord_not_joined.py

4. Remove all submissions didn't complete at least 1 swap: 4_remove_not_swapped.py

5. Remove all submissions with duplicate twitter/discord/principal ids: 5_remove_duplicate_ids.py

   

Final result in ./data/5_result.csv, 9792 unique valid submissions.
