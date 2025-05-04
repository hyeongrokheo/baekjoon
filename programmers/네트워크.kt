class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var networkCount = 0
        var found = BooleanArray(n)

        fun search(comNum: Int) {
            if (found[comNum]) {
                return
            }
            found[comNum] = true
            computers[comNum].forEachIndexed { i, v ->
                if (v == 1 && i != comNum) {
                    search(i)
                }
            }
        }

        while (!found.all{it==true}) {
            search(found.indexOfFirst{it==false})
            networkCount += 1
        }

        return networkCount
    }
}
