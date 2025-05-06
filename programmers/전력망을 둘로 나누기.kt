import java.util.*
import kotlin.math.*

class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {

        fun bfs(start: Int, wireList: MutableList<IntArray>): Int {
            var routes = mutableMapOf<Int, MutableSet<Int>>()
            wireList.forEach { wire ->
                if (routes[wire[0]] == null) {
                    routes[wire[0]] = mutableSetOf<Int>()
                }
                routes[wire[0]]!!.add(wire[1])

                if (routes[wire[1]] == null) {
                    routes[wire[1]] = mutableSetOf<Int>()
                }
                routes[wire[1]]!!.add(wire[0])
            }

            var visited = BooleanArray(n+1)
            var current = mutableListOf(start)

            var queue = ArrayDeque<Int>()
            queue.addLast(start)
            while (queue.size > 0) {
                var now = queue.pollFirst()
                if (!visited[now]) {
                    visited[now] = true
                    routes[now]?.let{
                        queue.addAll(it.toList())
                    }
                }
            }

            return visited.filter{it==true}.size
        }

        var wireList = wires.toMutableList()
        var networkDiffList = mutableListOf<Int>()
        repeat(wires.size) {
            var targetWire = wireList.removeAt(0)

            var networkA = bfs(1, wireList)
            var networkB = n - networkA
            networkDiffList.add(abs(networkA - networkB))

            wireList.add(targetWire)
        }

        return networkDiffList.sorted().first()
    }
}
