def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
  k = int(input("Enter Number:"))
  for i in range(k+1):
    print("fib(",i,"):",fib(i))

main()
