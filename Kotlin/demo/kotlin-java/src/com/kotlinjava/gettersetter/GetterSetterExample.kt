package com.kotlinjava.gettersetter

import java.time.LocalDate

fun main() {
    val person = Person()
    person.setName("junku")
    person.setBirthDate(LocalDate.of(2022, 10, 22))

    println(person.getName())
    println(person.getBirthDate())

    println(person.name)
    println(person.birthDate)

    /**
     * property가 없음애도, getter method면 property 처럼 사용이 가능하다.
     * 즉 앞에 method가 get이면 뒤에 있는 method는 그냥 property 처럼 사용이 가능한다.
     * 즉 java class 내부에 존재하는 method의 이름이 get이 아니면, kotlin 내부에서
     * getter로 complie 불가능하다는 것을 알아야 한다.
     */
    println(person.uuid)
}