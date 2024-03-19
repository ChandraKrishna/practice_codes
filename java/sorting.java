public class sorting {
    public void performSorting() {
        int temp;
        int[] a = {10,20,30,40,50,60,40,30,20,10,5,4,3,2,1};
        System.out.println("Length : "+a.length);
        for (int j = 0 ; j < a.length ; j++) {
            for(int i = 0 ; i < a.length - 1 ; i++) {
                if(a[i] > a[i+1]) {
                    temp = a[i+1];
                    a[i+1] = a[i];
                    a[i] = temp;
                }
            }
        }
        for(int k = 0 ; k < a.length ; k++) {
            System.out.println(a[k]);
        }
    }
    public static void main(String args[]) {
        sorting obj = new sorting();
        obj.performSorting();
    }
}
