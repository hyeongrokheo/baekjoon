class Solution {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        var ticketList = mutableListOf<MutableList<String>>()
        var used = BooleanArray(tickets.size)

        tickets.sortedBy{it[1]}.forEach { ticket ->
            ticketList.add(mutableListOf(ticket[0], ticket[1]))
        }

        fun dfs(current: MutableList<MutableList<String>>): MutableList<MutableList<String>>? {
            if (current.size == tickets.size+1) {
                return current
            } else {
                ticketList.forEachIndexed { i, ticket ->
                    if (!used[i] && ticket[0] == current.last()[1]) {
                        used[i] = true

                        current.add(ticket)
                        dfs(current)?.let { return it }
                        current.removeAt(current.size-1)

                        used[i] = false
                    }
                }
                return null
            }
        }

        var result = dfs(mutableListOf(mutableListOf("", "ICN")))!!

        return result.map{it[1]}.toTypedArray()
    }
}
