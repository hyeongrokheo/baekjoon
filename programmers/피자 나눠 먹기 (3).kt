class Solution {
    fun solution(slice: Int, n: Int): Int {
        return n/slice + if (n%slice != 0) 1 else 0
    }
}
