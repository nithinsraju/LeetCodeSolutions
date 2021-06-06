def defangIPaddr(address: str) -> str:
    print(address)
    deIP = ""
    for i in range(len(address)):
        if address[i] == ".":
            deIP += "["
            deIP += "."
            deIP += "]"
        else:
            deIP += address[i]
    return deIP


if __name__ == '__main__':
    ip = str(input())
    print(defangIPaddr(ip))
