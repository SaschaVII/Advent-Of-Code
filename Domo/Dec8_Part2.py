import numpy as np

def getDistance(first_coord, sec_coord):
    p0 = np.array(first_coord)
    p1 = np.array(sec_coord)
    return np.linalg.norm(p0 - p1)

def insertIntoShortest(shortest_connections, new_connection, distance, max_connections = 1000):
    if len(shortest_connections)==0:
        shortest_connections.append([new_connection[0],new_connection[1],distance])


    for i  in range(len(shortest_connections)):
        if shortest_connections[i][2] > distance:
            shortest_connections.insert(i, [new_connection[0],new_connection[1],distance])
            break

    if len(shortest_connections)> max_connections:
        shortest_connections.pop(-1)


def getThresholdDistance(shortest_connections):
    if len(shortest_connections)==0:
        return 1000000.0
    return shortest_connections[-1][2]

def getNewConnections(coordinates, max_connections = 1000):
    shortest_connections = []
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i >= j:
                continue

            distance = getDistance(coordinates[i],coordinates[j])
            if distance < getThresholdDistance(shortest_connections):
                insertIntoShortest(shortest_connections, [i,j], distance, max_connections)

    for connection in shortest_connections:
        connection.pop(2)
    return shortest_connections


def insertIntoConnections(new_connection, connections):
    i = 0
    for connection in connections:
        
        #Option 1: Those two are already connected
        if new_connection[0] in connection and new_connection[1] in connection:
            #print("already in connection: ", i, "connection: ", new_connection)
            return False


        #Option 2: Only first node in a connection
        if new_connection[0] in connection and new_connection[1] not in connection:
            j = 0
            for other_connection in connections:
                if new_connection[1] in other_connection:
                    #combine two (Option 4, both in seperate nodes)
                    elements = connections.pop(j)
                    for element in elements:
                        connections[i].append(element)
                    #print("combine: ", i,j ,"connection: ", new_connection)
                    return True
                j+=1
            #else
            #print("append ", i, "connection: ", new_connection)
            connections[i].append(new_connection[1])
            return True


        #Option 3. Only seconds node in a connection
        if new_connection[0] not in connection and new_connection[1] in connection:
            j = 0
            for other_connection in connections:
                if new_connection[0] in other_connection:
                    #combine two (Option 4, both in seperate nodes)
                    elements = connections.pop(j)
                    for element in elements:
                        connections[i].append(element)
                    



                    #print("combine: ", i,j ,"connection: ", new_connection)
                    return True
                j+=1
            #else
            #print("append ", i, "connection: ", new_connection)
            connections[i].append(new_connection[0])
            return True
        
        i+= 1

    #Option 5, neither part of connections
   
    connections.append(new_connection)
    return True
    print("new connection: ", new_connection)
    

if __name__ == '__main__':

    file_path = 'inputTest.txt'

    coordinates = []
    

    with open(file_path, 'r') as file:

        lines = file.readlines()
        for line in lines:
            single_coordinate = []
            for number in line.split(','):
                single_coordinate.append(int(number))
            coordinates.append(single_coordinate)    

    #print(coordinates)
    raw_connections = []
    connections = []

    # for i in range(1000):

    #     raw_connections.append(getNewConnection(coordinates, raw_connections))
    #     print("connection number: ", i)
        
    raw_connections = getNewConnections(coordinates, 10000)
        
    print(raw_connections)
    i= 0
    for connection in raw_connections:
        len_before_insert = len(connections)
        if insertIntoConnections(connection,connections):
            print("last insert: ",connection)
            first_x = coordinates[connection[0]][0]
            second_x = coordinates[connection[1]][0]
            print("len connections: ", len(connections))
            print("product: ", first_x*second_x)
        #print(i,"  connections:  ",connections)
        i+= 1
        len_after_insert = len(connections)
        


            
