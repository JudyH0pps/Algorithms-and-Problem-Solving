import java.io.*;

public class Solution {
	
	static final int MODE = 1;
	static int N, Q;
	static BufferedReader br;
	static int[] diskHall;
	static int hallptr;
	static int[] disk;

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		if (MODE == 0) br = new BufferedReader(new InputStreamReader(System.in));
		else br = new BufferedReader(new FileReader("input.txt"));
		
		String[] input;
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			input = inputline();
			N = Integer.parseInt(input[0]);
			Q = Integer.parseInt(input[1]);
			diskHall = new int[N];
			disk = new int[Q];
			
			input = inputline();
			diskHall[0] = Integer.parseInt(input[0]);
			for (int i = 1; i < N ; i++) {
				diskHall[i] = Math.min(Integer.parseInt(input[i]), diskHall[i-1]);
			}
			input = inputline();
			for (int i = 0; i < Q ; i++) {
				disk[i] = Integer.parseInt(input[i]);
			}
			
			System.out.printf("#%d %d\n", tc, stacking());	
		}
	}
	
	static int stacking() {
//		System.out.println(Arrays.toString(diskHall));
//		System.out.println(Arrays.toString(disk));
		boolean ok = false;
		hallptr = N;
		for(int q = 0; q < Q; q++ ) {
			int nowdisk = disk[q];
			if (hallptr == 0) return 0;
			ok = false;
			for(int h = hallptr-1; h >= 0; h-- ) {
				if (diskHall[h] >= nowdisk) {
					hallptr = h;
					ok = true;
					break;
				}
			}
			if (!ok) return 0; 
		}
		return hallptr + 1;
	}
	
	static String[] inputline() throws IOException{
		String[] tmp = br.readLine().trim().replace("(\n|\n\r|\r|\r\n)", "").split(" ");
		return tmp;
	}
}
