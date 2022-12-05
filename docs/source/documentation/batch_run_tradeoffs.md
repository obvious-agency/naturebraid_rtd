# Batch Run / Tradeoffs

## Batch run ecosystem services

### Summary

This tool allows a selection (or all) of the multiple ecosystem function models available in NB to be run in "batch process" mode, saving their various outputs into a user-specified folder. A complementary tool then allows these output to be loaded into the current ArcMap session for inspection.

### Input

- **Ecosystem services output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input: Study area baseline folder:** Specify the path and folder where files are stored from running the **Generate Baseline** tool. 

- **Tickboxes to run the individual ecosystem services:** Select the ecosystem services of interest. 

- The succeeding parameters are the same as those in the single service ecosystem services tools.

### Output

Within the output folder are separate folders for each of the ecosystem services with all the output files and PDFs. 

- **agprod:** Agricultural productivity 

- **carbon:** Carbon 

- **erosed:** Erosion and sediment 

- **flood:** Flood mitigation 

- **habconn:** Habitat connectivity 

- **habsuit:** Habitat suitability 

- **nitrogen:** Nitrogen 

- **phosphorus:** Phosphorus

## Load Outputs for Multiple Services

### Summary

This tool takes the already generated output from the **Batch run ecosystem services** tool and loads the results from the single ecosystem service models to the current ArcMap session.

### Input

- **Output folder:** Specify the path and folder where the outputs from the **Batch run ecosystem services** tool are stored. 

- **Tickboxes to load the outputs from the individual ecosystem services:** Select the ecosystem services of interest.

### Output

This tool will automatically load the outputs to the ArcMap session.

## Tradeoff Maps

### Summary

NB Trade-off maps identify where opportunities exist to improve delivery of services whilst protecting areas which currently delivery a high level of service. NB's individual service calculations include an output for each service where each cell in the terrestrial landscape is categorised into one of five provisioning categories from high to low, and this categorisation is further reduced into three categories for trade-off analysis, as indicated in the table below.

| Categories for NB individual service categories | Categories for NB tradeoffs |
| --- | --- |
| a) Very high existing service <br>b) High existing service | High existing good |
| c) Moderate or marginal service | Negligible existing good but negligible opportunity to improve significantly |
| a) Small or degrading service <br>b) Very small or rapidly degrading service | Bad or negligible existing good with potential to improve |

NB then layers those categorised services to identify parts of the landscape where trade-offs versus win-win situations exist, and where management interventions could enhance or protect multiple services. Areas with multiple "high existing good" and no "bad" or "potential to significantly improve" areas are flagged as win-win situations where status quo should be preserved. Similarly, areas where multiple "bad" or "potential to significantly improve" classifications exist are flagged as "win-win" situations for implementation of change. Areas where trade-offs exist where significant improvements of some services would likely go in tandem with degradation of other services- are separately categorised, as are areas where there are not obvious advantages in either preserving status quo or implementing management change.

For trade-off analysis, this categorisation is further reduced into "high existing good", "bad or negligible existing good with potential to improve", or "negligible existing good but negligible opportunity to improve significantly". NB then layers those categorised services to identify parts of the landscape where trade-offs versus win-win situations exist, and where management interventions could enhance or protect multiple services. Areas with multiple "high existing good" and no "bad" or "potential to significantly improve" areas are flagged as win-win situations where status quo should be preserved. Similarly, areas where multiple "bad" or "potential to significantly improve" classifications exist are flagged as "win-win" situations for implementation of change. Areas where trade-offs exist where significant improvements of some services would likely go in tandem with degradation of other services- are separately categorised, as are areas where there are not obvious advantages in either preserving status quo or implementing management change.

### Input

- **Output folder for tradeoffs:** Specify the path and folder where output from this tool should be stored. 

- **Folder containing ecosystem services output:** Specify the path and folder where files are stored from running the **Batch run ecosystem services** tool. 

