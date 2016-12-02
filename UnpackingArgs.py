def cal(age, area, values):
    answers = (100-age)-(area*3.5)-(values*2)
    print(answers)

    rohanData = [27, 28, 6]

    cal(rohanData[0], rohanData[1], rohanData[2])
    cal(*rohanData)