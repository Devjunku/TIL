package com.example.kotlinPractice

fun main() {
    EventPrinter().start()
}

interface EventListener {
    fun onEvent(count: Int)
}

// 이벤트가 발생되는 Counter class
class Counter(var listener: EventListener) {
    fun count() {
        for(i in 1..100) {
            if(i % 5 == 0) listener.onEvent(i)
        }
    }
}

//class EventPrinter: EventListener {
//    override fun onEvent(count: Int) {
//        println("${count}-")
//    }
//
//    fun start() {
//        val counter = Counter(this)
//        counter.count()
//    }
//}

class EventPrinter {
    fun start() {
        val counter = Counter(object: EventListener {
            override fun onEvent(count: Int) {
                println("${count}-")
            }
        })
        counter.count()
    }
}