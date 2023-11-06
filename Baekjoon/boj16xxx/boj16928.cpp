#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int main(){
  int n, m;
  int ladder[101] = {0, };
  bool visit[101] = {false, };
  int ans = 1000;
  queue<pair<int, int>> q; 
  cin >> n >> m;
  for (int i = 0; i < n + m; i++){
    int u, v;
    cin >> u >> v;
    ladder[u] = v;
  }
  q.push(make_pair(1, 0));
  while (!q.empty()){
    int cur = q.front().first;
    int dist = q.front().second;
    q.pop();
    for (int i = 1; i < 7; i++){
      int nxt = cur + i;
      if (nxt > 100 || visit[nxt]){
        continue;
      }
      if (nxt == 100){
        ans = dist + 1;
        break;
      }
      if (ladder[nxt] != 0){
        q.push(make_pair(ladder[nxt], dist + 1));
        visit[nxt] = true;
        visit[ladder[nxt]] = true;
      } else{
        q.push(make_pair(nxt, dist + 1));
        visit[nxt] = true;
      }
    }
  }
  cout << ans << "\n";

  return 0;
}
