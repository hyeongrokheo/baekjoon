import java.util.*

class Solution {
    fun solution(jobs: Array<IntArray>): Int {
        var pq = PriorityQueue<Triple<Int, Int, Int>>(compareBy({it.first}, {it.second}, {it.third}))

        var jobs_list = jobs.mapIndexed { i, v ->
            Triple(v[1], v[0], i)
        }.sortedBy {
            it.second
        }.toMutableList()

        var current_time = 0
        var spended_time_sum = 0

        while (pq.size > 0 || jobs_list.size > 0) {
            while (jobs_list.size > 0 && jobs_list[0].second <= current_time) {
                pq.add(jobs_list[0])
                jobs_list.removeAt(0)
            }

            if (pq.size != 0 && pq.peek().second <= current_time) {
                var (time, requested_at, _) = pq.poll()
                current_time += time
                spended_time_sum += current_time - requested_at
            } else {
                current_time = jobs_list[0].second
            }
        }

        return spended_time_sum / jobs.size
    }
}
