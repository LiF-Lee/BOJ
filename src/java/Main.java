import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] cnt = new int[100001];
        int N = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(br.readLine());
            cnt[a]++;
        }

        for (int i = 0; i < 100001; i++) {
            if (cnt[i] > 0) {
                for (int j = 0; j < cnt[i]; j++) {
                    bw.write(i + "\n");
                }
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}