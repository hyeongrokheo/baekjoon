class Solution {
    fun solution(n: Int): IntArray {
        if (n == 1) {
            return intArrayOf(1)
        }

        var result = mutableListOf<MutableList<Int>>()
        (1..n).forEach {
            result.add(IntArray(it).toMutableList())
        }

        var currentHeight = 0
        var currentWeight = 0
        var currentNum = 2

        result[0][0] = 1

        var repeatCount = n/3 + if(n%3==0) 0 else 1
        repeat(repeatCount) {
            while (currentHeight+1 < n && result[currentHeight+1][currentWeight] == 0) {
                currentHeight += 1
                result[currentHeight][currentWeight] = currentNum
                currentNum += 1
            }

            while (currentWeight+1<n && result[currentHeight][currentWeight+1] == 0) {
                currentWeight += 1
                result[currentHeight][currentWeight] = currentNum
                currentNum += 1
            }

            while (result[currentHeight-1][currentWeight-1] == 0) {
                currentHeight -= 1
                currentWeight -= 1
                result[currentHeight][currentWeight] = currentNum
                currentNum += 1
            }
        }

        return result.flatMap{it}.toIntArray()
    }
}
