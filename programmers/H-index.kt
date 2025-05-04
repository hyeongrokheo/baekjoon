import kotlin.math.*

class Solution {
    fun solution(citations: IntArray): Int =
        citations.sorted().reversed().mapIndexed { i, it ->
            minOf(it, i+1)
        }.maxOf{it}
}
