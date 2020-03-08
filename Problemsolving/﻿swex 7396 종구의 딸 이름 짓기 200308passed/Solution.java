import java.io.*;
import java.util.*;

public class Solution {
	static int N, M;
	static char ans[];
	static char[][] board;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++ ) {
			String[] tmp = br.readLine().split(" ");
			N = Integer.parseInt(tmp[0]);
			M = Integer.parseInt(tmp[1]);
			board = new char[N][M];
			ans = new char[N+M-1];
			for (int i=0; i < N; i++ ) {
				board[i] = br.readLine().toCharArray();
			}
			bfs();
			
			bw.append("#"+tc+" ");
			for (int i=0; i < ans.length ; i++) {
				bw.append(ans[i]);
			}
			bw.append("\n");
		}
		br.close();
		bw.flush();
		bw.close();
	}
	
	public static void bfs() {
		int[] dc = {0,1};
		int[] dr = {1,0};
		boolean[][] visit = new boolean[N][M];
		
		Queue<P> q = new LinkedList<>();
		q.add(new P(0,0,board[0][0]));
		ans[0] = board[0][0];
		if ((N - 1 == 0) && (M - 1 == 0)) return;
		int idx = 0;
		
		while(!q.isEmpty()) {
			int fornext = q.size(); 
			char minChar = 'z';
		
			for(int i=0; i<fornext; i++) {
				P now = q.poll();
				if (now.a != ans[idx]) continue;
//				System.out.println(now.r +" " + now.c + " " + now.a +" vs "+ans[idx]);
				for(int d = 0; d < 2; d++ ) {
					int nr = now.r + dr[d];
					int nc = now.c + dc[d];
					if (0 <= nr && nr < N && 0 <= nc && nc < M && !visit[nr][nc] && minChar >= board[nr][nc]) {
						if (minChar > board[nr][nc]) {
							minChar = board[nr][nc];
						}
						if (nr == N - 1 && nc == M - 1) {
							ans[++idx] = board[nr][nc];
							return;
						}
						visit[nr][nc] = true;
						q.add(new P(nr,nc,board[nr][nc]));
					}
				}
			}
			ans[++idx] = minChar;
//			System.out.println(Arrays.toString(ans));
		}
	}
	
	public static class P{
		int r,c;
		char a;
		P(int r, int c, char a){
			this.r = r;
			this.c = c;
			this.a = a;
		}
	}

}
