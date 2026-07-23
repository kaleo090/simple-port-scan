import socket
def portscan():
    option = input("ports pre-set? (y/n): ")
    if option == "y":
        ip = input("target: ")
        ports = [80, 8080, 4444, 3389, 21, 22, 23, 24, 25, 133, 134, 135, 53, 443, 444, 445, 587, 3306, 995, 993, 5432, 5900]

        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknow"
            a = s.connect_ex((ip, port))
            if a == 0:
                print(f"\033[1;32;40m {port} | OPEN | \033[35m {service} \033[00m \033[00m")

            else:
                print(f"\033[1;31;40m {port} | CLOSED | \033[33m {service} \033[00m \033[00m")
        s.close()
    elif option == "n":
        ip = input("target: ")
        num = int(input("enter a number: ")
        for port in range(num):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknow"
            a = s.connect_ex((ip, port))
            if a == 0:
                print(f"\033[1;32;40m {port} | OPEN | \033[35m {service} \033[00m \033[00m")

            else:
                print(f"\033[1;31;40m {port} | CLOSED | \033[33m {service} \033[00m \033[00m")
        s.close()
while True:
  portscan()
