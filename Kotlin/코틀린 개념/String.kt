package com.example.kotlinPractice.`코틀린 개념`

fun main() {

//    val test1 = "test.kotlin.String"
//    println(test1.length) // 길이
//
//    println(test1.toLowerCase())
//    println(test1.toUpperCase())
//
//    val test2 = test1.split(".")
//    println(test2)
//
//    println(test2.joinToString(""))
//    println(test2.joinToString("-"))
//
//    println(test1.substring(5..10))

//    val nullString: String? = null
//    val emptyString = ""
//    val blankString = " "
//    val normalString = "A"
//
//    println(nullString.isNullOrEmpty())
//    println(emptyString.isNullOrEmpty())
//    println(blankString.isNullOrEmpty())
//    println(normalString.isNullOrEmpty())
//
//    println()
//
//    println(nullString.isNullOrBlank())
//    println(emptyString.isNullOrBlank())
//    println(blankString.isNullOrBlank())
//    println(normalString.isNullOrBlank())

    val test3 = "kotlin.kt"
    val test4 = "java.java"

    println(test3.startsWith("java"))
    println(test4.startsWith("java"))

    println()

    println(test3.endsWith(".kt"))
    println(test4.endsWith(".kt"))

    println()

    println(test3.contains("lin"))
    println(test4.contains("lin"))
}