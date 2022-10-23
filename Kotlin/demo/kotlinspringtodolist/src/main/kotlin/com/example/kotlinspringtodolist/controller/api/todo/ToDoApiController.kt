package com.example.kotlinspringtodolist.controller.api.todo

import com.example.kotlinspringtodolist.model.http.ToDoDto
import com.example.kotlinspringtodolist.service.ToDoService
import org.springframework.http.HttpHeaders
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import javax.validation.Valid


@RestController
@RequestMapping("/api/todo")
class ToDoApiController(
    val toDoService: ToDoService
) {

    /**
     * CRUD 진행
     */

    // R
    @GetMapping(path = [""])
    fun read(@RequestParam(required = false) index: Int?): ResponseEntity<Any?> {
        return index?.let {
            toDoService.read(index)
        }?.let {
            return ResponseEntity.ok(it)
        }
        ?: run {
            return ResponseEntity
                .status(HttpStatus.MOVED_PERMANENTLY)
                .header(HttpHeaders.LOCATION, "/api/todo/all")
                .build()
        }
    }

    @GetMapping(path = ["/all"])
    fun readAll(): MutableList<ToDoDto>? {
        return toDoService.readAll()
    }

    // C
    /**
     * TODO: ResponseEntity로 내리기
     */
    @PostMapping(path = [ ""] )
    fun create(@Valid @RequestBody toDoDto: ToDoDto): ToDoDto? {
        return toDoService.create(toDoDto)
    }

    // U
    /**
     * TODO create, update에 따른 분기처리
     * U
     * create: 201
     * update: 200
     */
    @PutMapping(path = [ "" ])
    fun update(@RequestBody toDoDto: ToDoDto): ToDoDto? {
        return toDoService.update(toDoDto)
    }

    // D
    @DeleteMapping(path = [ "/{index}" ])
    fun delete(@PathVariable(name = "index") _index: Int): ResponseEntity<Any?> {

        when (toDoService.delete(_index)) {
            true -> return ResponseEntity.ok().build()
            false -> return ResponseEntity.status(500).build()
        }
    }
}