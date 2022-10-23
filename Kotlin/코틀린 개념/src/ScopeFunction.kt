
fun main() {
    /**
     * let
     * null이 아닌 경우에 사용하고
     * 그에 따른 새로운 결과를 반환하고 싶을 때 사용함
     * 또한 lambda 함수처럼 마지막줄의 값이 return됨.
     * let을 중첩해서 사용하면 가독성이 별로 좋지 않아서
     * 중첩할 일이 있으면, if else 구문을 사용하는 것을 추천한다.
     */
    val str: String? = "null"

    val result: Int? = str?.let {
        println(it)
        val abc: String? = "abc"
        val def: String? = "def"
        if (!abc.isNullOrEmpty() && !def.isNullOrEmpty()) {
            println("abcdef가 null이 아님")
        }
        1234
    }
    println(result)

//    val config = DatabaseClient()
//    config.url = "localhost:3306"
//    config.username = "mysql"
//    config.password = "1234"
//    val contected = config.connect()
//    println(contected)

    /**
     * 위 코드를 run을 활용하여 바꾸면? 아래와 같음
     * 중복되는 코드 없이 바로바로 사용할 수 있는 것임
     * 아래 코드 역시 let을 통해서 코드를 작성할 수 있으나
     * it이 중복되므로, let보다는 run을 이용하여 만드는 것이 훨씬 좋다.
     */

    val connected: Boolean = DatabaseClient().run {
        url = "localhost:3306"
        username = "mysql"
        password = "1234"
        connect()
    }
    println(connected)


    /**
     * with는 결과 반환없이 내부에서 수신객체를 이용할 때 사용함.
     * 이 역시 람다 함수이기 때문에 마지막번 줄은 return 값이 됨.
     */

    val withEx = "안녕하세요"
    val length = with(withEx) {
        length
    }
    println(length)

    val connectedUsingWith = with(DatabaseClient()) {
        url = "localhost:3306"
        username = "mysql"
        password = "1234"
        connect()
    }
    println(connectedUsingWith)

    /**
     * apply는 수신객체의 property를 구성하고 그 수신객체를 그대로 반환하고 싶을 때 사용한다.
     */

    val connectedUsingApply: DatabaseClient = DatabaseClient().apply {
        url = "localhost:3306"
        username = "mysql"
        password = "1234"
        connect()
    }
    println(connectedUsingApply)

    connectedUsingApply.connect().run {
        println(this)
    }

    /**
     * also는 객체 그 자체의 동작을 제어하고 싶을 때 사용할 수 있음
     */

    val user: User = User(name = "tony", password = "1234")
    user.validate()

    // 코드를 also를 사용하면 위 코드를 다음과 같이 바꿀 수 있음.
    User(name = "tony", password = "1234").also {
        it.validate()
        it.printName()
    }

}

class DatabaseClient {
    var url: String? = null
    var username: String? = null
    var password: String? = null

    // DB에 접속하고 Boolean 결과를 반환
    fun connect(): Boolean {
        println("DB 접속 중...")
        Thread.sleep(1000)
        println("DB 접속 완료")
        return true
    }
}

class User(val name: String, val password: String) {
    fun validate() {
        if (name.isNotEmpty() && password.isNotEmpty()) {
            println("검증성공")
        } else {
            println("검증실패")
        }
    }
    fun printName() = println(name)
}