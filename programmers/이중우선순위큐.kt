import java.util.*

class Solution {
    fun solution(operations: Array<String>): IntArray {
        var min_queue = PriorityQueue<Int>(compareBy({it}))
        var max_queue = PriorityQueue<Int>(compareBy({-it}))

        operations.forEach { operation ->
            var operation_list = operation.split(" ")
            var op = operation_list[0]
            var value = operation_list[1].toInt()

            if (op == "I") {
                min_queue.add(value)
                max_queue.add(value)
            } else if (op == "D" && value == 1 && max_queue.size > 0) {
                min_queue.remove(max_queue.peek())
                max_queue.poll()
            } else if (op == "D" && value == -1 && min_queue.size > 0) {
                max_queue.remove(min_queue.peek())
                min_queue.poll()
            }
        }

        return if (min_queue.size > 0 && max_queue.peek() >= min_queue.peek()) {
            intArrayOf(max_queue.peek(), min_queue.peek())
        } else {
            intArrayOf(0, 0)
        }
    }
}
