package com.kotlinjava.gettersetter

import java.time.LocalDate

class Student {

    @JvmField
    var name: String? = null
    var birthDate: LocalDate? = null
    val age: Int = 10

    var grade: String? = null
        private set


    fun changeGrade(grade: String) {
        this.grade = grade
    }


    /**
     * grade를 var로 해도 private set을 사용하면, setter를 만들지 않아도 됨.
     * 단지 중요한 것은 class 내부에서는 변경이 가능함.
     */

}
