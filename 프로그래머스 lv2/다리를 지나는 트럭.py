bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# return    8

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while bridge:   # 다리를 다 건널때까지
        time += 1
        bridge.pop(0)   # 이미 다리 위에 있는 트럭들 전진

        if truck_weights:   # 대기중인 트럭이 있을 때
            if truck_weights[0] + sum(bridge) <= weight:    # 무게 체크 후 안걸리면
                truck = truck_weights.pop(0)    # 대기중인 맨 앞트럭을
                bridge.append(truck)            # 다리 맨뒤에 투입
            else:   # 트럭이 다리 무게에 걸리면
                bridge.append(0)    # 다리에 있는 트럭들만 전진

    return time




