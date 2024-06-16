# 2장_탐색

# 깊이 우선 탐색
function DFS(root)
    open <- [root]
    closed <-[root]
    while open =/ []do
    x <- open #리스트의 첫 번째 요소
    if X == goal then return SUCCESS
    else
        X의 자식 노드를 생성한다.
        X를 closed 리스트에 추가한다.
        X의 자식 노드가 이미 open이나 closed에 있다면 버린다.
        남은 자식 노드들은 open의 처음에 추가한다. (스택처럼 사용)
    return FAIL


# 너비 우선 탐색
function BFS(root)
    open <- [root]
    closed <-[root]
    while open =/ []do
    x <- open #리스트의 첫 번째 요소
    if X == goal then return SUCCESS
    else
        X의 자식 노드를 생성한다.
        X를 closed 리스트에 추가한다.
        X의 자식 노드가 이미 open이나 closed에 있다면 버린다.
        남은 자식 노드들은 open의 끝에 추가한다. (스택처럼 사용)
    return FAIL

# 깊이 제한 탐색
function IDDFS(root)
    for depth from 0 to do
    found, remaining <- DFS(root, depth)
    if found =/ null then
        return found
    else if not remaining then
        return NULL

# 언덕 등반 기법
function HILL_CLIMBING(root)
    current <- root
    loop do
        # 현재 노드의 자식 노드들을 생성한다.
        neighbor <- 평가 함수값이 가장 높은 자식 노드
        # 만일 모든 위치가 현 위치보다 낮다면 그 곳을 정상이라고 판단한다.
        if VALUE(neighbor)<=VALUE(current) then
            return current
        # 현 위치가 정상이 아니라면 확인된 위치 중 가장 높은 곳으로 이동한다.
        current <- neighbor

# 최고 우선 탐색
function BEST_FIRST(root)
    open <- []
    closed <-[]
    while open =/ []do
    x <- open #리스트에서 가장 평가 함수의 값이 좋은 노드 
    if X == goal then return SUCCESS
    else
        X의 자식 노드를 생성한다.
        X를 closed 리스트에 추가한다.
        if X의 자식 노드가 이미 open이나 closed에 있지 않으면
            자식 노드들의 평가 함수값을 계산한다.
            자식 노드들을 open 리스트에 추가한다. 
    return FAIL

# A* 알고리즘
function ASTAR(root)
    open <- [root]
    closed <-[]
    while open =/ []do
    x <- open #리스트에서 가장 평가 함수의 값이 좋은 노드 
    if X == goal then return SUCCESS
    else
        X의 자식 노드를 생성한다.
        X를 closed 리스트에 추가한다.
        if X의 자식 노드가 이미 open이나 closed에 있지 않으면
            자식 노드의 평가 함수값 f(n) = g(n) + h(n)을 계산한다.
            자식 노드들을 open 리스트에 추가한다. 
    return FAIL
