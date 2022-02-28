package com.example.mvc.controller.get

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
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



}