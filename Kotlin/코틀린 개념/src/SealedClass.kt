sealed class Developer {
    abstract val name: String
    abstract fun code(language: String)
}


data class FrontendDeveloper(
    override val name: String
    ): Developer() {
    override fun code(language: String) {
        println("Frontend개발자 ${name}입니다. ${language}를 주 언어로 사용합니다.")
    }
}

data class BackendDeveloper(
    override val name: String
    ): Developer() {
    override fun code(language: String) {
        println("Backend개발자 ${name}입니다. ${language}를 주 언어로 사용합니다.")
    }
}

object OtherDeveloper: Developer() {

    override val name: String = "익명"
    override fun code(language: String) {
        TODO("Not yet implemented")
    }

}

object DeveloperPool {
    val pool = mutableMapOf<String, Developer>()

    /**
     * Developer class를 상속 받은 class는 2개 밖에 없으나
     * complier는 이를 알지 못함
     * 따라서 when문에서 else를 지우면 컴파일 오류가 발생함.
     *
     * 다르게 생각하면, Developer를 상속 받은 class를 모두 다 아는 경우에는 굳이 else를 쓰지 않아도 되지마, 써야하고
     * 모르는 경우에는 파급되는 class를 제어하기 힘들어진다.
     * 따라서 이러한 경우 상속한 class를 봉하는 것이 필요한데, 그때 사용하는 것이 sealed class임.
     * 그러므로 이런한 경우 sealed class를 사용하면 코드 생산성이 매우 좋아지고 효율적으로 변함.
     */

    fun add(developer: Developer) = when(developer) {
        is FrontendDeveloper -> pool[developer.name] = developer
        is BackendDeveloper -> pool[developer.name] = developer
        is OtherDeveloper -> println("지원하지 않는 개발자 종류입니다.")
    }
    fun get(name: String) = pool[name]
}

fun main() {
    val backendDeveloper = BackendDeveloper("back")
    DeveloperPool.add(backendDeveloper)

    val frontendDeveloper = FrontendDeveloper("front")
    DeveloperPool.add(frontendDeveloper)

    println(DeveloperPool.get("back"))
    println(DeveloperPool.get("front"))
}