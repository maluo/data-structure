public class Solution {
	public static void main(String[] args) {
		String in = "ddddaaaabbbccccdddaabbccddfffFfff";
		StringBuilder sb = new StringBuilder(1024);

		for (int i = 0; i < in.length() - 2; ){
			if (in.charAt(i) == in.charAt(i+1) &&  in.charAt(i+1) == in.charAt(i+2)){
				sb.append(Character.toUpperCase(in.charAt(i)));
				i += 3;
			}else{
				sb.append(in.charAt(i));
				i += 1;
			}
		}
		System.out.println(sb.toString());
	}
}
