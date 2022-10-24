package com.kotlinjava.exception;

import java.io.IOException;

public class JavaThrow {

    public void throwIOException() throws Exception {
        throw new IOException("체크드 익셉션인 IOException 발생!");
    }


    /**
     * kotlin의 throw는 예외처리를 강제하지 않음
     * 따라서 컴파일 오류가 발생하지 않음. 즉 다음과 같은 코드가 가능함.
     *
     * KotlinThrow kotlinThrow  = new KotlinThrow();
     * kotlinThrow.throwIOException();
     *
     *
     */


    public static void main(String [] args) {
        JavaThrow javaThrow = new JavaThrow();

        try {
            javaThrow.throwIOException();
        } catch (Exception e) {
            e.printStackTrace();
        }

        KotlinThrow kotlinThrow = new KotlinThrow();
        /**
         * 아래의 코드를 사용하지 않으러면 @Throws(IOException::class)를 사용하면 됨
         */
        //  kotlinThrow.throwIOException();

        try {
            kotlinThrow.throwIOException();
        } catch (IOException e) {
            e.printStackTrace();
        }



    }


}
