package com.example.kotlinPractice.`코틀린 개념`


// toString(), hashCode(), equals(), copy()
data class TicketA(val companyName: String, val name: String, var date: String, val seatNumber: Int)

class TicketB(val companyName: String, val name: String, var date: String, val seatNumber: Int)

fun main() {
//    val ticketA = TicketA("KoreanAir", "Junku", "2019-06-25", 14)
//    val ticketB = TicketB("KoreanAir", "Junku", "2019-06-25", 14)
//    println(ticketA)
//    println(ticketB) // 원래 이렇게 나오는게 맞음 (class)의 주소를 알려주는 것이 맞음
    // 근데 data class의 경우 데이터를 보여줌

//    val a = General("보영", 212)
//    println(a == General("보영", 212))
//    println(a.hashCode())
//    println(a)
//
//    val b = Data("루다", 306)
//    println(b == Data("루다", 306))
//    println(b.hashCode())
//    println(b)
//
//    println(b.copy())
//    println(b.copy("아린"))
//    println(b.copy(id = 618))

    var c = listOf(
        Data("아린", 1),
        Data("미주", 2),
        Data("미주", 2)
    )

    for((a, b) in c) {
        println("${a} ${b}")
    }

}

class General(val name: String, val id: Int)
data class Data(val name:String, val id: Int)
