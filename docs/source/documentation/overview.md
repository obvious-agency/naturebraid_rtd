# Overview

The Nature Braid (NB) framework, is the next-generation extension and software implementation of the Land Utilisation and Capability Indicato (LUCI) model which was the second-generation of the Polyscape framework, as described in [Jackson et al., (2013)](https://www.sciencedirect.com/science/article/pii/S0169204612003532). NB illustrates the impacts of land use, management, climate, etc on the environment and associated ecosystem services. It runs at fine spatial scales to understand the flows of energy, water, mass, and contaminants through the landscape and to water bodies. It compares the current capabilities of the landscape estimates of their potential capabilities.

## The NB framework includes models for

- Agricultural production

- Erosion risk and sediment delivery

- Estimating soil hydraulic characteristics

- Carbon sequestration

- Flood mitigation

- Habitat provision

    - Connectivity
    
    - Mean patch size

    - Shannon and Simpson's diversity
    
    - Species distribution and density

- Land use/cover accounting

- Rainfall-runoff

- Water quality – Nitrogen and Phosphorus

## Background

Ecosystem service condition is assigned based on nationally-available datasets (enhanced with local data where available), on topography (raster DEM), stream network (vector polyline format), precipitation and evapotranspiration (raster format), land cover and soil type (vector polygon format). These are linked to lookup tables and processed within the model, with simulation of connectivity through cost distance approaches for habitat and topographic routing for hydrological and associated services. The topographic routing approach enables explicit simulation of movement of water and difuse pollution over the landscape, as well as identifcation of features which help to mitigate risk of flash flood and in-stream pollution. The model runs at catchment scale with a fine resolution, enabling assessment of the impact of farm scale interventions at catchment scale. The model also identities opportunities to improve ecosystem service condition, and these output maps can be used for decision support. Tradeoffs and synergies between individual service provisions are modelled explicitly to support such decision making. The NB framework is designed to follow the following principles:

(Table 1: Principles of the NB framework)

| Practical | Conceptual |
|--------------|-----------|
| Can be run using nationally available data; i.e. available everywhere so *relevant to national spatial planning* | Operates at a spatial scale *relevant for field and sub-field level management decisions* |
| Modular – can embed other models and aspects can be embedded in other models (NB is a *framework*) | "Values" features and potential interventions by area affected, not just area directly modified |
| Fast running to enable "real time" scenario exploration | Addresses trade-offs and searches for "win-win" solutions |

## Availability and requirements for application

NB is an evolving framework; the current release version includes the previous generations' functionality along with additional habitat, erosion, rainfall-runoff, water quality, data analysis and reporting functions. It requires ESRI's ArcMap 10.4.1 or ArcGIS Pro 2.6 or above to run. Documentation and help are included within this document, and additionally embedded within the NB software and viewable through ArcMap or ArcGIS Pro.

NB requires three datasets to run and can be enhanced with local data if available:

1. **Digital elevation model (DEM):** To represent landscape topography and ideally has a grid size of 5x5m to 10x10m, although any resolution data can be used as input. The finer the resolution the more detailed the output

2. **Land cover information:** To represent impacts of different types of vegetation and management on ecosystem services. An existing database of land cover types are already supported by NB, but local data can also be used as long as the required parameterisation has been completed

3. **Soil information:** To represent the effect of soil types on ecosystem services. An existing database of soi classification schemes are already supported by NB, but local data can also be used as long as the required parameterisation has been completed

Other optional information that can be used as input include a stream network, rainfall, and evapotranspiration. These are not necessary to NB, but their addition improves the accuracy and reliability of NB output.

The DEM and stream network (if input) generates a hydrologically and topographically consistent DEM to correct for potential artefacts, allowing NB to more accurately simulate the flow of water through the landscape. Together with the land cover and soil information, NB generates a baseline scenario that feeds into determining the spatial distribution, supply, and opportunities of the individual ecosystem services. The land cover information can be amended to explore potential scenarios where the land use or management have changed. 

Because of its effcient numerical implementation, NB is fast-running and runs at multiple spatial scales, from sub-field to catchment to national planning. NB generates a series of raster datasets (maps) and underlying tables that illustrate areas and associated statistics of good provision and areas that would benefit from changes in management intervention. Multiple ecosystem services can be compared to identify where trade-offs or synergies in ecosystem services exist.

A number of national datasets are supported for United Kingdom and New Zealand applications. For other countries it is currently necessary to match land cover and soil information into the supported classification systems, or parameterise the local land cover and soil data with information required by NB. Support for a broader range of datasets will be added in the future. Suggested/default parameters are provided with NB; see the individual tool documentation for more detail.

(Table 2: Services, description, and method of the models within the NB framework)

| Service | Description | Method |
|---|---|---|
| Agricultural productivity | Evaluates the potential, current, and optimal agricultural productivity | Based on slope, fertility, drainage, aspect, climate |
| Carbon stocks and fluxes | Calculates carbon levels at a steady state, potential to increase storage, emissions, and sequestration | IPCC Tier 1 compatible. Based on soil, vegetation, stocking rate, fertiliser |
| Erosion and sediment | Estimates soil loss from gullies and rill/inter-rill erosion | Uses CTI and RUSLE. Based on slope, curvature, contributing area, land use and soil type |
| Flood mitigation | Maps locations that are sinks for overland and surface flow, where flow may accumulate, and average flow to all points of the stream and lake network | Topographical routing of water accounting for storage and infiltration capacity as function of soil & land use |
| Habitat connectivity and suitability | Identifies suitable areas for habitat expansion and protection based on connectivity and characteristics | Cost-distance approach: dispersal, fragmentation, connectivity; Identification of priority habitat by biophysical requirements; Measures of habitat richness, evenness, patch size etc. |
| Nitrogen and Phosphorus | Maps the terrestrial load of different land cover and soil, accumulation of nutrients through the landscape, pathway to streams, and in-stream nutrient concentrations | Export coeffcients (land cover, farm type, regional fertiliser, stocking rate) combined with water and sediment delivery models |
| Coast/floodplain inundation risk | Creates an indicative map of areas that could potentially be inundated by storm surge or long term rise | Based on topography and input height of storm surge/long term rise etc: surface and groundwater impacts estimated |
| Trade-offs/synergy identification | Identifies areas where management interventions may enhance or degrade multiple services | Various layering options with categorised service maps; e.g. Boolean, conservative, weighted arithmetic, distribution plots |

## Summary of included tools

- Preprocessing tools

    - Generate Baseline

    - Generate new land cover scenario

- Individual Ecosystem Services

    - Agricultural Productivity
    
    - Carbon Stocks and Fluxes
    
    - Erosion and Sediment
    
    - Flood mitigation
    
    - Habitat connectivity
    
    - Habitat suitability
    
    - Nitrogen
    
    - Phosphorus
    
    - RUSLE

- Batch run and tradeoffs
    
    - Batch run ecosystem services
    
    - Load Outputs for Multiple Services
    
    - Tradeoff maps

- Aggregation and disaggregation tools

    - Aggregate LUCI input data

    - Calculate aggregate input statistics

    - Create data aggregation grid
    
    - Report aggregate input statistics
    
    - Report aggregate single service statistics
    
    - Report aggregate tradeoff statistics

- Miscellaneous

    - Batch clip results and produce statistics (batch run folder)

    - Batch clip results and produce statistics (individual folders)
    
    - Calculate stream and study area statistics
    
    - Change user settings
    
    - Clean geodatabase
    
    - Clip and buffer raster
    
    - Clip data in folder
    
    - Clip LUCI Subset Output

    - Find confluences in stream network
    
    - Floodplain inundation

    - Get raster values at points
    
    - Recondition DEM
    
    - Sea level inundation
    
    - Show terrestrial flow
