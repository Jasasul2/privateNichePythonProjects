from collections import Counter 

values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
valueDictionary = {}

for i in range(0, len(values)):
    valueDictionary[values[i]] = i 

print(valueDictionary)

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def printCard(self):
        print(str(self.value) + self.suit)

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.cardValues = [cards[0].value, cards[1].value, cards[2].value, cards[3].value, cards[4].value]
        self.cardValues.sort()
        self.cardSuites = [cards[0].suit, cards[1].suit, cards[2].suit, cards[3].suit, cards[4].suit]
        self.highestCard = max(self.cardValues)
        self.onePair = [False, 0]
        self.twoPairs = [False, 0, 0]
        self.threeOfAKind = [False, 0]
        self.straight = [False, 0]
        self.flush = False 
        self.fullHouse = [False, 0, 0]
        self.four = [False, 0]
        self.straightFlush = [False, 0]
        self.royalFlush = False 
        self.Initialize()

    def printCards(self):
        for card in self.cards:
            card.printCard()
        
        print("values: " + str(self.cardValues))
        print("suites: " + str(self.cardSuites))

    # Checks if all cards are straight
    def CheckStraight(self):
        if(len(self.cardValues) != len(set(self.cardValues))):
            return 

        if(self.cardValues[-1] - self.cardValues[0] == 4):
            self.straight[0] = True
            self.straight[1] = self.cardValues[-1]
            print("---------------------------------------")
            print("STRAIGHT")
            print("---------------------------------------")

    # Checks if all cards are the same suit 
    def CheckFlush(self):
        flush = self.cardSuites.count(self.cardSuites[0]) == len(self.cardSuites)
        self.flush = flush
        if(flush):
            print("---------------------------------------")
            print("FLUSH!!!") 
            print("---------------------------------------")

    # Checks royal flush 
    def CheckRoyalFlush(self):
        royalFlush = sum(self.cardValues) == 50 and self.flush
        self.royalFlush = royalFlush
    
    # Checks straight flush 
    def CheckStraightFlush(self):
        straightFlush = self.flush and self.straight[0]
        self.straightFlush[0] = straightFlush
        self.straightFlush[1] = self.straight[1]

    def CreateCounter(self):
        self.counter = Counter(self.cardValues)
        hasPair = False
        hasTriple = False 
        for key in self.counter:
            if(self.counter[key] == 4):   #FOUR 
                self.four[0] = True 
                self.four[1] == key 

            elif(self.counter[key] == 3): #TRIPLE
                hasTriple = True
                self.threeOfAKind[0] = True 
                self.threeOfAKind[1] = key 
                self.fullHouse[1] = key 
                if(hasPair):
                    self.fullHouse[0] = True 

            elif(self.counter[key] == 2): #PAIRS
                if(hasPair):
                    self.twoPairs[0] = True 
                    self.twoPairs[2] = key 

                hasPair = True 
                self.onePair[0] = True 
                self.onePair[1] = key 
                self.twoPairs[1] = key 
                self.fullHouse[2] = key 
                if(hasTriple):
                    self.fullHouse[0] = True 

    def Initialize(self):
        self.CheckStraight()
        self.CheckFlush()
        self.CheckRoyalFlush()
        self.CheckStraightFlush()
        self.CreateCounter()

    def Compare(self, otherHand):
        return self.CompareRoyalFlush(otherHand)
    
    def CompareRoyalFlush(self, otherHand):
        if(self.royalFlush and not otherHand.RoyalFlush):
            return 1 
        elif(not self.royalFlush and otherHand.royalFlush):
            return 0
        else:
            return self.CompareStraightFlush(otherHand)
    
    def CompareStraightFlush(self, otherHand):
        if(self.straightFlush[0] and not otherHand.straightFlush[0]):
            return 1 
        elif(not self.straightFlush[0] and otherHand.straightFlush[0]):
            return 0
        elif(self.straightFlush[0] and otherHand.straightFlush[0]):
            if(self.straightFlush[1] > otherHand.straightFlush[1]):
                return 1
            elif(self.straightFlush[1] < otherHand.straightFlush[1]):
                return 0
            else:
                return self.CompareFour(otherHand)
        else:
            return self.CompareFour(otherHand)

    def CompareFour(self, otherHand):
        if(self.four[0] and not otherHand.four[0]):
            return 1 
        elif(not self.four[0] and otherHand.four[0]):
            return 0
        elif(self.four[0] and otherHand.four[0]):
            if(self.four[1] > otherHand.four[1]):
                return 1
            elif(self.four[1] < otherHand.four[1]):
                return 0
            else:
                return self.CompareFullHouse(otherHand)
        else:
            return self.CompareFullHouse(otherHand)

    def CompareFullHouse(self, otherHand):
        if(self.fullHouse[0] and not otherHand.fullHouse[0]):
            return 1 
        elif(not self.fullHouse[0] and otherHand.fullHouse[0]):
            return 0
        elif(self.fullHouse[0] and otherHand.fullHouse[0]):
            if(max(self.fullHouse) > max(otherHand.fullHouse)):
                return 1
            elif(max(self.fullHouse) < max(otherHand.fullHouse)):
                return 0
            else:
                return self.CompareFlush(otherHand)
        else:
            return self.CompareFlush(otherHand)
    
    def CompareFlush(self, otherHand):
        if(self.flush and not otherHand.flush):
            return 1 
        elif(not self.flush and otherHand.flush):
            return 0
        else:
            return self.CompareStraight(otherHand)

    def CompareStraight(self, otherHand):
        if(self.straight[0] and not otherHand.straight[0]):
            return 1 
        elif(not self.straight[0] and otherHand.straight[0]):
            return 0
        elif(self.straight[0] and otherHand.straight[0]):
            if(self.straight[1] > otherHand.straight[1]):
                return 1
            elif(self.straight[1] < otherHand.straight[1]):
                return 0
            else:
                return self.CompareThree(otherHand)
        else:
            return self.CompareThree(otherHand)
    
    def CompareThree(self, otherHand):
        if(self.threeOfAKind[0] and not otherHand.threeOfAKind[0]):
            return 1 
        elif(not self.threeOfAKind[0] and otherHand.threeOfAKind[0]):
            return 0
        elif(self.threeOfAKind[0] and otherHand.threeOfAKind[0]):
            if(self.threeOfAKind[1] > otherHand.threeOfAKind[1]):
                return 1
            elif(self.threeOfAKind[1] < otherHand.threeOfAKind[1]):
                return 0
            else:
                return self.CompareTwoPairs(otherHand)
        else:
            return self.CompareTwoPairs(otherHand)

    def CompareTwoPairs(self, otherHand):
        if(self.twoPairs[0] and not otherHand.twoPairs[0]):
            return 1 
        elif(not self.twoPairs[0] and otherHand.twoPairs[0]):
            return 0
        elif(self.twoPairs[0] and otherHand.twoPairs[0]):
            if(max(self.twoPairs) > max(otherHand.twoPairs)):
                return 1
            elif(max(self.twoPairs) < max(otherHand.twoPairs)):
                return 0
            else:
                return self.ComparePair(otherHand)
        else:
            return self.ComparePair(otherHand)

    def ComparePair(self, otherHand):
        if(self.onePair[0] and not otherHand.onePair[0]):
            return 1 
        elif(not self.onePair[0] and otherHand.onePair[0]):
            return 0
        elif(self.onePair[0] and otherHand.onePair[0]):
            if(self.onePair[1] > otherHand.onePair[1]):
                return 1
            elif(self.onePair[1] < otherHand.onePair[1]):
                return 0
            else:
                return self.CompareHighestCard(otherHand, 0)
        else:
            return self.CompareHighestCard(otherHand, 0)

    def CompareHighestCard(self, otherHand, deleter):
        self.highestCard = max(self.cardValues[0 : len(self.cardValues) - deleter])
        otherHand.highestCard = max(otherHand.cardValues[0 : len(otherHand.cardValues) - deleter])
        if(self.highestCard > otherHand.highestCard):
            return 1 
        elif(self.highestCard < otherHand.highestCard):
            return 0
        else:
            return self.CompareHighestCard(otherHand, deleter + 1)

with open("poker.txt", "r", encoding = "utf-8") as file:
    content = file.read()
    handPairs = content.splitlines()
    player1Wins = 0
    print("Started")
    x = 0
    for handPair in handPairs:
        pairs = handPair.split()
        cardlist = []
        for pair in pairs:
            newCard = Card(valueDictionary[pair[0]], pair[1])
            cardlist.append(newCard)

        hand1 = Hand(cardlist[0:5])
        hand2 = Hand(cardlist[5:])

        placeholder = player1Wins
        player1Wins += hand1.Compare(hand2)
        if(player1Wins > placeholder):
            print("P1 WON")
        else:
            print("P2 WON")

        hand1.printCards()
        print("****")
        hand2.printCards()
        print(".....")
        print("-----")

    print("................")
    print(player1Wins)



