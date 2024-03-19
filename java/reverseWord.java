public class reverseWord {

	public static void main(String[] args) {
		String str = "My name is Krishna Chandra";
		String rev = "";
		int i = 0;
		String[] arr = str.split(" ");
		for(i=arr.length -1;i>=0;i--) {
			rev = rev + arr[i] + " ";
		}
		System.out.print(rev);
	}

}
