#passenger class
class Passenger:
    def __init__(self, passengerName):
        self.passengerName = passengerName

    def setPassengerName(self, passengerName):
        self.passengerName = passengerName
    
    def getPassengerName(self):
        return self.passengerName
    
    def updatePassengerDetails(self):
        #update passenger's name
        pass
    
#flight class
class Flight:
    def __init__(self, flightNumber, departureTime, arrivalTime, departureLocation, arrivalLocation, date, boardingTill, type):
        self.flightNumber = flightNumber
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.departureLocation = departureLocation
        self.arrivalLocation = arrivalLocation
        self.date = date
        self.boardingTill = boardingTill
        self. type = type

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def getFlightNumber(self):
        return self.flightNumber
    
    def setDepartureTime(self, departureTime):
        self.departureTime = departureTime 

    def getDepartureTime(self):
        return self.departureTime
    
    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date
    
    def setBoardingTill(self, boardingTill):
        self.boardingTill = boardingTill

    def getBoardingTill(self):
        return self.boardingTill
    
    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime 

    def getArrivalTime(self):
        return self.arrivalTime

    def setDepartureLoctaion(self, departureLocation):
        self.departureLocation = departureLocation 

    def getDepartureLocation(self):
        return self.departureLocation 
    
    def setArrivalLoctaion(self, arrivalLocation):
        self.arrivalLocation = arrivalLocation 

    def getArrivalLocation(self):
        return self.arrivalLocation
    
    def updateFlightDetails(self):
        #update flight schedule
        pass
    
#Airport class
class Airport:
    def __init__(self, locationCode, terminal, gate):
        self.locationCode = locationCode
        self.terminal = terminal
        self.gate = gate

    def setLocationCode(self, locationCode):
        self.locationCode = locationCode

    def getLocationCode(self):
        return self.locationCode
    
    def setTerminal(self, terminal):
        self.terminal = terminal

    def getTerminal(self):
        return self.terminal
    
    def setGate(self, gate):
        self.gate = gate

    def getGate(self):
        return self.gate
    
    def updateAirportDetails(self):
        #update  airport details
        pass
    
#BoardingPass Class
class BoardingPass:
    def __init__(self, passenger, flight, airport, seat, electronicTicket):
        self.passenger = passenger
        self.flight = flight
        self.airport = airport
        self.seat = seat
        self.electronicTicket = electronicTicket

    def updateBoardingPassDetails(self):
        #update Boarding Pass Details
        pass

    def displayBoardingPassDetails(self):
        print('-----NATIONAL AIRLINES-----')

        print('--Passenger Class Data--')
        print('Passenger Name: ', self.passenger.getPassengerName())

        print('--Flight Class Data--')
        print('Type: ', self.flight.getType())
        print('Number: ', self.flight.getFlightNumber())
        print('Departure Date: ', self.flight.getDate())
        print('Boarding Till: ', self.flight.getBoardingTill())
        print('Departure Time: ', self.flight.getDepartureTime())
        print('Departure Location: ', self.flight.getDepartureLocation())   
        print('Arrival Time: ', self.flight.getArrivalTime())
        print('Arrival Location: ', self.flight.getArrivalLocation()) 

        print('--Airport Class Data--')
        print('Loctaion Code: ', self.airport.getLocationCode())
        print('Terminal: ' ,self.airport.getTerminal())
        print('Gate: ', self.airport.getGate())

        print('--BoardingPass Class Data--')
        print('Seat: ', self.seat)
        print('Electronic Ticket: ', self.electronicTicket)



#main
p1 = Passenger('JAMES SMITH')
f1 = Flight('NA4321', '11:40', '13:30','CHICAGO ORD', 'NEW YORK JFK', '06 DEC 20', '11:20', 'First Class')
a1 = Airport('ORD', '2', '03') # 'ORD' from 'CHICAGO ORD'
b1 = BoardingPass(p1, f1, a1, '09A', '629')
b1.displayBoardingPassDetails()