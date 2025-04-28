class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        var genresMap = (0..genres.size-1).map {
            genres[it] to plays[it]
        }.groupBy {
            it.first
        }.mapValues { (k, v) ->
            v.sumOf { it.second }
        }

        var topGenres = genresMap
            .toList()
            .sortedByDescending{
                    (k,v) -> v
            }.map {
                it.first
            }

        var playInGenresMap = (0..genres.size-1).map {
            listOf(genres[it], it, plays[it])
        }.groupBy {
            it[0]
        }.mapValues { (k, v) ->
            v.sortedWith(
                compareBy(
                    { -(it[2] as Int) },
                    { (it[1] as Int) }
                )
            )
        }

        var result = mutableListOf<Int>()
        topGenres.forEach {
            var songInGenres = playInGenresMap[it]!!
            result.add(songInGenres[0][1] as Int)
            if (songInGenres.size > 1) {
                result.add(songInGenres[1][1] as Int)
            }
        }

        return result.toIntArray()
    }
}
