import java.util.*;

public class treeTravel {
	static int[] inorder;
	static int[] postorder;

	static void recur(int instart,int poststart,int length) {
		if (length < 1) return;
		
//		System.out.printf("go %d %d %d\n",instart,poststart,length);
		
		int node = postorder[poststart + length - 1];
		System.out.printf("%d ",node);
		int pivot = 0;
		for (int i = instart; i < instart + length ; i++ ) {
			if (inorder[i] == node) {
				pivot = i;
				break;
			}
		}
		
		recur(instart, poststart, pivot - instart);
		recur(pivot + 1, poststart + pivot - instart, length - pivot + instart - 1);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		inorder = new int[n];
		postorder = new int[n];

		for (int i = 0; i < n; i++)
			inorder[i] = sc.nextInt();
		for (int i = 0; i < n; i++)
			postorder[i] = sc.nextInt();
		
		recur(0,0,n);
	}
}
