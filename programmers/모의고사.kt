class Solution {
    fun solution(answers: IntArray): IntArray {
        var pA = "12345".repeat(answers.size / 5 + 1).toList()
        var pB = "21232425".repeat(answers.size / 8 + 1).toList()
        var pC = "3311224455".repeat(answers.size / 10 + 1).toList()

        var scores = mutableListOf(0, 0, 0)

        answers.mapIndexed { i, v ->
            if (pA[i].toInt() - '0'.toInt() == v) {
                scores[0] += 1
            }

            if (pB[i].toInt() - '0'.toInt() == v) {
                scores[1] += 1
            }

            if (pC[i].toInt() - '0'.toInt() == v) {
                scores[2] += 1
            }
        }

        var maxV = scores.maxOf{it}
        var result = mutableListOf<Int>()

        scores.mapIndexed { i, v ->
            if (v == maxV) {
                result.add(i+1)
            }
        }

        return result.toIntArray()

    }
}
