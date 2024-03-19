public class randomString {
	static String str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz0987654321";
	static int length = 10;
	static String domain = "@domain.com";
	String random_email = "";
	static String email = "";
	static int position;
	
	public static String emailString (){
		for (int i = 0 ; i < length ; i++){
			position = (int) Math.floor(Math.random() * str.length());
			email = email + str.charAt(position);
			}
			return email;
		}
	
	public static void main(String[] args) {
		emailString();
		System.out.println(emailString().concat(domain));

	}

}
