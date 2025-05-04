class Solution {
    fun solution(numbers: String): Int {
        var res = mutableListOf<Int>()

        DFS(numbers.toList().map{it.toString().toInt()}, "", res)

        return res.toSet().size
    }

    fun DFS(numbers: List<Int>, n: String, res: MutableList<Int>) {
        if (!n.isBlank() && isPrime(n.toInt())) {
            res.add(n.toInt())
        }

        if (numbers.size > 0) {
            (0..numbers.size-1).forEach {
                var copyList = mutableListOf<Int>()
                copyList.addAll(numbers)
                var targetN = n + copyList[it]
                copyList.removeAt(it)
                DFS(copyList, targetN, res)
            }
        }
    }

    fun isPrime(number: Int): Boolean {
        if (number == 0) {
            return false
        } else if (number == 1) {
            return false
        } else if (number == 2) {
            return true
        } else if (number == 3) {
            return true
        }

        var count = 0
        (2..number-1).forEach {
            if (number % it == 0) {
                return false
            }
        }

        return true
    }
}
