package com.example.kotlinPractice

fun main() {
    data class Coding(val name: String, val birthYear: Int)

    val langList = listOf(Coding("c#", 2000),
        Coding("kotlin", 2011),
        Coding("Dart", 2011),
        Coding("Python", 1991))

    println(langList.associateBy{ it.birthYear })
    println(langList.groupBy{ it.name })

    val (over2010, under2010) = langList.partition{ it.birthYear > 2010 }
    println(over2010)
    println(under2010)


    val numbers = listOf(-3, 7, 2, -10, 1)
//    println(numbers.flatMap { listOf(it*10, it+10) })
    println(numbers.getOrElse(1) {50}) // 인덱스 1번 아이템이 없으면 50을 반환
    println(numbers.getOrElse(10) {50}) // 인덱스 10번 아이템이 없으면 50을 반환

    val names = listOf("A", "B", "C", "D")

    (names zip numbers).forEach{
        println(it.first)
        println(it.second)
    }
}