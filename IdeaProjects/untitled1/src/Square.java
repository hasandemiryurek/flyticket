public class Square {
    public static void main(String[] args) {
        int a = 5;
        int b = a++;
        int c = ++a;
        int d = a++ + b-- + c++;

        System.out.println("a="+a+"b="+b+"c="+c+"d="+d);
    }

}
