class Solution {
    fun solution(numbers: IntArray): String {
        return if (numbers.toList().maxOrNull() == 0) {
            "0"
        } else {
            numbers
                .map{ it.toString() }
                .sortedWith(compareBy({it.repeat(4)}))
                .reversed()
                .joinToString("")
        }
    }
}
