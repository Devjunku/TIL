import kotlin.concurrent.thread

class BankAccount {

    var balance: Double = 0.0
        private set

    fun deposit(depositAccount: Double) {
        balance += depositAccount
    }

    @Throws(InsufficientFunds::class)
    fun withdraw(withdrawAmount: Double) {
        if (balance < withdrawAmount) {
            throw InsufficientFunds()
        }
        balance -= withdrawAmount
    }
}

class InsufficientFunds: Exception()

//val account = BankAccount()
//println(account.balance) // 0.0
//account.deposit(100.0)
//println(account.balance) // 100.0
//account.withdraw(60.0)
//println(account.balance) // 40.0
//fun main() {
//    val lock = Any()
//    var num = 0
//    for (i in 1..1000) {
//        thread {
//            Thread.sleep(10)
//            synchronized(lock) {
//                num += 1
//            }
//        }
//    }
//    Thread.sleep(5000)
//    println(num)

//    var num = 0
//    for (i in 1..1000) {
//        thread {
//            Thread.sleep(10)
//            num += 1
//        }
//    }
//    Thread.sleep(5000)
//    print(num)
//}


//suspend fun main() {
//    var num = 0
//    coroutineScope {
//
//    }
//}