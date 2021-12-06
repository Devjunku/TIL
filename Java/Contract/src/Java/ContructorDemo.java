package Java;
class C {
    int left, right;

    public C(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public void sum() {
        System.out.println(this.left + this.right);
    }

    public int avg() {
        return ((this.left + this.right) / 2);
    }
}

class SubstractableCalculator extends C {
    public SubstractableCalculator(int left, int right) {
        super(left, right);
    }

    public void substract() {
        System.out.println(this.left - this.right);
    }

    public int avg() {
        return super.avg();
    }


}

public class ContructorDemo {
    public static void main(String[] args) {
        SubstractableCalculator s = new SubstractableCalculator(10, 20);
        s.sum();
        s.avg();
        s.substract();
    }
}
