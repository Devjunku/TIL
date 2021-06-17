import java.io.*;
import java.util.StringTokenizer;

public class solution {

    static int[] dn = {-1, 1, 0, 0, 0, 0};
    // 세로
    static int[] dm = {0, 0, -1, 1, 0, 0};
    // 가로
    static int[] dh = {0, 0, 0, 0, -1, 1};
    // 높이
    static int N, M, H, D, max_result;
    // 주어질 맵의 세로, 가로, 높이, 드릴의 내구성, 나올 결과값
    static int[][][] ground;
    // 주어질 맵
    static int[][][] rec;
    // 진행해 가며 그 위치의 최대 드릴 내구도 상태를 기록할 리스트
    static int[][][] visited;
    // 방문 배열

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int t=1;t<=T;t++){
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());

            D = Integer.parseInt(br.readLine());

            ground = new int[H][N][M];
            // 매 테스트케이스마다 맵 초기화
            for(int i = 0; i < H; i++) {
                for (int j = 0; j < N; j++) {
                    st = new StringTokenizer(br.readLine());
                    for (int k = 0; k < M; k++) {
                        ground[i][j][k] = Integer.parseInt(st.nextToken());
                        // 땅의 내구도 입력
                    }
                }
            }
            rec = new int[H][N][M];
            for(int i = 0; i < H; i++) {
                for (int j = 0; j < N; j++) {
                    for (int k = 0; k < M; k++) {
                        rec[i][j][k] = 0;
                        // 기록할 최적의 내구도 배열 초기화
                    }
                }
            }
            max_result = -1;
            // 보물을 못찾았을 때를 대비해서 -1로 초기화
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < M; j++) {
                    // 맨 위층을 탐색하며 드릴에 가장 적은 충격을 줄 위치를 찾음.
                    visited = new int[H][N][M];
                    // 매번 방문 리스트 탐색
                    for(int l = 0; l < H; l++) {
                        for (int m = 0; m < N; m++) {
                            for (int n = 0; n < M; n++) {
                                visited[l][m][n] = 0;
                            }
                        }
                    }
                    rec[0][i][j] = D - ground[0][i][j];
                    // 현재 가장 윗층을 뚫을 때 드릴의 내구도 감소
                    visited[0][i][j] = 1;
                    // 출발 지점을 다신 방문하지 못하게 방문표시
                    dfs(0, i, j, D-ground[0][i][j]);
                    // dfs로 탐색하며 내구도를 가장 크게 만들 수 있도록 보물 찾기 시작.
                }
            }
            System.out.println("#"+t+" "+max_result);
            // 매 테스트 케이스 값 출력
        }

    } // end of main

    public static void dfs(int h, int i, int j, int d) {
        if (d <= max_result)
            return;
        // 만약 현재 내구도가 최적의 결과보다 작아진다면 바로 return
        for(int k = 0; k < 6; k++) {
            // 상하좌우전후 6방향 탐색
            int nh = h + dh[k];
            int nn = i + dn[k];
            int nm = j + dm[k];
            // 높이, 세로, 가로 델타 이동
            if (0 <= nh && nh < H && 0 <= nn && nn < N && 0 <= nm && nm < M && visited[nh][nn][nm] == 0) {
                // 현재 정해진 범위에 방문하지 않은 좌표라면
                if (d >= ground[nh][nn][nm] && rec[nh][nn][nm] <= d - ground[nh][nn][nm]) {
                    // 현재 드릴 내구도가 벽을 뚫고 나서 양수 값이어야 하고, 현재 위치의 최적의 드릴 내구도보다 더 최적의 값이라면,
                    rec[nh][nn][nm] = d - ground[nh][nn][nm];
                    // 최적의 드릴 내구도를 갱신해줌
                    if (ground[nh][nn][nm] == 0 && max_result < rec[nh][nn][nm]) {
                        // 만약 보물을 찾았고, 결과값보다 더 최적의 값을 찾았다면
                        max_result = rec[nh][nn][nm];
                        // 값을 갱신
                        return;
                    }
                    visited[nh][nn][nm] = 1;
                    // 방문 체크를 하고
                    dfs(nh, nn, nm, d - ground[nh][nn][nm]);
                    // dfs를 통해 다음 길로 향하고
                    visited[nh][nn][nm] = 0;
                    // 방문이 이미 끝났던 경로는 이후 다시 방문할 수 있도록 방문 체크를 해제해줌.
                }
            }
        }
    }

}