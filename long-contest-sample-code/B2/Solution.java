import java.util.Scanner;
import java.util.Arrays;
import java.math.BigInteger;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] x = new int[n];
        int[] c = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            c[i] = sc.nextInt();
        }
        Arrays.sort(x);
        Arrays.sort(c);

        if (!(x[0] <= c[0])) {
            System.out.println(0);
        } else {
            int[] only = new int[n];
            for (int i = 0; i < n; i++) {
                only[i] = 0;
            }

            int ptr = 0;
            for (int i = 0; i < n; i++) {
                while (ptr + 1 < n && x[ptr+1] <= c[i]) {
                    ptr++;
                }
                only[ptr]++;
            }

            BigInteger ans = BigInteger.valueOf(1);
            int valid = 0;
            for (int i = n-1; i >= 0; i--) {
                valid += only[i];
                ans = ans.multiply(BigInteger.valueOf(valid));
                valid -= 1;
            }

            System.out.println(ans.toString());
        }
    }
}