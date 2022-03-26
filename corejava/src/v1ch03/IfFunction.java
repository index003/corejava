package v1ch03;

public class IfFunction {
    public static void main(String[] args) {
        int yourSales = 1000;
        int target = 800;
        String performance = "Bad";
        int bonus = 0;
        if (yourSales > 2 * target) {
            performance = "Excellent";
            bonus = 1000;
        } else if (yourSales >=1.5 * target) {
            performance = "Fine";
            bonus = 500;
        } else if (yourSales >= 1 * target) {
            performance = "Satisfactory";
            bonus = 100;
        } else {
            System.out.println("You're fired!");
        }
        System.out.printf("performance = %s, bonus = %d\n", performance, bonus);
    }
}
