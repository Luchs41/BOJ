# BOJ 1043
# 주어진 파티 중 거짓말을 할 수 있는 최대의 파티 수 구하기
# 진실을 아는 사람이 있는 파티에선 거짓말 불가, 어떤 파티에선 진실을 듣고 어떤 파티에선 거짓을 들어도 불가
# 첫 줄엔 사람 수 N과 파티 수 M, 둘째 줄엔 진실을 아는 사람 수와 그 명단, 이후로는 파티에 오는 사람 수와 명단이 주어진다. 
# 사람의 번호는 1~N까지, 진실을 아는 사람은 0~50, 파티엔 1~50명
# 뭔가 비트마스킹으로 하면 될거같은데
# 엥 그래프탐색인가?
# 진실을 미리 아는 사람들을 기준으로 BFS / DFS
# graph는 파티에 참여한 멤버가 있다면 간선이 있는 식으로 구성
# 그래프탐색으로 급선회~
def dfs(v) : 
  visitied[v] = 1
  for i in range(1, n + 1) : 
    if visitied[i] == 0 and graph[v][i] == 1 : 
      dfs(i)


n, m = map(int, input().split())
party_count = 0 # 거짓말을 한 파티의 수
graph = [[0] * (n + 1) for _ in range(n + 1)]
visitied = [0] * (n + 1)
truth_list = list(map(int, input().split()))[1:]
parties = []
# 파티 입력받기 -> graph에 간선 추가
for _ in range(m) : 
  party_list = list(map(int, input().split()))[1:]
  parties.append(party_list)
  for i in range(0, len(party_list)) : 
    for j in range(i + 1, len(party_list)) : 
      graph[party_list[i]][party_list[j]] = 1
      graph[party_list[j]][party_list[i]] = 1



for i in range(len(truth_list)) : 
  dfs(truth_list[i])
for party in parties : 
  for i in party : 
    if visitied[i] == 1 : 
      party_count -= 1
      break
  party_count += 1
print(party_count)