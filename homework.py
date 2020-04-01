/* 
 Author: 孔墨
 Result: AC  Submission_id: 1731876
 Created at: Thu May 16 2019 13:14:32 GMT+0800 (CST)
 Problem_id: 2151 Time: 406 Memory: 32192
*/

#大学计算机基础实验6练习题1
def f(i,j,n):
    L=[[0 for col in range(n)]for raw in range(n)] #创建二维列表
    for i in range(0,n):
        if i%2==0:
            L[i][0]=1
        else:
            L[i][0]=2
    for j in range(0,n):
        if j%2==0:
            L[0][j]=1
        else:
            L[0][j]=2
    for i in range(1,n):
        for j in range(1,n):
            L[i][j]=L[i-1][j]+L[i][j-1]
    return L[i-1][j-1]  #运用动态规划
n=int(input())
print(f(n,n,n+1))

#关键语法为冒泡排序，将数列从小到大排列