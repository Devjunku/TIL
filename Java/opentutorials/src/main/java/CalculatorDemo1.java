class Calculator {
    static double PI = 3.14;
    int left, right;

    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public int sum() {
        System.out.println(this.left + this.right);
        return this.left + this.right;
    }

    public int avg() {
        System.out.println(sum());
        return sum()/2;
    }
}

public class CalculatorDemo1 {



}
