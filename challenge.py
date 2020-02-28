#Recursive sum of multi-digit numbers
def rec_dig_sum(n):
    if n < 10:
      return n
    else:
      while n >= 10:
      	n = n % 10 + rec_dig_sum(int(n/10))
      return n


#Distribution of recursive digit sums
def distr_of_rec_digit_sums(low=0, high=1500):
    dict = {i:0 for i in range(0,10)}
    for i in range(low, high + ):
      key = rec_dig_sum(i)
      dict[key] += 1
    return dict

print(distr_of_rec_digit_sums())
