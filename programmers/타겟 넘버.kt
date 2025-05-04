class Solution {
    fun solution(numbers: IntArray, target: Int): Int {
        var count = 0

        fun dfs(currentSum: Int, index: Int) {
            if (index == numbers.size) {
                if (currentSum == target) {
                    count += 1
                }
            } else {
                val num = numbers[index]
                dfs(currentSum + num, index + 1)
                dfs(currentSum - num, index + 1)
            }
        }

        dfs(0, 0)
        println(count)
        return count
    }
}
