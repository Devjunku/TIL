import kotlin.collections.MutableMap

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = IntArray(N)

        val indexMap: MutableMap<Int, Int> = mutableMapOf()
        val failureMap: MutableMap<Int, Double> = mutableMapOf()

        stages.forEach { it ->
            when(indexMap.containsKey(it)) {
                true -> indexMap[it] = indexMap.getValue(it) + 1
                false -> indexMap[it] = 1
            }
        }

        var totalSize = stages.size

        for (i in 1..N) {
            when (indexMap.containsKey(i)) {
                true -> {
                    failureMap[i] = (indexMap.getValue(i) / totalSize.toDouble())
                    totalSize -= indexMap.getValue(i)
                }
                false -> failureMap[i] = 0.0
            }
        }

        val list = failureMap.toList().sortedByDescending { (_, value) -> value}

        for (i in 0 until N) {
            answer[i] = list[i].first
        }

        return answer

    }
}