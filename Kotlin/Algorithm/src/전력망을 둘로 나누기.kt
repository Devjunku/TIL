import java.util.Queue
import java.util.LinkedList
private class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        var answer = n
        val arr = Array<MutableList<Int>>(n){mutableListOf()}

        wires.forEach{
            arr[it[0] - 1].add(it[1] - 1)
            arr[it[1] - 1].add(it[0] - 1)
        }

        wires.forEach{
            answer = Math.min(answer,
                Math.abs(bfs(arr, arr[it[0]-1], it[0]-1, it[1]-1) -
                        bfs(arr, arr[it[1]-1], it[1]-1, it[0]-1)))
        }
        return answer
    }
    private fun bfs(arr:Array<MutableList<Int>>, startNode:MutableList<Int>, s:Int, e:Int):Int{
        val hs = HashSet<Int>()
        val q:Queue<Int> = LinkedList<Int>()
        hs.add(s)

        for(n in startNode){
            if(n == e) continue
            hs.add(n)
            q.offer(n)
        }

        while(q.isNotEmpty()) {
            val now = q.poll()
            for(i in arr[now].indices){
                if(hs.contains(arr[now][i])) continue
                hs.add(arr[now][i])
                q.offer(arr[now][i])
            }
        }
        return hs.size
    }
}