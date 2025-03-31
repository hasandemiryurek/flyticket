public class Date {
    private int day;
    private int month;
    private int year;

    public Date(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public void incrementMonth() {
        if (month < 12) {
            month++;
        } else {
            month = 1;
            year++;
        }
    }

    @Override
    public String toString() {
        return String.format("%02d/%02d/%04d", day, month, year);
    }

    // main function is optional
    public static void main(String[] args) {
        Date date = new Date(28, 2, 2024);
        date.incrementMonth();
        System.out.println(date.toString()); // Output: 28/03/2024
    }
}
