import kotlin.math.*

class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        var weight = 0
        var height = 0

        sizes.forEach {
            weight = max(weight, max(it[0], it[1]))
            height = max(height, min(it[0], it[1]))
        }

        return weight * height
    }
}
