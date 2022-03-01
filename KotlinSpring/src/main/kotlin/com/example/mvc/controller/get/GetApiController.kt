package com.example.mvc.controller.get

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController // RESTAPI Controller로 동작하겠다는 의미임
@RequestMapping("/api") // http://localhost:8080:api로 노출되게 됨
class GetApiController {

    @GetMapping(path = ["/hello", "/abcd"]) // http://localhost:8080:api/hello
    fun hello(): String {
        return "hello kotlin"
    }

    @RequestMapping(method = [RequestMethod.GET], path=["/request-mapping"])
    fun requestMapping(): String {
        return "request-mapping"
    }

    @GetMapping("/get-mapping/path-variable/{name}/{age}") // http://localhost:8080/api/get-mapping/path-variable/steve
    fun pathVariable(@PathVariable name: String, @PathVariable age: Int): String {
        println("${name}, ${age}")
        return name + " " + age
    }

    @GetMapping("/get-mapping/path-variable2/{name}/{age}") // http://localhost:8080/api/get-mapping/path-variable/steve
    fun pathVariable2(@PathVariable(value = "name") _name: String, @PathVariable(name = "age") age: Int): String {
        val name = "kotlin"
        println("${_name}, ${age}")
        return _name + " " + age
    }

    // https://localhost:8080/api/page?key=value=value&key=value
    @GetMapping("/get-mapping/query-param") // ?name=steve&age=20
    fun queryParam(
        @RequestParam name: String,
        @RequestParam(value = "age") age: Int
    ): String {
        println("${name}, ${age}")
        return name + " " + age
    }

}