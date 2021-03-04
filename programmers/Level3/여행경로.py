def solution(tickets):
    tickets.sort(reverse = True)
    print(tickets)
    routes = {}
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    
    print(routes)

    st = ['ICN']
    ans = []

    while st:
        top = st[-1]
        # print('top', top)
        if top not in routes or len(routes[top]) == 0:
            ans.append(st.pop())
            # print('ans', ans)
        else:
            st.append(routes[top].pop())
            # print('st',st)
    ans.reverse()
    # return ans

    



if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))