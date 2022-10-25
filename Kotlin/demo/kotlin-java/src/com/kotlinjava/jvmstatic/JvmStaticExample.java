package com.kotlinjava.jvmstatic;

public class JvmStaticExample {

    public static void main(String [] args) {
        /**
         * java에서 Companion object에 접근하려면, Companion property에 접근해야함.
         * 따라서 HelloClass.hello()로 사용할 수는 없음.
         */
        // String hello = HelloClass.Companion.hello();

        /**
         * object 또한 그냥 바로 접근할수는 없고 앞에 INSTANCE를 통해 접근해야함.
         */
        // Hiobject.INSTANCE.hi();

        /**
         * 이런 부분들이 매우 불편하기 때문에 companion object 또는 object에
         * @JvmStatic을 사용하면 곧바로 접근할 수 있다. 바로 아래와 같이 코드를 작성할 수 있음.
         */

        String hello = HelloClass.hello();
        Hiobject.hi();


    }


}
