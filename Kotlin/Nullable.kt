package com.example.kotlinPractice

fun main() {

//    var sample: String? = "Kotlin Exam"

//    println(sample?.toUpperCase()) // null이어도 실행은 되는데 null만 반환
//    println(sample?:"default".toUpperCase()) // null이 default로 바뀌고 실행됨
//    println(sample!!.toUpperCase()) // null이어서 exception을 발생시킴

//    sample?.run {
//        println(toUpperCase())
//        println(toLowerCase())
//    }

    // 동일성 : 내용의 동일성: 내용만 같으면 됨, 객체의 동일성: 객체가 동일할 때

    var a = Product("콜라", 1000)
    var b = Product("콜라", 1000)
    var c = a
    var d = Product("사이다", 1000)

    println(a == b)
    println(a === b)

    println(a == c)
    println(a === c)

    println(a == d)
    println(a === d)

}


class Product(val name: String, val price: Int) {
    override fun equals(other: Any?): Boolean {
        if(other is Product) {
            return other.name == name && other.price == price
        } else {
            return false
        }
    }
}