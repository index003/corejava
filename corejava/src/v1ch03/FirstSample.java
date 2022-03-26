package v1ch03;

public class FirstSample {
    public static void main(String[] args) {
        String sample = "We will not use 'Hello, World!";
        System.out.println(sample);
        for(int i = 0; i < sample.length(); i++) {
            System.out.print("=");
        }
        System.out.println();
        double x = 4;
        double y = Math.sqrt(x);
        System.out.println(y);
    }
}
