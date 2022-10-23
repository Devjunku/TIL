import java.time.LocalDateTime

object SingleTon {
    val a = 1234
    fun printA() = println(a)
}

object DateTimeUtils {
    val now: LocalDateTime
        get() = LocalDateTime.now()

    const val DEFAULT_FORMAT = "YYYY-MM-DD"

    fun same(a: LocalDateTime, b: LocalDateTime): Boolean = a == b
}