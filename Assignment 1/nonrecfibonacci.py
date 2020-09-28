def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1] 
    fibs = [0, 1]
    for i in range(1, n):
      k = fibs[-1] + fibs[-2]
      fibs.append(k)
    return fibs

def main():
  k = int(input("Enter Number:"))
  print(fib(k))

main()
