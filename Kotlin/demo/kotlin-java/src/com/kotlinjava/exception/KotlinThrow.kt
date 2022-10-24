package com.kotlinjava.exception

import com.kotlinjava.keyword.JavaKeyword
import java.io.IOException

class KotlinThrow {

    @Throws(IOException::class)
    fun throwIOException() {
        throw IOException("체크드 익셉션인 IOException 발생!")

    }
}

fun main() {
    val javaThrow = JavaThrow()
    javaThrow.throwIOException()

    val kotlinThrow = KotlinThrow()
    kotlinThrow.throwIOException()

    val keyword = JavaKeyword()
    keyword.`in`
    keyword.`is`
}