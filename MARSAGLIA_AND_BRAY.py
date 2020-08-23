import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statistics
import Q1_Wichmann_Hill
import time

WH = Q1_Wichmann_Hill.Uniform()

class marsaglia_bray:
    def __init__(self, value):
        self.samples = []
        self.samplesize = value
        self.start_time = time.time()

    def SampleRandomVariables(self):
        for i in range(self.samplesize):


            prob = WH.Generate()

            # u1 = random.uniform(0, 1)
            # u2 = random.uniform(0, 1)
            # u3 = random.uniform(0, 1)

            u1 = WH.Generate()
            u2 = WH.Generate()
            u3 = WH.Generate()

            # print("Random float number is ", prob)
            # print("Random float number is ", u1)
            # print("Random float number is ", u2)
            # print("Random float number is ", u3)

            def g(temp):
                if (abs(temp) < 1.0):
                    return 17.49731196 * math.exp(-0.5 * pow(temp, 2)) - 4.73570326 * (
                                3 - pow(temp, 2)) - 2.15787544 * (
                                   1.5 - abs(temp))
                elif (abs(temp) < 1.0 and abs(temp) < 1.5):
                    return 17.49731196 * math.exp(-0.5 * pow(temp, 2)) - 4.73570326 * (
                                3 - pow(temp, 2)) - 2.15787544 * (
                                   1.5 - abs(temp))
                elif (abs(temp) < 1.5 and abs(temp) < 3.0):
                    return 17.49731196 * math.exp(-0.5 * pow(temp, 2)) - 4.73570326 * (3 - pow(temp, 2))
                elif (abs(temp) <= 3.0):
                    return 0

            if (prob < 0.8638):
                X = 2.0 * (u1 + u2 + u3 - 1.5)
            elif (prob < 0.9745):
                X = 1.5 * (u1 + u2 - 1)
            elif (prob < 0.9973002039):
                while True:
                    x = 6 * u1 - 3
                    y = 0.358 * u2
                    if (y < g(x)):
                        break
                    # u1 = random.uniform(0, 1)
                    # u2 = random.uniform(0, 1)
                    u1 = WH.Generate()
                    u2 = WH.Generate()
            elif (prob < 1):
                while True:
                    # v1 = random.uniform(-1, 1)
                    # v2 = random.uniform(-1, 1)
                    v1 = WH.UniformRange()
                    v2 = WH.UniformRange()

                    x = v1 * ((9 - 2 * math.log(v1 ** 2 + v2 ** 2)) / (v1 ** 2 + v2 ** 2)) ** 0.5
                    y = v2 * ((9 - 2 * math.log(v1 ** 2 + v2 ** 2)) / (v1 ** 2 + v2 ** 2)) ** 0.5

                    if (x > 3 or y > 3):
                        if (x > 3):
                            X = x
                        else:
                            X = y
                        break
            self.samples.append(X)

    def GetSample(self):
        return self.samples

    def setSampleSize(self, value):
        self.samplesize = value

    def printPDF(self):
        plt.hist(self.samples, bins=50, density=True, edgecolor='black', linewidth=1)
        plt.show()

        print("--- %s seconds ---" % (time.time() - self.start_time))

    def getMean(self):
        return statistics.mean(self.samples)

    def getStandardDeviation(self):
        return statistics.stdev(self.samples)



test = marsaglia_bray(1000000)
test.SampleRandomVariables()
print(test.getMean())
print(test.getStandardDeviation())
print(test.getStandardDeviation()**2)
test.printPDF()



