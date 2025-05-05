class Solution {
    fun solution(n: Int, times: IntArray): Long {
        fun evaluate(time: Long): Long {
            return times.map{time/it}.sum()
        }

        var start = 1L
        var end = 1000000000000000000L
        var mid = 0L
        while (start < end) {
            mid = (start+end)/2

            println("$start, $end, $mid, ${evaluate(mid)}")

            if (evaluate(mid) >= n) {
                end = mid
            } else {
                start = mid+1
            }
        }
        return end
    }
}
