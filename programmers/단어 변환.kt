class Solution {
    fun solution(begin: String, target: String, words: Array<String>): Int {
        fun convertable(word1: String, word2: String): Boolean {
            var diffCount = 0
            (0..word1.length-1).forEach { index ->
                if (word1[index] != word2[index]) {
                    diffCount += 1
                }
            }

            return diffCount == 1
        }

        var convertCount = 0
        var currentWords = mutableListOf(begin)
        while (true) {
            if (currentWords.contains(target)) {
                break
            }

            convertCount += 1

            var newWords = mutableListOf<String>()
            currentWords.forEach { currentWord ->
                words.forEach { newWord ->
                    if (!currentWords.contains(newWord) && convertable(currentWord, newWord)) {
                        newWords.add(newWord)
                    }
                }
            }

            currentWords.addAll(newWords.toSet().toList())

            if (newWords.size == 0) {
                return 0
            }
        }

        return convertCount
    }
}
