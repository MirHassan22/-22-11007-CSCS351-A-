class SortedList:

    def __init__(self):

        self.sortedList = []


    def getLength(self):

        return len(self.sortedList)  

    def insertNode(self, data):

        self.sortedList.append(data)

        self.sortedList.sort()

        return self.sortedList.index(data)


    def removeLowest(self):

        if len(self.sortedList ) == 0:

            return -1

        else:

            smallest = self.sortedList[0]

            self.sortedList.remove(smallest) 

            return smallest


    def removeHighest(self):

        if len(self.sortedList) == 0:

            return -1

        else:

            highest = self.sortedList[len(self.sortedList)-1]

            self.sortedList.remove(highest)

            return highest  


    def getFirst(self):

        if len(self.sortedList) > 0:

            return self.sortedList[0]


    def getLast(self):

        if len(self.sortedList) > 0:

            return self.sortedList[len(self.sortedList) - 1]   


    def isEmpty(self):

        return len(self.sortedList) == 0
