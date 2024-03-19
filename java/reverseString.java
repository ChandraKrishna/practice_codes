public class reverseString {

	public static void main(String[] args) {
		String str = "My name is Krishna Chandra";
		char ch[] = str.toCharArray();
		int i = 0;
		String rev = "";
		for(i=str.length() -1; i>=0 ; i--) {
			rev = rev + ch[i];
		}
		System.out.print("Reverse is : " +rev);
	}

}
