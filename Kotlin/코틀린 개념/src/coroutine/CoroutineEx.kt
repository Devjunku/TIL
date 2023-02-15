package coroutine
import sun.rmi.server.Dispatcher
import kotlinx.coroutines.*


class CoroutineEx {



    val scope = CorouineScope(Dispatcher.Default)
    val coroutineA = scope.launch {}
    val coroutineB = scope.async {}




}




