import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var bridge = ArrayDeque<Int>()
        var truck_weight_sum = 0
        var trucks = ArrayDeque<Int>()

        trucks.addAll(truck_weights.toList())

        bridge.addAll(
            (0..bridge_length-1).map{ 0 }
        )

        var time = 0
        while (true) {
            if (truck_weight_sum == 0 && trucks.size == 0) {
                break
            }
            time += 1

            var end_truck = bridge.pollLast()
            truck_weight_sum = truck_weight_sum - end_truck

            var cand: Int? = trucks.peekFirst()
            if (cand != null && truck_weight_sum + cand <= weight) {
                trucks.pollFirst()
                truck_weight_sum += cand
                bridge.addFirst(cand)
            } else {
                bridge.addFirst(0)
            }
        }

        return time
    }
}
