package com.example.kotlinspringtodolist.database

import com.example.kotlinspringtodolist.model.http.ToDoDto
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

data class ToDo(
    /**
     * 1. 인덱스
     * 2. 이름
     * 3. 설명
     * 4. 일정 시간
     * 5. 생성 시간
     * 6. 수정 시간
     */

    var index: Int?= null,
    var title: String? = null,
    var description: String? = null,
    var schedule: LocalDateTime? = null,
    var createdAt: LocalDateTime? = null,
    var updatedAt: LocalDateTime? = null
)

fun ToDo.convertToDo(toDoDto: ToDoDto):ToDo {
    return ToDo().apply {
        this.index = toDoDto.index
        this.title = toDoDto.title
        this.description = toDoDto.description
        this.schedule = LocalDateTime.parse(toDoDto.schedule, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
        this.createdAt = toDoDto.createdAt
        this.updatedAt = toDoDto.updatedAt
    }
}