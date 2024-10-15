import geopandas as gpd


shapefile_path= "E:/####@@@/nyer.shp"


# shapefile_path = r"E:/####@@@/nyer.shp"  # Ensure the correct path format
try:
    gdf = gpd.read_file(shapefile_path)
    print(gdf.head())  # Display the first few rows to check if it's loading properly
except Exception as e:
    print(f"Error: {e}")