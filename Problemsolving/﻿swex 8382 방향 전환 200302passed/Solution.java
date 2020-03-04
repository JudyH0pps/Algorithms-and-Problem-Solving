import java.util.Scanner;
import java.lang.Math;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			int a,b,c,d;
			a = sc.nextInt();
			b = sc.nextInt();
			c = sc.nextInt();
			d = sc.nextInt();
			
			a = Math.abs(c-a);
			b = Math.abs(d-b);
			int ans = Math.min(a, b) * 2;
			int line = Math.abs(a-b);
			if (line >= 0) ans += (int)(line / 2) * 4 + line % 2;
			System.out.printf("#%d %d\n",test_case,ans);
		}
		
	}

}
