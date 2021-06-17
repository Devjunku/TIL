import java.io.*;
import java.util.StringTokenizer;

public class ArrayLoopDemo {
  static int[] dn = {-1, 1, 0, 0, 0, 0};
  static int[] dm = {0, 0, -1, 1, 0, 0};
  static int[] dh = {0, 0, 0, 0, -1, 1};

  static int N, M, H, D, max_result;
  static int[][][] ground;
  static int[][][] rec;
  static int[][][] visited;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int T = Integer.parseInt(br.readLine());
    for (int t=1; t<=T; t++) {
      st = new StringTokenizer(br.readLine());
      N = Integer.parseInt(st.nextToken());
      M = Integer.parseInt(st.nextToken());
      H = Integer.parseInt(st.nextToken());

      D = Integer.parseInt(br.readLine());

      ground = new int[H][N][M];

      for (int i = 0; i < H; i++) {
        for (int j = 0; j < N; i++) {
          st = new StringTokenizer(br.readLine());
          for (int k = 0; k < M; k++) {
            ground[i][j][k] = Integer.parseInt(st.nextToken());
          }
        }
      }

      rec = new int[H][N][M];
      for (int i = 0; i < H; i++) {
        for (int j = 0; j < N; j++) {
          for (int k = 0; k < N; k++) {
            rec[i][j][k] = 0;
          }
        }
      }

      max_result = -1;

      for(int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          visited = new int[H][N][M];

          for (int l = 0; l < H; l++) {
            for (int m = 0; m < N; m++) {
              for (int n = 0; n < m; n++) {
                visited[l][m][n] = 0;
              }
            }
          }
          rec[0][i][j] = D -ground[0][i][j];
          visited[0][i][j] = 1;

          dfs(0, i, j, D-ground[0][i][j]);
        }
      }
      System.out.println("#"+t+" "+max_result);
    }
  }
  public static void dfs(int h, int i, int j, int d) {
    if (d <= max_result)
      return;
    
    for(int k = 0; k < 6; k++) {
      int nh = h + dh[k];
      int nn = i + dn[k];
      int nm = j + dm[k];
      if (0 <= nh && nh < H && 0 <= nn && nn < N && 0 <= nm && nm < M && visited[nh][nn][nm] == 0) {
        if (d >= ground[nh][nn][nm] && rec[nh][nn][nm] <= d - ground[nh][nn][nm]) {
          rec[nh][nn][nm] = d - ground[nh][nn][nm];

          if (ground[nh][nn][nm] == 0 && max_result < rec[nh][nn][nm]) {
            max_result = rec[nh][nn][nm];
            return;
          }
          
          visited[nh][nn][nm] = 1;
          dfs(nh, nn, nm, d - ground[nh][nn][nm]);
          visited[nh][nn][nm] = 0;
        }
      }
    }
  }
}