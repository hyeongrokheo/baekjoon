class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var totalSize = brown + yellow

        (1..totalSize).forEach { it ->
            if (totalSize % it == 0) {
                var width = totalSize / it
                var height = it

                if ((width - 2) * (height - 2) == yellow && width * 2 + height * 2 - 4 == brown) {
                    return intArrayOf(width, height)
                }
            }
        }

        return intArrayOf()
    }
}
