class Solution {
    fun solution(word: String): Int {
        var dict = mutableListOf<String>()
        var gathers = listOf("A", "E", "I", "O", "U")

        fun dfs(str: String) {
            if (str.length > 5) {
                return
            }

            dict.add(str)
            gathers.forEach { gather ->
                dfs(str + gather)
            }
        }

        dfs("")

        dict.forEachIndexed { i, v ->
            if (v == word) {
                return i
            }
        }

        return 0
    }
}
