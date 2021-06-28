def flipImage(image):
    for i in range(len(image)):
        image[i].reverse()
        for j in range(len(image[i])):
            if image[i][j] == 0:
                image[i][j] = 1
            else:
                image[i][j] = 0
    print(image)


if __name__ == '__main__':
    a = []
    rows = int(input())
    columns = int(input())
    for x in range(rows):
        subarr = []
        for y in range(columns):
            subarr.append(int(input()))
        a.append(subarr)
    flipImage(a)
