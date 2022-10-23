package com.example.kotlinspringtodolist.model.http

import com.example.kotlinspringtodolist.database.ToDo
import com.example.kotlinspringtodolist.model.dateformatannotation.StringFormatDateTimeAnnotation
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import javax.validation.constraints.NotBlank
import javax.validation.constraints.NotNull

data class ToDoDto(
    
    var index: Int? = null,

    @field: NotBlank
    var title: String? = null,
    
    var description: String? = null,

    @field: NotBlank
    @field: StringFormatDateTimeAnnotation(pattern = "yyyy-MM-dd HH:mm:ss", message = "메세지 형식이 유효하지 않습니다.")
    var schedule: String? = null,

    var createdAt:LocalDateTime? = null,
    
    var updatedAt: LocalDateTime? = null
 ) {
    // TODO 이전에 사용했던 Custom Annotation 사용하면 됨. → StringFormatDateTimeAnnotation으로 대체함.
//    @AssertTrue(message = "yyyy-MM-dd HH:mm:ss format이 맞지 않습니다.")
//    fun ValidSchedule(): Boolean {
//        return try {
//            LocalDateTime.parse(schedule, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
//            true
//        } catch (e: Exception) {
//            false
//        }
//    }
}

fun ToDoDto.convertToDoDto(toDo: ToDo): ToDoDto {
    return ToDoDto().apply {
        this.index = toDo.index
        this.title = toDo.title
        this.description = toDo.description
        this.schedule = toDo.schedule?.format(DateTimeFormatter.ofPattern("yyy-MM-dd HH:mm:ss"))
        this.createdAt = toDo.createdAt
        this.updatedAt = toDo.updatedAt
    }
}
