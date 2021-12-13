import java.util.Scanner

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    val m = sc.nextInt()

    val arr = IntArray(n+1) {0}


    for (i in 1..n) arr[i] += arr[i-1] + sc.nextInt()

    var i: Int
    var j: Int
    for (k in 0 until m) {
        i = sc.nextInt()
        j = sc.nextInt()
        println(arr[j] - arr[i-1])
    }
    sc.close()
}