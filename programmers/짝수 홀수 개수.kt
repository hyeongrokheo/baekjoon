class Solution {
    fun solution(num_list: IntArray): IntArray {
        return num_list.filter{it%2==0}.size.let {
            intArrayOf(it, num_list.size-it)
        }
    }
}
