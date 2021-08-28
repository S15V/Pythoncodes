def birthdayCakeCandles(candles):
    # Write your code here
    max = candles[0]

    for i in range(1, len(candles)):

        if candles[i] > max:
            max == candles[i]
        print(max)
        count=0
    for i in range(0,len(candles)):
        if candles[i]==max:
                count+=1
        else:
                i+=1
        return count


