package com.example.kotlinPractice.`코틀린 개념`


public fun CoroutineScope.launch(
    context: CoroutineContext = EmptyCoroutineContext,
    start: CoroutineStart = CoroutineStart.DEFAULT,
    block: suspend CoroutineScope.() -> Unit
): Job  {
    val newContext = newCoroutineContext(context)
    val coroutine = if (start.isLazy) {
        LazyStandaloneCoroutine(newContext, block)
    } else {
        StandaloneCoroutine(newContext, active = true)
    }
    coroutine.start(start, coroutine, block)
    return coroutine
}

public fun <T> CoroutineScope.async(
    context: CoroutineContext = EmptyCoroutineContext,
    start: CoroutineStart = CoroutineStart.DEFAULT,
    block: suspend CoroutineScope. () -> T
): Deferred<T> {
    val newContext = newCoroutineContext(context)
    val coroutine = if (start.isLazy) {
        LazyDeferredCoroutine(newContext, block)
    } else {
        DeferredCoroutine<T>(newContext, active = true)
    }
    coroutine.start(start, coroutine, block)
    return coroutine
}

fun main()
{
    val nameList = listOf("박수영", "김지수", "김다현", "신유나", "김지우")
    nameList.forEach{println(it + " ")}
    println()

    println(nameList.filter{ it.startsWith("김") })
    println(nameList.map { "이름: " + it })
    println(nameList.any{ it == "김지연" })
    println(nameList.all { it.length == 3 })
    println(nameList.none { it.startsWith("이") })
    println(nameList.first { it.startsWith("김") })
    println(nameList.last { it.startsWith("김") })

    println(nameList.count { it.contains("") })



}