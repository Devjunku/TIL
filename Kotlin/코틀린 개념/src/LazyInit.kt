import kotlin.concurrent.thread

class HelloBot {
    val greeting: String? by lazy(LazyThreadSafetyMode.SYNCHRONIZED) {
        println("초기화 몇번될까")
        hello()
    }

    fun sayHello() = println(greeting)
}

fun hello() = "안녕하세요."


class `LateInit` {
    lateinit var text: String

    val textInitialized: Boolean
            get() = this::text.isInitialized

//    fun textPrint() {
//        text = "Hi"
//        if (this::text.isInitialized) {
//            println("초기화됨")
//        } else {
//            println("초기화되지 않음")
//        }
//        println(text)
//    }

}


fun main() {

    /**
     * 탑레벨 함수를 통한 지연 할당 방식
     * 이러한 경우 가변성에 많이 노출됨
     * 그렇기 때문에 불변성을 유지하면서
     * by lazy를 통해 지연초기화를 진행할 수 있음
     * by lazy는 정확히 한 번만 호출됨.
     * 또한 멀티스레드에 안전하게 설계되어 있음
     * lazy는 LazyThreadSafeMode에서 동기화를 설정해줄 수 있음 (안정성을 지정할 수 있음)
     */

//    var helloBot = HelloBot()
    //...
    //...
    //...
//    for (i in 0 until 5) {
//        Thread {
//            helloBot.sayHello()
//        }.start()
//    }


    /**
     * DI나 외부초기화를 염두해두고 만든 것임
     * isInitialized의 경우 top level에서 사용할 수 없음
     * 따라서 따로 getter를 만들어두며 됨.
     */
    var lateInit = LateInit()
    lateInit.text = "초기화"
    if (lateInit.textInitialized) {
        println("초기화됨")
    } else {
        println("그렇지 않음")
    }

}