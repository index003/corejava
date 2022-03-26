package v1ch03;

public class WhileFunction {
    public static void main(String[] args) {
        double balance = 0.0;
        int years = 0;
        double goal = 1000000.0;
        double payment = 20000.0;
        double interestRate = 5.0;

        while (balance < goal) {
            balance += payment;
            double interest = balance * interestRate / 100;
            balance += interest;
            years++;
        }
        System.out.println(years);
    }
}
