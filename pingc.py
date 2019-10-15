from pythonping import ping


def function1():
    t = int(input("How many servers:"))
    if t == 0:
        print("OOPPSSS.....I'm not that much smart to ping ZERO SERVER, SORRY!!!")
    elif t == 1:
        ip = input("Enter vaild IP address:")
        pong(ip, t)
    else:
        function2(t)


def function2(t):
    servers = []
    compare = []
    for x in range(t):
        un = input("Enter vaild IP address:")
        servers.insert(int(x), un)
    for i in range(t):
        response_list = ping(servers[i], size=32, count=10)
        compare.insert(int(i), response_list.rtt_avg_ms)
        print(f'{servers[i]} \t {response_list.rtt_avg_ms}')

    f = compare.index(min(compare))
    s = compare.index(max(compare))

    print(f"\nFastest server is : {servers[f]}\t{min(compare)}")
    print(f"Slowest server is : {servers[s]}\t{max(compare)}")


def pong(servers, t):
    ser = []
    err = ['[Request timed out]', 'error']
    if t == 1:
        ser.append(servers)
    response_list = ping(ser[t-1], size=9, count=1, timeout=0.4)
    if (str(response_list._responses) == err[0]):
        print("O0Opps please choose another server")
    else:
        print(ping(ser[t-1], size=32, count=10))


if __name__ == "__main__":
    function1()
