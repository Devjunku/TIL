package com.example.kotlinPractice.`코틀린 개념`

fun main() {

    var a = FoodPoll("짜장")
    var b = FoodPoll("짬뽕")

    a.vote()
    a.vote()

    b.vote()
    b.vote()
    b.vote()

    println("${a.name}, ${a.count}")
    println("${b.name}, ${b.count}")

    println("${FoodPoll.total}")


}

//open class Animal(var name: String, var age: Int, var type: String) {
//    fun introduce() {
//        println("안녕하세요. 저는 ${type} ${name}이고 ${age}살 입니다.")
//    }
//}
//
//// 1. 서브 클래스는 슈퍼 클래스에서 갖는 속성의 이름과 같은 이름의 속성을 갖을 수 없음
//// 2. 서브 클래스가 생성될 때는 반드시 슈퍼 클래스의 생성자까지 호출되어야 함.
//
//class Dog(name:String, age: Int) : Animal (name, age, "개") {
//    fun bark() {
//        println("멍멍~!")
//    }
//
//    fun moew() {
//        println("야옹~!")
//    }
//}

//override

//open class Animal {
//
//    open fun eat() {
//        println("음식을 먹습니다.")
//    }
//}
//
//class Tiger : Animal() {
//    override fun eat() {
//        println("고기를 먹습니다.")
//    }
//}

// abstract

//abstract class Animal {
//    abstract fun eat()
//    fun sniff() {
//        println("킁킁!")
//    }
//}
//
//class rabbit: Animal() {
//    override fun eat() {
//        print("당근을 먹습니다.")
//    }
//}

// 추상함수는 생성자는 갖을 수 있으나, 인터페이스는 생성자를 갖을 수 없음
// 구현부가 있는 함수는 open 함수
// 구현부가 없는 함수는 abstact 함수
// 따라서 별도의 open 선언이 없어도 인터페이스에 포함된 모든 함수는 sub class에서 재구현이 가능하다.
// 또한 한 번에 여러 인터페이스를 상속 받을 수 있어 좀 더 유연한 설계가 가능함.

// interface

//interface Runner {
//    fun run()
//}
//
//interface Eater {
//    fun eat() {
//        println("음식을 먹습니다.")
//    }
//}
//
//class Dog : Runner, Eater {
//    override fun run() {
//        println("우다다다 뜁니다.")
//    }
//
//    override fun eat() {
//        println("허겁지겁 먹습니다.")
//    }
//}

// Object

//object Counter {
//    var count = 0
//
//    fun countUp() {
//        count ++
//    }
//
//    fun clear() {
//        count = 0
//    }
//}

// static: 클래스 내부에서 별도의 영역에 고정적으로 존재하여 인스턴스를 생성하지 않아도 공용으로 사용 가능한 속성이나 함수

class FoodPoll(val name:String) {
    companion object {
        var total = 0
    }

    var count = 0

    fun vote() {
        total ++
        count ++
    }

}