class Solution {
    fun solution(diffs: IntArray, times: IntArray, limit: Long): Int {
        fun evaluate(level: Int): Long {
            var spendTime = 0L
            (0..diffs.size-1).forEach { index ->
                var diff = diffs[index]
                var time = times[index]

                if (diff > level) {
                    var timePrev = times[index-1]
                    spendTime += (diff-level) * (timePrev+time) + time
                } else {
                    spendTime += time
                }
            }

            return spendTime
        }

        var left = 1
        var right = 100000

        while (left < right) {
            var mid = (left + right) / 2
            // println("$left, $right, $mid, ${evaluate(mid)}")

            if (evaluate(mid) > limit) {
                left = mid+1
            } else {
                right = mid
            }
        }

        return left
    }
}
