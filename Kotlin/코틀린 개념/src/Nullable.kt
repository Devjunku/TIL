fun main(args: Array<String>) {
    var a: String? = null

    a = "kotlin Exam String"

    a?.run {
        println(uppercase())
        println(lowercase())
    }

}