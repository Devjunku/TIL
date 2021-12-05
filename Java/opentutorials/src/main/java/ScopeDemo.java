class C {
    int left, right;


    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public void sum() {
        System.out.println(this.left + this.right);
    }

    public void avg() {
        System.out.println((this.left + this.right) / 2);
    }
}

class substractableCalculator extends C {
    public void substract() {
        System.out.println(this.left - this.right);
    }
}

class MultiplicationableCalculator extends C {
    public void multiplication() {
        System.out.println(this.left * this.right);
    }
}

class DivisionableCalculator extends MultiplicationableCalculator {
    public void division() {
        System.out.println(this.left / this.right);
    }
}

public class ScopeDemo {
    public static void main(String[] args) {
        substractableCalculator s = new substractableCalculator();
        s.setOprands(10, 20);
        s.sum();
        s.avg();
        s.substract();

        MultiplicationableCalculator m = new MultiplicationableCalculator();
        m.setOprands(10, 20);
        m.multiplication();

        DivisionableCalculator d = new DivisionableCalculator();
        d.setOprands(10, 20);
        d.multiplication();
        d.division();
    }
}