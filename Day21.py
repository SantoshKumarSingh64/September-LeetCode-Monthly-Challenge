'''
Question Description :-

Car Pooling

You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the 
i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:
        Input: trips = [[2,1,5],[3,3,7]], capacity = 4
        Output: false

Example 2:
        Input: trips = [[2,1,5],[3,3,7]], capacity = 5
        Output: true

Example 3:
        Input: trips = [[2,1,5],[3,5,7]], capacity = 3
        Output: true

Example 4:
        Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
        Output: true
  

Constraints:
        trips.length <= 1000
        trips[i].length == 3
        1 <= trips[i][0] <= 100
        0 <= trips[i][1] < trips[i][2] <= 1000
        1 <= capacity <= 100000
'''
def carPooling(trips, capacity):

    ans = [0] * 1001
    starting = 1001
    end = 0
        
    for x in trips:
        starting = min(starting,x[1])
        end = max(end,x[2])
        ans[x[1]] += x[0]
        ans[x[2]] -= x[0]
    
    for x in range(1,end+1):
        ans[x] = ans[x] + ans[x-1]
    
    for x in range(starting,end+1):
        if ans[x] > capacity:
            return False
    return True

print(carPooling([[2,1,5],[3,5,7]],3))

'''
Optimal Solution :-

def carPooling(trips, capacity):
    pois = []
    for num, start, end in trips:
        pois.extend([(start, num), (end, -num)])
    num_used = 0
    for _, num in sorted(pois):
        num_used += num
        if num_used > capacity:
            return False
    return True
'''