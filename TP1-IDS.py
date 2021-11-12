import random


class State:
    size = 2
    initial_state = []
    final_state = []
    next_states = []
    visited_states = []
    max_visited_states=1
    #Max depth is the total number of solutions
    maxDepth=0

    def taquin_ids(self):
        self.setSize()
        self.setMaxDepth()
        self.final_state = self.setFinalState()
        self.initial_state = [3, 1, 2, 4, 5, " ", 6, 7, 8]
        for limit in range(1,self.maxDepth+1):
            print('iteration:', limit)
            self.visited_states=[]
            self.next_states=[]
            if(self.dfs(limit)):
                return True
        print('not found')


    def dfs(self, limit):
        #we need a compteur because we don't want to modify the number "max_visited_states"
        compteur=self.max_visited_states
        self.next_states.append(self.initial_state)
        #While compteur!=0 means that we haven't set yet the next states of the states we got in the previous call
        while(self.next_states and compteur!=0):
            state=self.next_states.pop()
            self.affiche(state)
            if state == self.final_state:
                print(len(self.visited_states))
                print('found after',limit,'iterations.')
                return True
            elif state not in self.visited_states:
                self.visited_states.append(state)
                self.setNextStates(state)   
            # Set the number of times we need to call setNextStates in the next iteration
            # which is equal to the max length we got of the next_states list 
                self.max_visited_states=max(self.max_visited_states,len(self.next_states))+1 #+1 because self.next_states missing the popped value
            #  With each handled state (calculate it's nexts) we decrement the counter until we got 0 
                compteur-=1
        return False



    def display(self, list):
        for e in list:
            print(e, end=' ')
        print()


    def affiche(self, state):
        matrix = [ state[i:i+self.size] for i in range(0,len(state),self.size) ]
        for l in matrix:
            self.display(l)
        print('\n')
    

    def factorial(self, n):
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact
    
    def setMaxDepth(self):
        self.maxDepth=self.factorial(self.size**2)//2

    def setSize(self):
        self.size = int(input("Write the size of the square: "))

    def sefInitialState(self):
        self.initial_state.append(" ")
        for x in range(self.size ** 2 - 1):
            self.initial_state.append(x + 1)
        random.shuffle(self.initial_state)
        return self.initial_state

    def setFinalState(self):
        self.final_state.append(" ")
        for x in range(self.size ** 2 - 1):
            self.final_state.append(x + 1)
        return self.final_state

    def getFreeSpot(self, current_state):
        i = 0
        for spot in current_state:
            if spot == " ":
                return i
            i += 1

    def translationFunction(self, state, direction):
        # To obtain mutability
        copy_state = state.copy()
        freePosition = self.getFreeSpot(copy_state)
        if direction == "u":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition - self.size]
            # Setting the upper case to ' '
            copy_state[freePosition - self.size] = " "
            # Seetting the free spot to the value of the upper case
            copy_state[freePosition] = changingValue
            return copy_state

        if direction == "d":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition + self.size]
            # Setting the bottom case to ' '
            copy_state[freePosition + self.size] = " "
            # Seetting the free spot to the value of the bottom case
            copy_state[freePosition] = changingValue
            return copy_state

        if direction == "l":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition - 1]
            # Setting the left case to ' '
            copy_state[freePosition - 1] = " "
            # Seetting the free spot to the value of the left case
            copy_state[freePosition] = changingValue
            return copy_state

        if direction == "r":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition + 1]
            # Setting the right case to ' '
            copy_state[freePosition + 1] = " "
            # Seetting the free spot to the value of the right case
            copy_state[freePosition] = changingValue
            return copy_state


    def setNextStates(self, current_state):
        freeSpotIndex = self.getFreeSpot(current_state)
        # If the free spot is on the upper ligne
        if freeSpotIndex < self.size:
            # If the empty spot is the upper left corner
            if freeSpotIndex == 0:
                self.next_states.append(self.translationFunction(current_state, "d"))
                self.next_states.append(self.translationFunction(current_state, "r"))
            # If the empty spot is the upper right corner
            elif freeSpotIndex == self.size - 1:
                self.next_states.append(self.translationFunction(current_state, "d"))
                self.next_states.append(self.translationFunction(current_state, "l"))
            else:
                self.next_states.append(self.translationFunction(current_state, "l"))
                self.next_states.append(self.translationFunction(current_state, "d"))
                self.next_states.append(self.translationFunction(current_state, "r"))

        # If the free spot is on the bottom ligne
        elif freeSpotIndex > self.size ** 2 - self.size - 1:
            # If the empty spot is the bottom right corner
            if freeSpotIndex == self.size ** 2 - 1:
                self.next_states.append(self.translationFunction(current_state, "l"))
                self.next_states.append(self.translationFunction(current_state, "u"))
            # If the empty spot is the bottom left corner
            elif freeSpotIndex == self.size ** 2 - self.size:
                self.next_states.append(self.translationFunction(current_state, "r"))
                self.next_states.append(self.translationFunction(current_state, "u"))
            else:
                self.next_states.append(self.translationFunction(current_state, "r"))
                self.next_states.append(self.translationFunction(current_state, "l"))
                self.next_states.append(self.translationFunction(current_state, "u"))

        # If the free spot is on the left border but not in the corners
        elif freeSpotIndex % self.size == 0:
            self.next_states.append(self.translationFunction(current_state, "d"))
            self.next_states.append(self.translationFunction(current_state, "r"))
            self.next_states.append(self.translationFunction(current_state, "u"))

        # If the free spot is on the right border (the corners case is treated above)
        elif freeSpotIndex % self.size == 2:
            self.next_states.append(self.translationFunction(current_state, "d"))
            self.next_states.append(self.translationFunction(current_state, "l"))
            self.next_states.append(self.translationFunction(current_state, "u"))

        # If the free spot is not on any border
        else:
            self.next_states.append(self.translationFunction(current_state, "d"))
            self.next_states.append(self.translationFunction(current_state, "u"))
            self.next_states.append(self.translationFunction(current_state, "r"))
            self.next_states.append(self.translationFunction(current_state, "l"))


state = State()
state.taquin_ids()
