package v1ch03;

public class StringFunction {
    public static void main(String[] args) {
        String greeting = "Hello";
        String s = greeting.substring(0, 3);
        System.out.println(s);

        String expletive = "Expletive";
        String PG13 = "delete";
        String message = expletive + PG13;
        System.out.println(message);

        int age = 13;
        String rating = "PG" + age;
        System.out.println(rating);
        System.out.println("The boy age is  " + age);

        greeting = greeting.substring(0, 3) + 'p';
        System.out.println(greeting);

        boolean isEquals = "Hello".equals(greeting);
        System.out.println(isEquals);
        System.out.println("Help".equals(greeting));
        System.out.println("help".equals(greeting));
        System.out.println("Help".equalsIgnoreCase(greeting));
        int equalsResult = greeting.compareTo("help");
        System.out.println(equalsResult);
        System.out.println(greeting.compareTo("Help"));
        System.out.println(greeting.compareTo("Big"));
    }
}
