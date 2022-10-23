import java.time.LocalDateTime
import java.util.*

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    val immutableList = listOf("달러", "유로", "원")

    val mutableList = mutableListOf<String>().apply {
        this.add("달러")
        this.add("유로")
        this.add("원")
    }


    // ImmutableSet
    val numberSet = setOf(1, 2, 3, 4)

    // MutableSet
    val mutableSet = mutableSetOf<Int>().apply {
        this.add(1)
        this.add(2)
        this.add(3)
        this.add(4)
    }

    // ImmutableMap
    val numberMap = mapOf(
        "one" to 1,
        "two" to 2,
        "three" to 3
    )

    // MutableMap
    val mutableMap = mutableMapOf<String, Int>().apply {
        this["one"] = 1
        this["two"] = 2
        this["three"] = 3
    }

    /**
     * Collection Builder
     * 내부에서는 mutable, 외부에서는 immutable
     * 초기에는 가변적이지만, 이후 불변을 원한다면, buildList를 사용하는 것을 추천한디.
     */
    val numberList: List<Int> = buildList{
        add(1)
        add(2)
        add(3)
    }


    //LinkedList
    val linkedList = LinkedList<Int>().apply {
        addFirst(1)
        addFirst(2)
        addFirst(3)

    }

    //ArrayList
    val arrayList = ArrayList<Int>().apply {
        add(1)
        add(2)
        add(3)
    }

    // kotlin의 list는 java와 같이 Iterable함.
    val iterator = immutableList.iterator()
    while (iterator.hasNext()) {
        println(iterator.next())
    }
}