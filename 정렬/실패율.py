# #내가 푼 정답
# def solution(N, stages):
#     stay = [0] * (N+1)
#     result = []
#     for stage in stages:
#         stay[stage-1] += 1
#     for i in range(len(stay)):
#         if stay[i] == 0:
#             result.append([i+1, 0])
#         else:
#             result.append([i+1, stay[i]/sum(stay[i:])])
#     result.pop()
#     result.sort(key = lambda x : (-x[1], x[0]))
#     print([x[0] for x in result])
#
# solution(4, [4,4,4,4,4])

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key=lambda t : t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer