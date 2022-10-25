package com.kotlinjava.jvmstatic;

public class JvmFieldExample {

    public static void main(String [] args) {

        /**
         * kotlin의 static field를 java에서 사용하는 방법
         * 물론 깨알같이 get method를 만들어줬다.
         *
         * 하지만, static에 있는 const의 경우 직접 접근이 가능하다.
         */
        // JvmFieldClass.Companion.getId();
        // JvmFieldObject.INSTANCE.getName();
        int code = JvmFieldClass.CODE;
        String familyName = JvmFieldObject.FAMILY_NAME;

        /**
         * 물론 const 이외에도 property에 직접 접근을 하기 위해서는 @JvmField를 이용하면 된다.
         */
        int id = JvmFieldClass.id;
        String name = JvmFieldObject.name;
    }
}
