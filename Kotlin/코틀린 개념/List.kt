package com.example.kotlinPractice.`코틀린 개념`

fun main() {
    var a = listOf("사과", "딸기", "배")
    println(a[1])

    for(fruit in a) {
       println("${fruit}")
    }

    println()

    var b = mutableListOf(6, 3, 1)
    b.add(4)
    b.add(2, 8)

    b.removeAt(1)
    b.shuffle()
    b.sort()
    println(b)


}