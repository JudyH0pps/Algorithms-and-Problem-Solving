import java.io.*;
import java.util.Arrays;

public class Solution {
	
	static final int INPUTMODE = 0;
	static BufferedReader br;
	static int N, X, M;
	static int[] nums;
	static int[][] ranges;
	static int maxSum;
	static int[] solarr;
	static boolean find;
	
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); 
		if (INPUTMODE == 1) br = new BufferedReader(new InputStreamReader(System.in));
		else br = new BufferedReader(new FileReader("input.txt"));
		
		int T = Integer.parseInt(br.readLine().trim());
		for (int tc = 1; tc <= T; tc++) {
			int[] input = inputline();
			N = input[0];
			X = input[1];
			M = input[2];
			
			ranges = new int[M][3];
			for (int m = 0; m < M; m++ ) ranges[m] = inputline(); 
			
			nums = new int[N];
			solarr = new int[N];
			find = false;
			maxSum = -1;
			permutation(0);
			
			bw.append("#"+tc);
			if (find) {
				for(int i=0; i<N; i++) {
					bw.append(" "+solarr[i]);
				}
			}
			else bw.append(" -1");
			bw.append("\n");
		}
		br.close();
		bw.flush();
		bw.close();
	}
	
	static void permutation(int level) {
		if (level == N) {
			if (arrchk()) {
				find = true;
//				System.out.println(Arrays.toString(nums));
			}
			return;
		}
		for (int next = 0; next <= X; next++) {
			nums[level] = next;
			permutation(level + 1);
		}
	}
	
	static boolean arrchk() {
		int[] cumul = new int[N+1];
		cumul[0] = 0;
		for (int i = 1; i <= N; i++) {
			cumul[i]= nums[i-1] + cumul[i-1];  
		}
		if (cumul[N] <= maxSum ) return false;
		
//		System.out.println(Arrays.toString(cumul));
		for (int m = 0; m < M; m++) {
			int left = ranges[m][0] - 1;
			int right = ranges[m][1];
			if (cumul[right] - cumul[left] != ranges[m][2]) return false;
		}
		maxSum = cumul[N];
		for (int i = 0; i < N ; i++) {
			solarr[i] = nums[i]; 
		}
		return true;
	}
	
	static int[] inputline() throws IOException {
		String[] input = br.readLine().trim().replace("(\r\n|\r|\n|\n\r)", "").split(" ");
		int[] tmp = new int[input.length];
		
		for (int i = 0; i < input.length ; i++) {
			tmp[i]= Integer.parseInt(input[i]); 
		}
		
		return tmp;
	}

}
