# Miscellaneous

This section contains standalone tools and functions, and are described briefly.

## Batch clip results and produce statistics (batch run folder)
### Summary

### Inputs

### Outputs

## Batch clip results and produce statistics (individual folders)
### Summary

### Inputs

### Outputs

## Calculate stream and study area statistics
### Summary
For either Nitrogen or Phosphorus, this function calculates the statistics of nutrient loads and concentrations in the study area and in the streams. It populates the stream entry/exit points with statistics about nutrient loading and concentrations. Please ensure you have run the *Generate Baseline*, *Nitrogen*, and/or *Phosphorus* tools first.

### Inputs
- **Baseline folder:** Specify the path and folder where the output from the *Generate Baseline* tool is stored.

- **Nutrient folder:** Specify the path and folder where the output from the *Nitrogen* or *Phosphorus* tool is stored.

- **Element:** Specify which element you are calculating statistics for, this is a dropdown menu containing either Nitrogen or Phosphorus.

### Outputs
The outputs will be saved to the input nutrient folder, with files being created and updated with statistic information: *studyareacalcs.dbf*, *entryexitpoints.shp*, and *streamnetwork.shp*.

## Change user settings
### Summary
This tool allows the user to configure some aspects of NB:

- **Scratch path:** Sets the location of the scratch geodatabases that hold the intermediate files during a NB run. 

- **Basemap:** Choose the basemap shown when NB loads output into ArcMap. 

- **Use developer mode?:** If making code changes, setting this to true will mean that any modules imported will be refresh before they are used. This removes the extra step of manually refreshing the toolbox after a code change. 

- **Reset all settings to their default values:** Resets the user settings to default values.

It does not produce output, but updates the internal settings of the Nature Braid.

## Clean geodatabase
### Summary
This tool manually clears a geodatabase, and the scratch geodatabase is commonly used as input to remove any intermediate files still left from a previous run.

## Clip and buffer raster
### Summary
This tool takes a raster and shapefile, buffers the shapefile by a user-defined width, and clips the raster down to the extent of the buffered shapefile.

### Inputs
- **Input raster:** Specify the path and filename of the raster to be clipped down to the buffered shapefile.

- **Clip extent:** Specify the path and filename of the shapefile to be buffered and used as the clip extent.

- **Buffer width (metres):** Specify the amount in metres how far the shapefile is to be buffered.

- **Output raster:** Specify the path and filename of the output raster.

### Outputs
The output is a clipped raster saved to the location and filename specified by the *Output raster* parameter above.

## Clip data in folder
### Summary
This tool runs a batch operation to clip all the rasters and shapefiles within the input folder to the extent of a user-defined shapefile.

### Inputs
- **Input folder:** Specify the path and folder containing the folder with the raster and shapefiles to be clipped. This is usually the output from one of the other NB tools.

- **Output folder:** Specify the path and folder where the outputs where this tool will be saved.

- **Clip extent:** Specify the path and filename of the shapefile that the files from the input folder will be clipped down to.

### Outputs
The clipped outputs will be saved in the folder specified by the *Output folder* parameter.

## Clip LUCI subset output
### Summary
This tool runs a batch operation to clip all the rasters and shapefiles, and to update the maps within the PDF of NB output from the baseline tool, the single services tools, or from the tradeoff tool. This is similar to the *Clip data in folder* tool.

### Input
- **Output: Folder for clipped extent from all input folders:** Specify the path and name of the folder where you want the output from this tool to be stored.

- **Input: clip extent shapefile or feature class:** Specify the path and filename of the shapefile that the input files will be clipped down to.

- **Input: Original/full baseline folder:** Specify the path and name of the folder containing the original output from the *Generate Baseline* tool.

- **Input: Original/full LUCI single services output folder:** Specify the path and name of the folder containing the original output from one of the single services tools.

- **Input: Original/full LUCI tradeoff output folder (optional):** Specify the path and name of the folder containing the original output from the tradeoff tool.

- **Clip baseline folder?** Tick this if you want to clip the baseline folder. Sometimes the baseline folder does not need to be clipped, such as when this tool is being run again to clip the output of different service folders. *Default is unticked*

- **Input: Clipped baseline folder (optional):** Optionally, specify the clipped baseline folder from a previous run of this tool. Specifying a baseline folder here is useful for the auto-generation of PDFs and auto-loading of layers.

### Output
The output from this folder will be a series of folders with the clipped datasets, saved to the location from the *Output: Folder for clipped extent from all input folders*.

## Find confluences in stream network
### Summary
This tool uses the output from the *Generate Baseline* tool to create a shapefile of confluences in the study area's stream network.

### Inputs
- **Output folder:** Specify the path and folder name where the output from this tool will be stored.

- **Baseline folder:** Specify the path and folder name that contains the output from the *Generate Baseline* tool.

### Outputs
The output is a point shapefile called *confluences.shp* found in the output folder.

## Floodplain inundation
### Summary
This tool uses the flatwater inundation approach described in [Ballinger et al. (2011)](https://www.wgtn.ac.nz/sgees/research-centres/documents/potential-flooding-and-inundation-on-the-hutt-river.pdf) and [Benavidez (2018)](http://researcharchive.vuw.ac.nz/handle/10063/7948) to generate flooding extent.

### Inputs

### Outputs

## Get raster values at points
### Summary

### Inputs

### Outputs

## Recondition DEM
### Summary

### Inputs

### Outputs

## Sea level inundation
### Summary

### Inputs

### Outputs

## Show terrestrial flow
### Summary

### Inputs

### Outputs

