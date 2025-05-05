class Solution {
    fun solution(n: Int, edge: Array<IntArray>): Int {
        var edgeMap = mutableMapOf<Int, MutableSet<Int>>()

        edge.forEach { e ->
            if (edgeMap[e[0]] == null) {
                edgeMap[e[0]] = mutableSetOf<Int>(e[1])
            } else {
                edgeMap[e[0]]!!.add(e[1])
            }

            if (edgeMap[e[1]] == null) {
                edgeMap[e[1]] = mutableSetOf<Int>(e[0])
            } else {
                edgeMap[e[1]]!!.add(e[0])
            }
        }

        var currentNode = mutableListOf<Int>(1)
        var visited = BooleanArray(n+1)
        visited[1] = true
        var farNodeSize = 1

        while (true) {
            var newNode = mutableListOf<Int>()

            currentNode.forEach { node ->
                edgeMap[node]!!.forEach { nextNode ->
                    if (!visited[nextNode] && !currentNode.contains(nextNode)) {
                        visited[nextNode] = true
                        newNode.add(nextNode)
                    }
                }
            }

            // println("$currentNode, $newNode")

            if (newNode.size == 0) {
                break
            } else {
                farNodeSize = newNode.distinct().size
            }
            currentNode = newNode
        }

        return farNodeSize
    }
}
