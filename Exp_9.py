import pandas as pd
property_data = pd.DataFrame({
    "property_id": [1, 2, 3, 4, 5, 6],
    "location": ["City A", "City B", "City A", "City C", "City B", "City A"],
    "bedrooms": [3, 5, 4, 6, 2, 5],
    "area_sqft": [1200, 2500, 1500, 3000, 900, 2200],
    "listing_price": [300000, 550000, 380000, 750000, 200000, 620000]
})
avg_price_per_location = property_data.groupby("location")["listing_price"].mean()
print("Average Listing of Property per location",avg_price_per_location)
print()
properties_more_than_4_bed = property_data[property_data["bedrooms"] > 4].shape[0]
print("Number of Properties with More Than 4 Bedrooms:", properties_more_than_4_bed)
largest_property = property_data.loc[property_data["area_sqft"].idxmax()]
print("Property with the Largest Area",largest_property)
