# Miscellaneous

This section contains standalone tools and functions, and are described briefly.

## Calculate stream and study area statistics

### Summary

For either Nitrogen or Phosphorus, this function calculates the statistics of nutrient loads and concentrations in the study area and in the streams.

## Change user settings

### Summary

This tool allows the user to configure some aspects of LUCI:

- **Scratch path:** Sets the location of the scratch geodatabases that hold the intermediate files during a LUCI run. 

- **Basemap:** Choose the basemap shown when LUCI loads output into ArcMap. 

- **Use developer mode?:** If making code changes, setting this to true will mean that any modules imported will be refresh before they are used. This removes the extra step of manually refreshing the toolbox after a code change. 

- **Reset all settings to their default values:** Resets the user settings to default values.

## Clean geodatabase

### Summary

This tool manually clears a geodatabase, and the scratch geodatabase is commonly used as input to remove any intermediate files still left from a previous run.

## Clip and buffer raster

### Summary

This tool takes a raster and shapefile, buffers the shapefile by a user-defined width, and clips the raster down to the extent of the buffered shapefile.

## Clip data in folder

### Summary

This tool runs a batch operation to clip all the rasters and shapefiles within the input folder to the extent of a user-defined shapefile.

## Clip LUCI Subset Output

### Summary

This tool runs a batch operation to clip all the rasters and shapefiles, and to update the maps within the PDF of LUCI output from the baseline tool, the single services tools, or from the tradeoff tool.

## Create Polygon Grid

### Summary

This tool generates a grid of square-shaped cells of a specified size, from an input polygon extent. The grid extent can optionally be aligned to suitable coordinates e.g. 123456 to 123000, and have a buffer applied. If a desired cell size is not known, set to zero.

The output grid will overlap the input extent completely, and as such, if the extent is not exactly divisible by the chosen cell size, the extent of the output will be slightly larger than that of the input.

## Floodplain inundation

### Summary

This tool uses the flatwater inundation approach described in Ballinger et al. (2011) and Benavidez (2018) to generate flooding extent. ***Note: This tool is currently being tested for the Lower Hutt catchment, New Zealand and is still in-development.***

## Recondition DEM

### Summary

This tool implements the AGREE method (Hellweger, 1997) to burn streams into a digital elevation raster.

## Sea level inundation

### Summary

This tool calculates the land area covered by user-defined sea level rise and the height of the flood water for the inundated area.

## Show terrestrial flow

### Summary

This tool uses the flow direction information to identify where flow is exiting or entering the study area, or where there are ridgelines at the boundary.