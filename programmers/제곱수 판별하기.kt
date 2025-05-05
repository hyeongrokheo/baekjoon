import kotlin.math.*

class Solution {
    fun solution(n: Int): Int {
        return sqrt(n.toDouble()).toInt().let {
            if (it*it == n) 1 else 2
        }
    }
}
