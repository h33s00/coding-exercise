import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt(); //첫 줄은 수의 개수이다.
		int arr [] = new int[total]; //수의 개수만큼의 배열.
		int num = 0;
		for (int i = 0; i < total; i++) {
			num = sc.nextInt();
			arr[i] = num;
		}
		sc.close(); //입력 끝.
		bubbleSort(arr);
		for (int n : arr) {
			System.out.println(n);
		}
	}
	public static void bubbleSort(int[] A) {
		for (int k = 0; k < A.length; k++) {
			for (int j =1; j < A.length-k; j++) {
				if (A[j]<A[j-1]) {
					int temp = A[j-1];
					A[j-1] = A[j];
					A[j] = temp;
				}
			}
		}
	}	
}