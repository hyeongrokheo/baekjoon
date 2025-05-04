class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var lostList = lost.filter{!reserve.contains(it)}.toList().sorted()
        var reserveList = reserve.filter{!lost.contains(it)}.toMutableList()

        var lostCount = 0

        lostList.forEach { l ->
            if (reserveList.contains(l-1)) {
                reserveList.remove(l-1)
            } else if (reserveList.contains(l+1)) {
                reserveList.remove(l+1)
            } else {
                lostCount += 1
            }
        }

        return n-lostCount
    }
}
