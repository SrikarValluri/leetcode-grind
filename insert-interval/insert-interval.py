class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []


        for interval in intervals:
            # Option 1: newInterval higher in range than current Interval (no merging)
            if interval[1] < newInterval[0]:
                res.append(interval)

            # Option 2: newInterval lower in range than current Interval (no merging)
            elif  interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
                # Then this will probably go back to this option again, or maybe Option 1

            # Option 3: Merging is required!
            else:
                x = min(newInterval[0], interval[0]) # minimum x value
                y = max(newInterval[1], interval[1]) # maximum y value to merge ranges
                newInterval = [x, y]

        res.append(newInterval)

        return res
