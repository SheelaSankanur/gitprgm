def max_profit(prices):
    n=len(prices)
    max_profit=0
    for i in range(n-1):
        for j in range(i+1,n):
            profit=prices[j]-prices[i]
            max_profit=max(max_profit,profit)
    return max_profit
if __name__=="__main__":
    prices=[7,10,1,3,6,9,2]
    print("max profit:", max_profit(prices))  # Output: 8
