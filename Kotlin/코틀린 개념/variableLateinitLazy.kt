package com.example.kotlinPractice.`코틀린 개념`

fun main(args: Array<String>) {

    val codingBoot = CodingBoot()

    codingBoot.search(CodingBoot.SPARTA_CODING)
    codingBoot.search(CodingBoot.CODE_STATES)
    codingBoot.search(CodingBoot.RISING_CAMP)

    val a = LateInitSample()
    println(a.getLateInitText())
    a.text = "늦게 할당했쥐롱"
    println(a.getLateInitText())

    val number: Int by lazy {
        println("초기화 했지렁~")
        10
    }

    println("초기화를 시작합니당~")
    println(number)
    println(number)

}

class CodingBoot {
    fun search(bootName: String) {

        val price = when(bootName) {
            SPARTA_CODING -> "얼마인지 잘 모름..."
            CODE_STATES -> "뭐가 제일 쌈?"
            RISING_CAMP -> "근데 전 부트캠프 갈 생각은 없습니당.."
            else -> 0
        }

        println("${bootName}.. ${price}ㅎㅎ 가격은 진짜 모르겠습니다.")

    }

    companion object {
        const val SPARTA_CODING = "스파르타코딩"
        const val CODE_STATES = "코드스테이트"
        const val RISING_CAMP = "라이징캠프"
    }
}

class LateInitSample{
    lateinit var text:String

    fun getLateInitText(): String {
        if(::text.isInitialized) {
            return "text"
        } else {
            return "default"
        }
    }
}