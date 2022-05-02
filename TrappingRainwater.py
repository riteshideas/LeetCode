class SolutionV1:
    def trap(self, height: list) -> int:
        """
        0 - Air/Nothing
        1 - Solid Block
        2 - Water
        """

        rainwater = 0
        infoList = []
        dup_height = height

        # Create the 2d array
        for a in range(max(height)):
            infoList.append([])
            for b in range(len(height)):
                if dup_height[b] != 0:
                    infoList[a].append(1)
                    dup_height[b] -= 1
                else:
                    infoList[a].append(0)
        infoList.reverse()
        for f, c in enumerate(infoList):
            for d, e in enumerate(c):
                if (1 in infoList[f][d:]) and (1 in infoList[f][:d + 1]) and (e == 0):
                    infoList[f][d] = 2
                    rainwater += 1

        return rainwater



class SolutionV2:
    def trap(self, height: list) -> int:

        # Function to return rainwater collected from the small list given
        def getWaterFromHeight(SmallHeight: list) -> int:
            returnVal = 0
            SmallHeight.remove(max(SmallHeight))
            highest = max(SmallHeight)

            for i in SmallHeight:
                returnVal += highest - i

            return returnVal

        def popUnwantedValues(PopHeight: list) -> list:
            i = 0
            popVals = []
            returnHeight = PopHeight

            while True:
                if PopHeight[i] <= PopHeight[i + 1]:
                    popVals.append(i)
    
                else:
                    break

                i += 1
    
            for n, i in enumerate(popVals):
                returnHeight.pop(i - n)

            return returnHeight

        def popUnwantedValuesBack(PopHeight: list) -> list:
            while True:
                if PopHeight[-1] <= PopHeight[-2]:
                    PopHeight.pop(-1)
                elif PopHeight[-1] > PopHeight[-2]:
                    break

            return PopHeight

        def splitHeightList(HeightList: list):
            lists = []
            tempList = []
            firstVal = None

            for n, a in enumerate(HeightList):
                if firstVal == None:
                    firstVal = a

                if n == len(HeightList)-1:
                    tempList.append(a)
                    lists.append(tempList)
                    break

                elif HeightList[n+1] >= firstVal:
                    firstVal = None
                    tempList.append(a)
                    tempList.append(HeightList[n+1])
                    lists.append(tempList)
                    tempList = []

                else :
                    tempList.append(a)

            return lists

        water = 0

        if len(height) != 1:
            height = popUnwantedValues(height)
            height = popUnwantedValuesBack(height)
            MultiLists = splitHeightList(height)
            print(MultiLists)

            for i in MultiLists:
                if len(i) > 2:
                    water += getWaterFromHeight(i)

        return water


                

        


mySol = SolutionV2()
print(mySol.trap([4,2,0,3,2,5]))