import java.util.*

class Solution {
    fun solution(points: Array<IntArray>, routes: Array<IntArray>): Int {
        fun findRoute(targetPoints: List<Int>): MutableList<MutableList<Int>> {
            var route = mutableListOf<MutableList<Int>>()
            route.add(points[targetPoints[0]-1].toMutableList())

            (1..targetPoints.size-1).forEach { index ->
                var current = points[targetPoints[index-1]-1].toMutableList()
                var next = points[targetPoints[index]-1].toMutableList()

                while (current != next) {
                    if (current[0] != next[0]) {
                        if (next[0] - current[0] > 0) {
                            current[0] += 1
                        } else {
                            current[0] -= 1
                        }
                    } else {
                        if (next[1] - current[1] > 0) {
                            current[1] += 1
                        } else {
                            current[1] -= 1
                        }
                    }
                    var newCurrent = mutableListOf<Int>()
                    newCurrent.addAll(current)
                    route.add(newCurrent)
                }
            }

            return route
        }

        var allRoutes = routes.map {
            findRoute(it.toList())
        }
        var maxSize = allRoutes.maxOf{it.size}
        return (0..maxSize-1).map { index ->
            var allPoint = mutableListOf<MutableList<Int>>()

            allRoutes.forEach { route ->
                if (route.size > index) {
                    allPoint.add(route[index])
                }
            }

            allPoint.groupBy{it}.mapValues{(i, v) -> v.size}.values
        }.flatten().filter{it>1}.size
    }
}