- **Tradeoff options:** Five options are possible in the tradeoff mapping tool. 

    - *Equal arithmetic:* counts the number of "wins", "losses" and "negligible impact" predicted under change, and identifies those areas where more wins or more losses are expected overall. It treats all services as being of equal importance, and is a special / simple case of the "weighted arithmetic" option. 

    - *Conservative:* seeks to avoid negative change in any service. This option is not available when more than four service are being traded off against each other (where conservation is particularly important for a subset of services, see the mixed conservative/arithmetic option). 

    - *Standard:* considers concepts from both, considering both the overall "sum" from the tradeoff analysis and the balances of "wins" and "losses". In some way it can be seen as a middle ground between the arithmetic and conservative approach; seeking to maximise wins with minimal losses. Although all output is produced through objective/deterministic functions the choices made to categorise this third "standard" option are somewhat subjective. This option is only supported for up to four single services. 

    - *Weighted arithmetic:* counts the number of "wins", "losses" and "negligible impact" predicted under change, and identifies those areas where more wins or more losses are expected. 

    - *Mixed conservative/weighted additive:* allows up to three services to treated conservatively, and treats the rest through the weighted additive approach. This allows a small number of services identified as vital to be prioritised, while also enabling consideration of a wider range of services 

- **Reporting option:** Four reporting options are possible. 

    - *Limited:* produces an aggregated "overall" tradeoff/synergy map. 

    - *Summary:* generates the Limited map, and stores additional information at each pixel so the total number of "wins", "losses", and "negligible impacts" can be investigated. 

    - *Individual:* stores individual service information on "wins", "losses" etc so these numbers can be interrogated along with the summary output at each pixel. 

    - *Full (summary + individual):* stores all this information within all output tradeoff rasters. Users should balance their needs for fuller reporting/analysis with storage and computational demands. 

- **Lowest level of calculation:** This sets the lowest level of tradeoff calculations that will be carried out. E.g. a value of two (lowest possible value) will carry out two way calculations, then three way, up to the maximum level of tradeoffs input. Conversely, a value set at the maximum level (ie. 4 with 4 services being analysed) will only carry out the highest level analysis.The highest level of analysis is the quickest option, and does offer some capability to explore which services contribute to wins and losses through the raster attribute table. 

- **Tickboxes to select which ecosystem services to consider:** Tick the boxes of the services that will be considered for the tradeoffs. 

- **Weight for each of the ecosystem services:** The weighting for the services can be specified. Weighting that will be given to this service. For the mixed weighted arithmetic/conservative approach a weight of -1 will cause this service to be treated as conservative. In all other cases, the number must be greater than zero. Its proportional weighting in the tradeoff calculation is the contribution this makes to the overall sum of weights. *Default value is 1.*

- **Habitant being considered for what species?:** Specify the species for which habitat connectivity was modelled. Currently this model defaults to 11 for broadleaved woodland generic focal species Parameterisation for further species will take place according to NB project needs. *Default value is 11.*

Up to three (3) other rasters can be included in the tradeoff analysis. These can be ouputs from the RUSLE tool or rasters from other non-NB tools, as long as they have the same extent and cell size as the NB output rasters. The values in the raster **must** be reclassified to the following:

| Raster value | Meaning |
| --- | --- |
| 1 | Very high existing service |
| 2 | High existing service |
| 3 | Moderate or marginal service |
| 4 | Small or degrading service |
| 5 | Very small or rapidly degrading service |

- **Consider user-input service 1/2/3:** Tick these boxes if you want your user-input service rasters to also be included in the calculation.

- **Raster for user-input service 1/2/3:** Specify the path and filename to the user-input raster to be considered for tradeoff analyses. Note: remember to reclassify the rasters to have the scale of 1 to 5 based on the table above.

- **Weight for user-input service 1/2/3:** The weighting for the services can be specified. Weighting that will be given to this service. For the mixed weighted arithmetic/conservative approach a weight of -1 will cause this service to be treated as conservative. In all other cases, the number must be greater than zero. Its proportional weighting in the tradeoff calculation is the contribution this makes to the overall sum of weights. *Default value is 1.*

### Output

The tool produces rasters showing the spatial distribution of tradeoffs and synergies. The corresponding tables summarise the proportion of the study area that have the following characteristics: 

- Excellent service provision 

- Moderate service provision 

- Negligible service or tradeoffs 

- Opportunity to improve service 

- Excellent opportunity to improve service

The rasters and tables are named with combinations of abbreviations of the services being considered for that tradeoff: 

- **Agp:** Agricultural productivity 

- **Car:** Carbon 

- **Ero:** Erosion and sediment 

- **Flo:** Flood mitigation 

- **Hab:** Habitat connectivity and suitablity 

- **Nit:** Nitrogen 

- **Pho:** Phosphorus

- **Us1:** User-input service 1

- **Us2:** User-input service 2

- **Us3:** User-input service 3
