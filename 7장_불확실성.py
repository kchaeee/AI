# 7장_불확실성

# 몬티홀 문제
import random

NGames=10000
UnchangeGame=[]
ChangeGame=[]

for i in range(0, NGames):
    # 자동차는 랜덤하게 숨겨진다.
    CarDoor=random.choice(["Door1", "Door2", "Door3])

    # 사용자가 첫 번째 선택을 한다.
    UseDoor=random.choice(["Door1", "Door2", "Door3])

    # 호스트가 자동차가 있지 않은 문을 연다.
    OpenDoor=list(set(["Door1", "Door2", "Door3])-set([UseDoor, CarDoor]))[0]

    # 남아 있는 문을 결정한다.
    OpenDoor=list(set(["Door1", "Door2", "Door3])-set([UseDoor, OpenDoor]))[0]
                       
    # 사용자가 선택을 바꾸지 않아서 성공하면 True를 리스트에 추가한다. True는 정수 1이다.
    UnchangeGame.append(UseDoor=CarDoor)
                       
    # 사용자가 선택을 바꾸어서 성공하면 True를 리스트에 추가한다. True는 정수 1이다.
    ChangeGame.append(OtherDoor=CarDoor)

# 각 리스트에서 정수 1의 개수를 센다.
print(f"{NGames} 개의 게임 중에서 바꾸지 않았을 때의 승률: {sum(UnchangeGame)/NGames} \n\
    바꾸었을 때의 승률: {sum(ChangeGame)/NGames}")

# 확신도 실습
IF (E1 AND E2 AND E3) OR (E4 AND NOT E5)
THEN H
E = max(min(E1, E2, E3), min(E4, -E5))
E = max(min(0.8, 0.9, 0.1), min(-0.4,-(-0.5))
  = max(0.1, -0.4)
  = 0.1
IF (E1 AND E2 AND E3) OR (E4 AND NOT E5)
THEN H
cf(H, e) = cf(E, e) x cf(H, E)
         = 0.1 x 0.7 = 0.07
                                       
