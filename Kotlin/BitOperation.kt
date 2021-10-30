package com.example.kotlinPractice

fun main() {
    var bitData = 0b10000
    bitData = bitData or(1 or 2)
    println(bitData.toString(2))

    var result = bitData and(1 shl 4)
    println(result.toString(2))

    println(result shl 4)

    bitData = bitData and((1 shl 4).inv())
    println(bitData)

    println((bitData xor (0b10100)).toString(2))
}