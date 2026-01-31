# 703. Kth Largest Element in a Stream

We are constantly adding scores and we want to constantly track the `k` largest scores.

Hence, we are constantly maintaining the `k` largest values and we specifically care about the smallest of the `k` values at any time.

This makes for a perfect min-heap use case.

Note the edge case where `k == len(nums) + 1`.