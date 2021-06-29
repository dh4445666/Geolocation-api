import googlemaps

# import data, replace with input or with dataset

#.....................

#set Google maps api
gmaps_key = googlemaps.Client(key = "API")

# obejcts lat as latitude and lon as longitude
df["LAT"] = None
df["LON"] = None

# Get latitude lat and longitude lon
for i in range(0,len(df), 1):  
    geocode_result = gmaps_key.geocode(df.iat[i,0]) # address of property panda
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lat"]
        df.iat[i, df.columns.get_loc("LAT")] = lat
        df.iat[i, df.columns.get_loc("LON")] = lon
    except:
    lat = None
    lon = None

print(geocode_result[0])
        
