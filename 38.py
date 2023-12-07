def count(arr, n):
    visited = [False for i in range(n)]
    count_dis=0

    for i in range(n):
        if (visited[i] == True):
          continue
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
         
        count_dis = count_dis+1;
   
    print(count_dis)

arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)
