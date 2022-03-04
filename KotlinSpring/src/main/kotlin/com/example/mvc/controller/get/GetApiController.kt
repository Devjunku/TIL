package com.example.mvc.controller.get

import com.example.mvc.model.http.UserRequest
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
        @RequestParam(value = "name") name: String,
        @RequestParam(value = "age") age: Int
    ): String {
        println("${name}, ${age}")
        return name + " " + age
    }
    // name, age, address, email 등 4가지 주소를 받아야 한다? 어떻게? 객체로 받는다!
    // 참고로 spring에서 반환타입이 object 형식이면 `json 형식`으로 바뀜
    /**
     * phoneNumber를 어떻게 받을 것이냐?
     * phone-number로 받고 싶은 데, 그럴 수 없음
     * 따라서 RequestParam으로 해서 name으로 받아야 함.
     */
    @GetMapping("/get-mapping/query-param/object")
    fun queryParamObject(userRequest: UserRequest): UserRequest {
        println(userRequest)
        return userRequest
    }

    /**
     * map 형태로 받기! 이게 더 좋네
     */
    @GetMapping("/get-mapping/query-param/map")
    fun queryParamMap(@RequestParam map: Map<String, Any?>): Map<String, Any?> {
        println(map)
        val phoneNumber = map["phone-number"]
        println(phoneNumber)
        return map
    }




}