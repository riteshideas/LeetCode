class UndergroundSystem:

    def __init__(self):
        self.customerInfo = {}
        self.averageTimings = {}

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Add data if not inside
        if id not in self.customerInfo:
            self.customerInfo[id] = {}

        self.customerInfo[id]["Start Station"] = stationName
        self.customerInfo[id]["Start Time"] = t

        print(self.customerInfo)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.customerInfo[id]["Exit Station"] = stationName
        self.customerInfo[id]["Exit Time"] = t

        if f'{self.customerInfo[id]["Start Station"]} {stationName}' not in self.averageTimings:
            self.averageTimings[f'{self.customerInfo[id]["Start Station"]} {stationName}'] = []

        self.averageTimings[f'{self.customerInfo[id]["Start Station"]} {stationName}'].append(t - self.customerInfo[id]["Start Time"])



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        average_time = [0,0]
        for a in self.averageTimings[f"{startStation} {endStation}"]:
            average_time[0] += a
            average_time[-1] += 1

        return average_time[0] / average_time[-1]

'''    
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
'''
