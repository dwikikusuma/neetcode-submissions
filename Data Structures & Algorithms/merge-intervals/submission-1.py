class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = []
        tmp = intervals[0]

        for interval in intervals[1:]:
            tmp_end = tmp[1]
            int_s = interval[0]
            int_e = interval[1]

            if tmp_end >= int_s:
                if tmp_end > int_e:
                    continue
                
                tmp[1] = int_e
            else:
                result.append(tmp)
                tmp = interval

        result.append(tmp)
        return result