package leetProb4;

import java.util.*;

public class Sort {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[] arr1 = new int[10];
		int[] arr2 = new int[10];

		int arr1len = arr1.length;
		int arr2len = arr2.length;
		for (int p = 0; p < arr1len; p++) {
			arr1[p] = scanner.nextInt();
		}
		for (int q = 0; q < arr2len; q++) {
			arr2[q] = scanner.nextInt();
		}
		int[] result = new int[arr1len + arr2len];
		System.arraycopy(arr1, 0, result, 0, arr1len);
		System.arraycopy(arr2, 0, result, arr1len, arr2len);

		System.out.println(Arrays.toString(result));
		sorting(arr1, arr1len, arr2, arr2len, result);
		median(result);
		scanner.close();
	}

	public static void sorting(int[] arr1, int arr1len, int[] arr2, int arr2len, int[] result) {

		int i = 0, j = 0, k = 0;
		while (i < arr1len && j < arr2len) {
			if (arr1[i] < arr2[j]) {
				result[k] = arr1[i];
				i++;
				k++;
			} else {
				result[k] = arr2[j];
				j++;
				k++;
			}
		}
		while (j < arr2len) {
			result[k] = arr2[j];
			j++;
			k++;
		}
		while (i < arr1len) {
			result[k] = arr1[i];
			i++;
			k++;
		}

		System.out.println(Arrays.toString(result));
	}

	public static void median(int[] result) {
		int n = result.length;
		double mean;
		System.out.println(n);
		if (n % 2 == 0) {
			mean = (double) (result[(n / 2 - 1) + 1] + result[n / 2 - 1]) / 2;
			System.out.println(mean);
		} else {
			mean = result[n / 2];
			System.out.println(mean);

		}
	}
}
