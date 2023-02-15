package com.example.kotlinPractice.KotlinAdvanced

fun isLetter(c: Char) = c in 'a'..'z' || c in 'A'..'Z'

fun isNotDigit(c: Char) = c in '1'..'9'

fun main() = with(BufferedReader(InputStreamReader()))