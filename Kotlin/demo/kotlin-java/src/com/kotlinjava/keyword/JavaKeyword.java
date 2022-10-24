package com.kotlinjava.keyword;

import java.io.InputStream;

/**
 * 자바 코드에서 코틀린의 예약어를 변수명으로 정한 경우 사용할 수 없으나, 백틱 `` 을 이용하여 사용할 수 있음.
 * 예를 들어서 System.`in`이 있음.
 */


public class JavaKeyword {

    private InputStream in;

    private Boolean is;

    public InputStream getIn() {
        return in;
    }

    public Boolean getIs() {
        return is;
    }

    public void setIn(InputStream in) {
        this.in = in;
    }

    public void setIs(Boolean is) {
        this.is = is;
    }
}

enum CountryCodeJava{
    kr, kp, us;
}
