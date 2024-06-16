# 3장_트리

# 미니맥스 알고리즘
function minimax(node, depth, maxPlayer)
    if depth == 0 or node가 단말 노드 then
        return node의 휴리스틱값
    if maxPlayter then # 최대화 노드
        value
        for each child of node no
            value <- max(value, mminimax(child, depth-1, FALSE))
        return value
    else
        value
        for each child of node do
            value <- min(value, minimax(child,depth-1, TRUE))
        return value


# 알파베타 알고리즘
function alphabeta(node, depth,a, b, maxPlayer)
    if depth == 0 or node가 단말 노드 then
        return node의 휴리스틱값
    if maxPlayter then # 최대화 노드
        value
        for each child of node no
            value <- max(value, mminimax(child, depth-1, a, b, FALSE))
        a <- max(a, value)
        if a>=b then
            break
        return value
    else
        value
        for each child of node do
            value <- min(value, minimax(child,depth-1, a, b, TRUE))
        b <- min(b, value)
        if a>=b then
            break
        return value
