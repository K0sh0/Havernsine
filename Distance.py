# Importing math library to use mathematical functions
import math 

# Define Haversine function to calculate the distance between two points on the earth
def haversine(lat1, lon1, lat2, lon2): 
      
    # calculate differences between latitudes and longitudes 
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
  
    # convert latitude coordinates from degree to radians
    lat1 = lat1 * math.pi / 180.0
    lat2 = lat2 * math.pi / 180.0
  
    # apply haversine formula 
    a = ( math.sin(dLat / 2)**2) + ( math.sin(dLon / 2)**2) * math.cos(lat1) * math.cos(lat2)
    
    # radius of the earth in miles
    rad = 3959
    
    # compute the circular angle 
    c = 2 * math.asin(math.sqrt(a)) 
    
    # return the haversine distance
    return rad * c 
  
# Driver code 
if __name__ == "__main__":
    
    # past 2 minutes after 0030
    minn = 2           
    
    # convert minutes to degrees
    deg = (minn / 60) * 15
    
    # coordinates of the first location
    lat1 = -8.5
    lon1 = 85.7
    
    # adjust the longitude of the first location according to the time
    lon1 = lon1 - deg
    
    # coordinates of the second location
    lat2 = -37.8
    lon2 = 144.9

    # compute haversine distance
    distance = haversine(lat1, lon1,lat2, lon2)
    
    # calculate the angle
    angle = (90 - distance  / 69.097)  
    
    # printing the calculated distance in miles and the angle
    print(haversine(lat1, lon1,lat2, lon2), "Miles")
    print(angle)
