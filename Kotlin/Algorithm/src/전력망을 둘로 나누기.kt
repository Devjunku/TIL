import java.util.Queue
import java.util.LinkedList

class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        var answer = n
        val graph = Array<MutableList<Int>>(n){mutableListOf()}

        wires.forEach{
            graph[it[0] - 1].add(it[1] - 1)
            graph[it[1] - 1].add(it[0] - 1)
        }

        wires.forEach{
            answer = Math.min(answer,
                Math.abs(
                    countNode(graph, graph[it[0]-1], it[0]-1, it[1]-1) -
                            countNode(graph, graph[it[1]-1], it[1]-1, it[0]-1)
                )
            )
        }
        return answer
    }

    fun countNode(graph:Array<MutableList<Int>>, startNode:MutableList<Int>, s:Int, e:Int):Int{

        val hs = HashSet<Int>() // 중복을 허용하지 않음
        val q:Queue<Int> = LinkedList<Int>()
        hs.add(s)
        for(n in startNode){
            if(n == e) continue
            hs.add(n)
            q.offer(n)
        }

        while(q.isNotEmpty()) {
            val now = q.poll()
            for(i in graph[now].indices){
                if(hs.contains(graph[now][i])) continue
                hs.add(graph[now][i])
                q.offer(graph[now][i])
            }
        }

        return hs.size
    }
}

