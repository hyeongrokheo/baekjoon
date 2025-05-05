import kotlin.math.*

class Solution {
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        fun parse(t: String): Int {
            return t.split(":")[0].toInt() * 60 + t.split(":")[1].toInt()
        }

        var videoLen = parse(video_len)
        var position = parse(pos)
        var opStart = parse(op_start)
        var opEnd = parse(op_end)

        fun skipOp(position: Int): Int {
            return if (position >= opStart && position < opEnd) {
                opEnd
            } else {
                position
            }
        }

        fun zfill(str: String): String {
            return "0".repeat(2-str.length) + str
        }

        position = skipOp(position)

        commands.forEach { command ->
            when (command) {
                "next" -> {
                    position = min(position+10, videoLen)
                }
                "prev" -> {
                    position = max(position-10, 0)
                }
            }

            position = skipOp(position)
        }

        var minute = zfill((position/60).toString())
        var second = zfill((position%60).toString())

        return "$minute:$second"
    }
}
