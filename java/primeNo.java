public class primeNo {

	public static void main(String[] args) {
		int i = 57;
		int d = 2;
		int c = 0;
		int f = 0;
		for(c=d;c<i;c++) {
			if(i%c==0) {
				f = 1;
				break;
			}
		}
		if(f==1) {
			System.out.print("No is Not Prime");
		}else System.out.print("No is Prime");
	}

}
