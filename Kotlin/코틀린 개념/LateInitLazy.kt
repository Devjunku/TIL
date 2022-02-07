package com.example.kotlinPractice.`코틀린 개념`

fun main() {
    // 그 동안 변수의 기초적인 이야기를 진행했음
    // 이제 좀 주의해야할 사항을 이야기

    // var은 객체 변경이 가능
    // val은 불가능
    // 하지만 val에 할당된 데이터를 수정할 수 없는 것은 아님

    // 그런데 절대 변경이 불가능한 것이 있음 const(상수) 임
    // 이 상수는 변수의 속성이나 지역 변수로는 사용할 수 없음
    // companion object 안에 생성을 하든지 해서 객체의 생성과는 관계 없이
    // 클래스와 관계된 고정적인 값으로만 사용하게 됨
    // 상수는 일반적으로 모두 대문자와 언더바를 섞어 상수라는 것을 알림

    val foodCourt = FoodCourt()

    foodCourt.searchPrice(FoodCourt.FOOD_CREAM_PASTA)
    foodCourt.searchPrice(FoodCourt.FOOD_RAMEN)
    foodCourt.searchPrice(FoodCourt.FOOD_PIZZA)

    // 여기서 그럼 왜 굳이 이렇게 상수를 사용해서 코딩을 하는가면
    // 변수로 설정하여 코드를 작성하면, 성능의 하락이 발생하기 때문임
    // 따라서 고정적으로 사용하는 값은 상수로 표현하여 메모리에 저장하여 사용함
    // 좀 더 효율적으로 자원을 사용할 수 있기 때문임.


    // lateinit var -> 할당 전에 변수 선언만 해놓음

    // 1. 초기값 할당 전까지는 변수를 할당할 수 없음 (에러발생)
    // 2. 기본 자료형에는 사용할 수 없음  String class는 가능

    // 또한 lateinit 변수의 초기화를 하였는지 여부를 확인 할 떄는 변수 앞에 ::variable.isInitialized 이렇게 작성할 수 있음

    val a = LateInitSample()

    println(a.getLateInitText())
    a.text = "새로 할당한 값"

    println(a.getLateInitText())

    val number: Int by lazy {
        println("초기화 합니다.")
        7
    }

    println("코드를 시작합니다.")
    println(number)
    println(number)

    // 변수를 사용하는 시점까지
    // 초기화를 자동으로 늦춰주는 지연 대리자 속성
    // lazy delegate properties

}
class FoodCourt {
    fun searchPrice(foodName: String) { // 이때 어떤 음식이 들어있는지 알 수 없기 때문에 companion object를 통해 상수로 선언해주게 됨.
        val price = when(foodName) {
            FOOD_CREAM_PASTA -> 13000
            FOOD_RAMEN -> 8500
            FOOD_PIZZA -> 25000
            else -> 0
        }

        println("${foodName}의 가격은 ${price}원입니다.")
    }

    companion object {
        const val FOOD_CREAM_PASTA = "크림파스타"
        const val FOOD_RAMEN = "라면"
        const val FOOD_PIZZA = "피자"
    }
}

class LateInitSample {
    lateinit var text: String

    fun getLateInitText(): String {
        if(::text.isInitialized) {
            return text
        } else {
            return "기본값"
        }
    }
}