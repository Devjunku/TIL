fun main(args: Array<String>) {

    println(factorial(10))

}

private tailrec fun factorial(n: Int): Int {
    if (n == 1) {
        return 1
    }
    return n * factorial(n-1)
}
