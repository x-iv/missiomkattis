def candle(days):
    total_candles = (days/2) * (2 * 1 + (days -1) * 1)

    total_candles += days

    return int(total_candles)

#number of data sets
num_data = int(input())

#process each data set
for _ in range(1, num_data + 1):
    dataset_num, days = map(int, input().split())

    total_candles = candle(days)

    print(f"{dataset_num} {total_candles}")
