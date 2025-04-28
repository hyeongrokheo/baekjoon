class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        var result = 1

        var clothesMap = clothes.groupBy {
            it[1]
        }

        clothesMap.values.forEach {
            result = result * (it.size + 1)
        }

        return result - 1
    }
}
