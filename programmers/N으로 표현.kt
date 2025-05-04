class Solution {
    fun solution(N: Int, number: Int): Int {
        val dp = mutableListOf<MutableSet<Int>>(mutableSetOf(0))

        (1..9).forEach { index ->
            var currentSet = mutableSetOf<Int>()

            dp[index-1].forEach {
                currentSet.add(it-N)
                currentSet.add(it+N)
                currentSet.add(it*N)
                currentSet.add(it/N)
            }

            (0..index-1).forEach { index2 ->
                var dn = N.toString().repeat(index - index2).toInt()

                dp[index2].forEach {
                    currentSet.add(it+dn)
                    currentSet.add(it-dn)
                    currentSet.add(it*dn)
                    currentSet.add(it/dn)
                }
            }

            // println(currentSet)
            if (currentSet.contains(number)) {
                return index
            }

            dp.add(currentSet)
        }
        return -1
    }
}
