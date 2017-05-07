def find_distance():
    
    import pygeocoder as geo
    from math import radians, cos, sin, asin, sqrt
    
    #haversine borrowed from 1st comment on this link: 
    #https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points 
    #haversine formula:
    def haversine(lon1, lat1, lon2, lat2):
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        km = 6367 * c
        return km
    
    while True:    
        try:
            locA = str(raw_input("Please enter the first place here, being as specific as possible (place,state/country): "))
            locB = str(raw_input("Please ener the second place here: "))
            a = geo.Geocoder.geocode(locA)
            b = geo.Geocoder.geocode(locB)
        except geo.GeocoderError:
            print("Looks like that place does not exist, try again!")
            continue
        else:
            print('Yep those are places!')
            break 

    distance = haversine(a.longitude,a.latitude,b.longitude,b.latitude)
    print("The distance between {} and {} is: ").format(locA,locB)
    print(distance,"km, or",distance*0.621371," miles")
