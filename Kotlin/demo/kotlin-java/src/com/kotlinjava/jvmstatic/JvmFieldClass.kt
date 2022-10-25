package com.kotlinjava.jvmstatic

class JvmFieldClass {

    companion object {
        const val CODE = 1234
        @JvmField
        val id = 1234
    }

}

object JvmFieldObject {
    @JvmField
    val name = "tony"
    const val FAMILY_NAME = "stark"
}

fun main() {
    val id = JvmFieldClass.id
    val name = JvmFieldObject.name
}

/**
 * kotlin은 기본적으로 static field를 제공하고 있지 않음. 그리고 static의 특성을 kotlin에서 사용하고자 한다면,
 * object, companion object를 사용하면 됨.
 * 위의 것을 java에서 사용하는 경우는 좀 다르다.
 */