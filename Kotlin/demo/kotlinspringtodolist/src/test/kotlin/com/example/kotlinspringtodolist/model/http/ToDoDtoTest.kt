package com.example.kotlinspringtodolist.model.http

import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test
import javax.validation.Validation

class ToDoDtoTest {

    /**
     * Test전 validator 불러오기
     * Validation, buildDefaultValidatorFactory().validator
     */

    val validator = Validation.buildDefaultValidatorFactory().validator

    @Test
    fun toDoDtoTest() {
        val toDoDto = ToDoDto().apply {
            this.title = "테스트"
            this.description = ""
            this.schedule = "2022-10-03 16:36:38"
        }

        val result = validator.validate(toDoDto)
        result.forEach {
            println(it.propertyPath.last().name)
            println(it.message)
            println(it.invalidValue)
        }
        Assertions.assertEquals(true, result.isEmpty())
    }

}