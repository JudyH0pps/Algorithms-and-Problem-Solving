import java.util.Scanner;

public class cycle {
	static int minL;
	static int N;
	static int[][] graph;
	static boolean[] visit;
	
	static void DFS(int startnode, int node, int score) {
		
		for (int nextnode = 0 ; nextnode < N ; nextnode ++) {
			int W = graph[node][nextnode];
			if (W > 0 && score + W < minL) {
				if (visit[nextnode]) {
					if (startnode == nextnode) {
						minL = score + W;
					}
					continue;
				}
				
				visit[nextnode] = true;
				DFS(startnode, nextnode, score + W);
				visit[nextnode] = false;	
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++ ) {
			N = sc.nextInt();
			int M = sc.nextInt();
			graph = new int[N][N];
			
			for (int i = 0; i < M; i ++) {
				int s, e, c;
				s = sc.nextInt();
				e = sc.nextInt();
				c = sc.nextInt();
				graph[s - 1][e - 1] = c;
			}
			
			visit = new boolean[N];
			minL = 10000 * M;
			
			for (int node = 0; node < N; node++ ) {
				visit[node] = true;
				DFS(node,node,0);
				visit[node] = false;
			}
			
			System.out.println("#"+t+" "+minL);
		}
	}
}
