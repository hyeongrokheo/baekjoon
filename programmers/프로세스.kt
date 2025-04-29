import java.util.*

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var deque = ArrayDeque<Pair<Int, Int>>()
        var p = priorities.mapIndexed{ i, v ->
            Pair<Int, Int>(v, i)
        }
        deque.addAll(p)

        var count = 0
        while (deque.size > 0) {
            var top = deque.pollFirst()

            if (deque.filter{ it.first > top.first }.size > 0) {
                deque.addLast(top)
            } else {
                count = count + 1
                if (top.second == location) {
                    return count
                }
            }
        }

        return -1
    }
}
