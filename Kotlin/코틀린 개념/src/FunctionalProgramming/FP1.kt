package FunctionalProgramming

import java.util.Collections

/**
 * 일급객체란, 함수를 인자로서 사용하거나, 결과값으로 반환하거나 변수에 할당하는 것을 말한다.
 */


fun main() {
    // 1 함수도 타입이다!

    val func : () -> Unit = {}

    // 2 함수는 변수이다. 사용할 때는 함수이다! 라는 것을 알려주기 위해 ()를 사용하자.
    // 여기서 list안에 함수가 들어가 있다면, list에서 따로 할당하여 함수를 작동시킬 수 있다.

//    val list = mutableListOf(printHello)
//    val func0: () -> Unit = list[0]
//    func0()

    // 함수는 다른 함수의 인자로도 넣을 수 있다.
    call(printHello)

    // 여기서 fun으로 할당한 함수는 일급객체로 보지 않는다. 따라서 변수가 될 수 없다.

    // 인자가 여러개 일 떄
    val result = plus(2, 3, 4)
    println(result)

    // 고차함수

    val list = listOf("1", "2", "3")
//    val printStr: (String) -> Unit = {
//        println(it)
//    }
//
////    forEachStr(list, printStr)
//    list.forEach(printStr)
//
//    val upperCase: (String) -> String = {
//        it.uppercase()
//    }
//    println(list.map(upperCase))

//
//    val function = outerFunc()
//    function()


    // 후행 lambda 전달
    forEachStr(list) {
        println(it)
    }

    // lambda Reference
    val callReference = ::printHello
    callReference()()

    val numberList = listOf("1", "2", "3")
//    numberList.map { it.toInt() }.forEach { println(it) }
    numberList.map(String::toInt).forEach(::println)


}

val printHello: () -> Unit = { println("Hello") }

// 완전히 생략한 lambda식.
val summa = { a: Int, b: Int -> a + b }

// 함수를 받아서 Unit을 반환하는 함수, lambda 함수를 간결하게 작성할 수 있음.
fun outerFunc(): () -> Unit { return { println("익명함수") } }

fun forEachStr(collection: Collection<String>,  action: (String) -> Unit) {
    for (item in collection) {
        action(item)
    }
}


val printMessage: (String) -> Unit = {message: String ->
    println(message)
}
val printMessage2: (String) -> Unit = {message ->
    println(message)
}
val printMessage3: (String) -> Unit = {
    println(it)
}

val plus: (Int, Int, Int) -> Int = { a, b, c ->
    a + b + c
}




fun call(block: () -> Unit) {
    block()
}