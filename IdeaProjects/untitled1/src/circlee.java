public class circlee {
    public static void main(String[] args) {

        Circle myCircle;

        myCircle = new Circle(10, new Point(0, 0));

        System.out.println("Area of the circle: " + myCircle.area());
        System.out.println("Perimeter of the circle: " + myCircle.perimeter());

        Circle anotherCircle = new Circle(8, new Point(15, 0));

        boolean doIntersect = myCircle.intersect(anotherCircle);
        if (doIntersect) {
            System.out.println("The circles intersect.");
        } else {
            System.out.println("The circles do not intersect.");
        }
    }
}