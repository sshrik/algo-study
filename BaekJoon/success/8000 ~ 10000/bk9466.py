import sys

fastio = sys.stdin.readline

NOT_VISITED = -1;
VISITED = 0;
MATCHED = 1;
NOT_MATCHED = 2;

def getCycle(start, selectResult, matched):
  stack = [start];
  cycle = [];
  
  while len(stack) > 0:
    now = stack.pop();
    next = selectResult[now];
    
    if matched[now] == MATCHED or matched[now] == NOT_MATCHED:
      return cycle, [];
    elif matched[now] == VISITED:
      cycleStart = cycle.index(now);
      return cycle[:cycleStart], cycle[cycleStart:];
    else:
      matched[now] = VISITED;
      cycle.append(now);
      stack.append(next);
  
  return cycle, [];

if __name__ == "__main__":
  T = int(fastio().strip());

  for _ in range(T):
    N = int(fastio().strip());
    
    inp = fastio().strip().split(" ");
    
    selectResult = [int(inp[i]) - 1 for i in range(N)];
    
    matched = [NOT_VISITED for _ in range(N)];
    
    for i in range(N):
      if matched[i] != NOT_VISITED:
        continue;
      
      nonCycleList, cycleList = getCycle(i, selectResult, matched);
      
      # print(i, "번째 사람의 사이클: ", nonCycleList, cycleList)
      
      for nonCycleIndex in nonCycleList:
        matched[nonCycleIndex] = NOT_MATCHED
      
      for cycleIndex in cycleList:
        matched[cycleIndex] = MATCHED;
          
    count = 0;
    
    for i in range(N):
      if matched[i] == NOT_MATCHED:
        count += 1;
        
    print(count);
  