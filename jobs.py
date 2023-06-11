def sorting_func(row):
        return row[1]
        
def nonCon(jobs, i):
    
    for j in range(i-1,0,-1):
        print(i,j)
        print(jobs[i]," ",jobs[j])
        if jobs[i][1]<=jobs[j][0]:
            print(jobs[j]," ",jobs[i])
            return j
    return -1
jobs = [(0,20,3),(10,25,7),(25,50,7),(15,60,8),(40,70,5),(50,70,5),(70,80,9),(75,90,9)]
n = len(jobs)

dp = []
jobs.sort(key=sorting_func, reverse=True)
print(jobs)

dp.insert(0, jobs[0][2])    
for i in range(1,n):
    # Calculate profit by excluding the current job.
    exc_pr = dp[i-1]
    
    # Calculate by including profit
    inc_pr = jobs[i][2]
    print(i)
    # Find index of not confliting jobs
    index = nonCon(jobs,i)
    
    if index != -1:
        inc_pr+=dp[index]
    
    dp.insert(i, max(inc_pr,exc_pr))

print(dp)
    
