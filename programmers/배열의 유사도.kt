class Solution {
    fun solution(s1: Array<String>, s2: Array<String>): Int {
        return s1.size - (s1.toSet() - s2.toSet()).size
    }
}
