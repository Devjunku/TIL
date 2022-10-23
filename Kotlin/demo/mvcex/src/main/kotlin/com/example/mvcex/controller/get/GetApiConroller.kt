package com.example.mvcex.controller.get

import com.example.mvcex.model.http.UserRequest
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController


@RestController
@RequestMapping("/api") // http://localhost:8080/api로 노출 , 이거 잊지 말기..
class GetApiConroller {

    @GetMapping(path = ["/hello", "/abcd"])
    /**
     * GET만 동작하면서 http://localhost:8080/api/hello에 노출되어 있음
     * 다른 주소로도 노출시킬 때는 path를 사용하여 `배열`로 넘겨주며, 다음과 같은 주소로 mapping되어 있음.
     * http://localhost:8080/api/hello
     * http://localhost:8080/api/abcd
     */
    fun hello(): String {
        return "hello kopring"
    }

    @RequestMapping(
        method=[RequestMethod.GET],
        path = ["/request-mapping"]
    ) //  GET, POST, DELETE, PUT 등 다 동작하게 됨.
    fun requestMapping(): String {
        return "request-mapping"
    }

    /**
     * path variable을 받는 방법
     */
    @GetMapping("/get-mapping/path-vaiable/{name}/{age}") // http://localhost:8080/api/get-mapping/path-vaiable/{name}로 노출
    fun pathVariable(@PathVariable name: String, @PathVariable age: Int): String {
        println("$name: ${name}, age: ${age}")
        return name + " " + age
    }

    @GetMapping("/get-mapping/pv/{name}/{age}") // http://localhost:8080/api/get-mapping/path-vaiable/{name}로 노출
    fun pathVariable2(@PathVariable(value = "name") _name: String, @PathVariable(value = "age") _age: Int): String {
        /**
         * 지역 변수 사용에서 함수 인자와 이름이 겹치는 경우가 있다. 이럴 경우는 거의 없겠지만, 있을 수도 있음
         * 현재 상황에서는 pathVariable의 name과 함수 인자인 _name이 일치하지 않는 경우임
         * 이때는 PathVariable 속성 중 value라는 속성이 있음 따라서 이 속성을 사용하면, path의 name과 함수 인자인 _name을 매칭시킬 수 있음.
         */
        val name = "kotlin"
        println("$name: ${_name}, age: ${_age}")
        return _name + " " + _age
    }

    /**
     * Query Parameter의 생김새
     * http://localhost:8080/api/page?key=value&key=value
     * 여기서 key는 모두 다른 값, value는 중복되어도 상관이 없음
     * 이때 중요한 것은 변수 명과 동일한 순서로 되어있으면 받을 수 있음.
     * 이 역시 value와 name 인자를 사용하여 queryParameter를 mapping 시킬 수 있음.
     *
     * 여기서 한 번 더 나아가서 이러한 parameter가 엄청 많은 경우 fun의 인자로 모두 다 넣어주기에는 너무 비효율적이기 때문에
     * 이를 object로서 받을 수 있음.
     */

    @GetMapping("/get-mapping/query-param") // ?name=junku&age=20로 보낼겁니다!
    fun queryParam(
        @RequestParam(name = "name") _name: String,
        @RequestParam(value = "age") _age: Int
    ): String {
        println("name: ${_name}, age: ${_age}")
        return "$_name $_age"
    }

    /**
     * 이름, 나이, 주소, 이메일 등 여러 가지 값을 받아야 하는 경우
     * 한 번에 받아서 처리하면 더 효율적일 것임
     * 따라서 이러한 param을 받도록 하는 class를 정의해야함.
     * 또한 기본적으로 spring에서 RestController를 선언하는 순간
     * return type이 object인 순간 json 형태로 바뀜.
     * 따라서 request를 받은 후 object 객체에 맵핑된 데이터는 json형태로 return되어 response 하게 됨.
     * 추가적으로 kotlin에서는 변수명에 '-'을 지원하지 않기 때문에 객체로 받을 수 없음
     * phone-number 불가능!
     */
    @GetMapping("/get-mapping/query-param/object")
    fun queryParamQbject(userRequest: UserRequest): UserRequest {
        println(userRequest)
        return userRequest
    }

    /**
     * map으로 query parameter를 받는 경우
     * 이때는 -으로도 받을 수 있음.
     * 왜냐하면 key값이기 때문에 아에 string형태로 들어가기 때문임.
     */
    @GetMapping("/get-mapping/query-param/map")
    fun queryParamMap(
        @RequestParam map: Map<String, Any>
    ): Map<String, Any> {
        println(map)
        return map
    }
}