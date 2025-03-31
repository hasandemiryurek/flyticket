public class newww {
    public static void main(String[] args) {
        Rectangle myRectangle;

        myRectangle = new Rectangle(5, 3, new Point(0, 0));

        System.out.println("Area of the rectangle: " + myRectangle.area());
        System.out.println("Perimeter of the rectangle: " + myRectangle.perimeter());

        Point[] corners = myRectangle.corners();
        System.out.println("Corners of the rectangle:");
        for (int i = 0; i < corners.length; i++) {
            System.out.println("Corner " + (i+1) + ": (" + corners[i].x + ", " + corners[i].y + ")");
        }
    }
}