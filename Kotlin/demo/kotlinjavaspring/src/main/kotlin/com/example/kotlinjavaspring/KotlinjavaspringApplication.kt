package com.example.kotlinjavaspring

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import javax.persistence.*
import javax.transaction.Transactional

@SpringBootApplication
class KotlinjavaspringApplication

fun main(args: Array<String>) {
    runApplication<KotlinjavaspringApplication>(*args)
}

@Transactional
open class Service


@Entity
@Table
class Person(
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    var id: Long?,

    @Column
    var name: String,

    var age: Int
) {


}

