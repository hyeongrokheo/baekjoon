class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var remainDays = progresses.mapIndexed { i, v ->
            var remainProgress = 100-v
            var res = remainProgress / speeds[i]
            if (remainProgress % speeds[i] > 0) {
                res += 1
            }

            res
        }

        var res = mutableListOf<Int>()
        var flag = 0
        remainDays.forEach {
            if (it > flag) {
                res.add(1)
                flag = it
            } else {
                res[res.size-1] += 1
            }
        }

        return res.toIntArray()
    }
}
