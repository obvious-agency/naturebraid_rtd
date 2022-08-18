# Individual ecosystem services tools

All of the individual ecosystem services tools requires the output from the **Generate Baseline** tool. Each tool generates files and several are loaded to the screen with the correct symbology and the legend. The key outputs are written to a PDF file that can be found within the output folder. If desired, the key maps and tables can be generated in PNG format by ticking the *Generate PNG maps and graphs parameter*. These maps and tables can be found under the Images folder of the output folder.

If a tool fails, the user can re-run the tool through the Results window and tick the Rerun tool (will continue previous run from the point where any errors occurred option. This only works if the relevant files such as intermediate and temporary files are still within the scratch folder and have not been erased

## Agricultural Productivity

### Summary

This tool evaluates potential agricultural productivity of the land according to simple criteria (slope, fertility, aspect and drainage). The model calculates predicted optimal agricultural utilisation based on soil type, using assigned values of fertility and waterlogging (yes, no or seasonal) and topographic data, using calculated values for aspect slope and elevation. If desired you can weight this calculation to increase soil fertility values to account for farmer effort and management which may be applied due to low production potential in the region containing your study area. Current agricultural utilisation will be mapped according to the land cover data, ranking land use from highest productivity to lowest: Arable; Improved grassland; Unimproved grassland; Woodland and heath; Bog sand and rock. An output for relative utilisation is calculated from comparison of current and potential utilisation.

As input, this tool requires the outputs from the **Generate Baseline** tool. Output from this tool can be used to assess where land may be under or over utilised. The tool can also be used to identify areas of more productive land, where farmers may be less willing to make changes, and areas of less productive land,which could be targeted for re-wilding or afforestation

### Input

- **Output folder:** Specify the path and folder where output from this tool should be stored.

- **Input:** Study area baseline folder: Specify the path and folder where files are stored from running the **Generate Baseline** tool.

- **Slope threshold (degrees) for very productive land:** Maximum slope (in degrees) of very highly productive agricultural land. This can be changed to respect regional agricultural practice. If an adjusted value is applied, this should be considered when interpreting model output, in terms of additional management efforts required to enable agricultural production of steeper slopes. When setting this threshold DEM resolution should be considered. For example, use of an overly coarse DEM may mean that smaller areas of steep slope are not detected. *(Default value is 5.)*

- **Slope threshold (degrees) for somewhat productive land:** Maximum slope (in degrees) of somewhat productive agricultural land. This can be changed to respect regional agricultural practice. If an adjusted value is applied, this should be considered when interpreting model output, in terms of additional management efforts required to enable agricultural production of steeper slopes. When setting this threshold DEM resolution should be considered. For example, use of an overly coarse DEM may mean that smaller areas of steep slope are not detected. *(Default value is 15.)*

- **Elevation threshold (metres) for improved agriculture:** Maximum threshold in metres above sealevel (m asl) of productive agricultural land. This can be changed to respect regional agricultural practice. If an adjusted value is applied, this should be considered when interpreting model output, in terms of additional management efforts required to enable agricultural production at higher elevations. *(Default value is 350m asl.)*

- **Elevation threshold (metres) for all agriculture:** Maximum threshold in metres above sealevel (m asl) of all agricultural land. This can be changed to respect regional agricultural practice. If an adjusted value is applied, this should be considered when interpreting model output, in terms of additional management efforts required to enable agricultural production at higher elevations. *(Default value is 3000m asl.)*

- **Fertility relative to national standard:** This parameter allows fertility to be adjusted for regional variation to account for the study area being in a low or very low fertility region.

    - *1: standard*

    - *2: low fertility*

    - *3: very low fertility*

- **Save intermediate calculations?:** If this is selected, the intermediate categorisations for agricultural productivity, based on single indicators only (i.e. slope, waterlogging etc.), are saved for user inspection. This will enable consideration of how the component factors affect productivity potential. Saving this data is recommended if slope and elevtaion thresholds are adjusted or soil fertility reweighted because exploration of intermediary data will enable the influence of these user choices to be better understood when interpreting model output.

- **Consider slope in overall valuation?:** Select to consider slope in evaluation of agricultural productivity. This should be applied in areas where slope is a factor in agricultural productivity. If not selected in areas with slopes over relevant thresholds, this may reduce accuracy of output on predicted agricultural productivity.

- **Consider elevation in overall valuation?:** Select to consider elevation in evaluation of agricultural productivity. This should be applied in areas where elevation is a factor in agricultural productivity. If not selected in areas with elevations over relevant thresholds, this may reduce accuracy of output on predicted agricultural productivity.

- **Consider waterlogging in overall valuation?:** Select to consider waterlogging in evaluation of agricultural productivity. This should be applied in areas where waterlogging is a factor in agricultural productivity. If not selected in areas with waterlogging, this will reduce accuracy of output on predicted agricultural potential. Conversely, in areas where all soils are prone to waterlogging and have been artificially drained, it may be more accurate not to apply this variable, and this option should be de-selected.

- **Consider soil fertility in overall valuation?:** Select to consider soil fertility in evaluation of agricultural productivity. If not selected in areas where soil fertility is important this will reduce accuracy of output on predicted agricultural potential. Where management activities aim to overcome issues with soil fertility, it may still be appropriate to select this option, in combination with a soil fertility adjustment of 2 or 3 in "Fertility relative to national standard" above.

- **Consider aspect in overall valuation?:** Consideration of aspect can be adjusted. Choose adjustment desired from dropdown options:

    - *0: no*

    - *1: yes, direct face only*

    - *2: yes, direct face + face-E and face-W*

### Output

- **Current agricultural utilisation (util_curr):** This map predicts the current agricultural utilisation from the input land cover product (or land cover scenario), and is therefore reliant on its accuracy. Arable and improved grassland are considered to be highly productive, for example, while bare ground and wetlands are considered to provide no agricultural utilisation. The output is discrete; five categories of production are considered, from very high production (or production capacity) to no production (or production capacity).

- **Predicted optimal agricultural utilisation (util_pred):** This map ignores the input land cover, and instead predicts a near-optimal utilisation based on soil water holding characteristics, fertility, slope and aspect. Flat, well-draining and fertile areas are predicted to have high potential for agricultural production for example, more waterlogged areas or steeper areas have less potential. This model output is dependent on accuracy of user set thresholds and weightings, as well as the soil data layer supplied as input to the scenario pre-processing tool. Uncertainty may also be introduced through model processing, since values for soil fertility and waterlogging are based on estimates or national averages for the soil type, and may not reflect site conditions accurately.

- **Relative agricultural utilisation (util_rel):** This map compares the previous two outputs, and flags where land appears to be over or under-utilised. If both current and predicted utilisation are within one category of each other, land is considered to be appropriately utilised. If they differ by more than one category, LUCI flags where current production appears to be over utilising the land (so may be ineffcient farming, or not sustainable), and also where opportunities to increase agricultural production may be present. Any errors in model output for current and predicted agricultural utilisation will propagate through to this data layer.

- **Agricultural utilisation status (util_stat):** This map combines the current and "predicted optimal" output in a different way to the relative utilisation described previously. Rather than being concerned with direction of change (under or over utilisation), it considers whether the current agricultural utilisation may be worthy of preservation or change. Land in appropriate utilisation is considered worthy of protection, areas where land is over or under-utilised are flagged for consideration of change to management. This output is a fundamental input to the trade-off and synergy mapping algorithms within LUCI. Again, errors in model output for current and predicted agricultural utilisation will propagate through to this data layer

## Carbon Stocks and Fluxes

### Summary

**For England and Wales:** The model first calculates carbon levels at steady state i.e. assuming that land cover is fully established and soil and biomass carbon are no longer in flux. Values are assigned based on the soil and land cover combination, according to assumptions that a) the England and Wales mean for a given soil and landcover combination is broadly representative of the steady state soil carbon where that combination occurs and b) the England and Wales mean biomass carbon for a landcover is broadly representative of the steady state mean value. Values calculated for use in the model are based on the IPCC tier 1 protocols on Climate Change (IPCC); separating carbon into above ground biomass, below ground biomass, deadwood, litter, and soil carbon. The total values for biomass carbon and soil carbon are then fed into the model, to avoid modelling time spent on unnecessary processing.

The model then calculates potential to increase carbon storage over the landscape, by comparing a value of potential carbon stock at equilibrium under a different landcover with the current carbon stock. The model applies a "space for time" substitution to calculate potential for emissions or sequestration, in assuming that any change in carbon storage in soils following landuse change can be estimated based on comparison with data from other sites with the same soils where the new land use is already established. In the case of a supplied landcover change scenario, the second valuation layer is indicative of emissions, whilst in the case of a baseline run, the second valuation layer is indicative of potential for sequestration of carbon, as detailed below.

The values for carbon and land use combinations were based on Bradley et al. (2005), Milne and Brown (1997), and Morison et al. (2012).Values for some soil/land use combinations may be based on expert opinion where data were absent. These calcluations will also be affected by spatial uncertainty in land use and soil layers combined in stage 1.

**For New Zealand:** The model first calculates carbon levels at steady state i.e. assuming that land cover is fully established and soil and biomass carbon are no longer in flux. Values are assigned based on the land cover, according to assumptions that a) the average value for that landcoveris broadly representative of the steady state soil carbon where that coveroccurs and b) the average carbon for a landcover is broadly representative of the steady state mean value. Values calculated for use in the model are based on the IPCC tier 1 protocols on Climate Change (IPCC); separating carbon into above ground biomass, below ground biomass, deadwood, litter, and soil carbon.

The model then calculates potential to increase carbon storage over the landscape, by comparing a value of potential carbon stock at equilibrium for that soil type with the current carbon stock associated with the landcover. The model applies a "space for time" substitution to calculate emissions or sequestration, in assuming that any change in carbon storage in soils following landuse change can be estimated based on comparison with data from other sites with the relevant soil or landcover.

### Input

- **Output folder:** Specify the path and folder where output from this tool should be stored.

- **Input: Study area baseline folder:** Specify the path and folder where files are stored from running the **Generate Baseline** tool.

- **Very high stock threshold:** Threshold for stocks to be classified as very high that feeds into classification for mapping and tradeoffs. *Default value is 90.*

- **High stock threshold:** Threshold for stocks to be classified as high that feeds into classification for mapping and tradeoffs. *Default value is 50.*

- **Moderate stock threshold:** Threshold for stocks to be classified as moderate that feeds into classification for mapping and tradeoffs. *Default value is 27.*

- **Low stock threshold:** Threshold for stocks to be classified as low that feeds into classification for mapping and tradeoffs. *Default value is 21.*

### Output

- **Carbon stock (cstock) and Carbon stock to 30 (CSto30):** This map shows the estimated total carbon storage in the biomass and either top 1m or top 30cm of soil in tonnes/ha. Values are calculated based on soil carbon data for soil type and land-use combinations, and average biomass carbon for each land-cover type. The dataset used depends on the level of aggregation selected in the pre-processing tool; fully disaggregated *(Soil disaggregation value is 15)* uses published soil series level national data from Bradley et al. (2005); Milne and Brown (1997), whereas LULUCF inventory level *(Soil disaggregation value is 14)* uses values taken from the more aggregated inventory approach described in Dyson et al. (2009); Morison et al. (2012).

    Potential sources of error and uncertainty include inaccuracies in user input spatial land use and soil data; in particular, peats are not well accounted for spatially in soil or land use datasets. Accounting will have significant uncertainty, due to use of inventory values of average C for the relevant land use on the relevant soil type; these are often estimated, or based on limited sampling. Actual carbon storage will be strongly affected by site variation from national average conditions.

    Although average and estimated values are not expected to provide an accurate measure of change for in- dividual sites, there is an assumption that errors will balance out at scales relevant for most assessments, particularly for national level inventories. Likely site variation around the mean value applied is strongly affected by the option selected for soil disaggregation; there is much greater variance within the lumped soil types applied in the LULUCF compatible approach. Values for some soil/land use combinations in the fully disaggregated approach may be based on expert opinion where data were absent, increasing uncertainty.

- **Classified carbon stock (cstockclass):** This map is a classified version of carbon stock created both for display purposes and for calculation of inputs to trade-off mapping. Only provided for 1m of soil depth plus biomass, and subject to same sources of error as the non-classified version, in addition to influence from the user-set thresholds. The user provided values for low, moderate, high and very high storage should therefore reflect levels requiring improvements for agricultural purposes or worth protecting to avoid CO<sub>2</sub> emissions.

- **Carbon emission estimation (cemit):** This map predicts the rate of emissions or sequestration of C in tonnes/ha/year. Output will be subject to the same sources of error as the carbon stock maps, in addition to error associated with the space for time substitution approach, since soils may never reach the expected carbon value. There is an assumption that soils will take 150 years to reach the expected value, and output is provided as annual average sequestration or emissions, however soil carbon change tends to follow an exponential curve, and much of the change would occur during the first few years. This approach also fails to account for any initial losses due to soil disturbance etc., which will be strongly affected by land management approaches and timing of activities. Using the fully disaggregated approach, new soil carbon is calculated for the "effective depth" occupied by the same quantity of soil, to give a value for change in carbon that accounts for change in soil density.

    **For scenario:** In the case of a supplied landcover change scenario, the second valuation layer is indicative of emissions in kg m{math}`^{-2\ yr-1}`, calculated as:
    
    ```{math}
    Scenario\ total\ C\ storage − Current\ total\ C\ storage \over 150
    ```
    
    **For current land cover:** In the case of a baseline run, the second valuation layer is indicative of potential for sequestration of carbon in soils. The scenario with most soil carbon is identified from the average under each land use on the relevant soil type, and sequestration potential thus calculated as:
    
    ```{math}
    Maximum\ potential\ soil\ C\ storage + Associated\ biomass\ carbon − Current\ total\ C\ storage \over 150
    ```

    Positive values mapped for carbon change indicate potential to store more carbon in soils and biomass if landcover is changed. Where values are negative for a baseline run, this shows that soils are able to store more carbon under a different landuse, but that reduction in biomass carbon may offset any benefits.
    
- **Classified carbon emission estimation (cemitclass):** This map is a classified version of carbon emission created both for display purposes and for calculation of inputs to trade-off mapping. Only provided for 1m of soil depth plus biomass, and subject to same sources of error as the non-classified version, in addition to influence from the pre-set thresholds.

    **For scenario:** If the carbon stock per unit area is reducing under the applied scenario, opportunity to reverse this is flagged. Conversely, where carbon stocks are expected to increase, protection is suggested, and where they are expected to remain static, LUCI will indicate preservation of the carbon stock "status quo".
    
    **For current land cover:** If the total carbon stock per unit area has potential to increase under a maximum soil carbon stock scenario, opportunity for interventions to sequester carbon is flagged. Where the current landcover has maximum soil carbon stock, LUCI will indicate preservation of the carbon stock "status quo". Conversely, where total carbon stocks would decrease due to biomass carbon loss under a scenario of land use change to increase soil carbon, LUCI flags these areas as probably unsuitable for change.
    
    For example, many woodland areas have moderate to high carbon stocks and hence are considered as of moderate to high value according to the carbon stock calculation, and preservation may have been considered. However, if the woodland has been planted onto peat, for example, a reduction in stored carbon (and associated net CO<sub>2</sub> emission) might be anticipated, so interventions to prevent this or revert land use might be appropriate.
    
- **Carbon status (cstatus):** This map is an assessment of provision of carbon storage and sequestration service which feeds in to the LUCI trade off calculations. It is calculated by combination of classified stock and classified emission layers, and therefore subject to any errors and uncertainties in the creation of these layers. The output maps as good performance anything with high carbon and no loss, as well as areas sequestering or without potential for further carbon storage. Areas with low carbon and no sequestration are mapped as moderate, whilst anything losing carbon, or with potential to gain, or else steady state low carbon is mapped as bad.
    
- **High SOC (HighSOC):** This map highlights locations which are likely to have significant carbon in total soils and biomass; for example landcover associated with deep peats. The classification is applied where either soil or landcover indicates possibility of large stores, and this helps to account for greater inaccuracies in soil mapping due to the diffculty of gathering data. Potential sources of error include inaccuracies in land use and soil input data, or LUCI classification of land cover as associated with high carbon stores; these are based on general trends and may not be representative of the area mapped. The map is intended to highlight areas which may warrant protection.

## Erosion and Sediment

### Summary

This tool identifies areas at risk of erosion and also areas at risk of contributing significant sediment loading into water bodies. Areas of land that are vulnerable to erosion are identified in LUCI using the Compound Topographic Index (CTI) Thorne and Zevenbergen (1990). The CTI represents the erosive potential of overland flow by combining three important factors in this form of soil erosion: water flow magnitude and concentration, slope, and landscape convexity/concavity. Appropriate CTI values can be calibrated to particular landscapes/regions by identifying existing erosion scars and setting threshold values accordingly. Areas of land which are vulnerable to severe soil erosion and at risk of being linked to proximate watercourses by uninterrupted overland flow are identified by combining the erosion information with information on their connectivity to streams (derived from topographical information and soil hydraulic properties); this allows users to identify and prioritise areas of land for sediment delivery mitigation efforts (e.g. buffer zone creation).

### Input

- **Output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input: Study area baseline folder:** Specify the path and folder where files are stored from running the **Generate Baseline** tool. 

- **CTI threshold for moderate erosion risk:** Specify the Compound Topographic Index (CTI) threshold for moderate erosion risk. *Default value is 50.*

- **CTI threshold for high erosion risk:** Specify the Compound Topographic Index (CTI) threshold for high erosion risk. *Default value is 1000.*

### Output

- **Erosion vulnerability (erosion):** This map shows areas at risk from soil erosion. Areas of "opportunity for change" have CTI values exceeding min threshold, while areas of "high opportunity for change" have CTI values exceeding max threshold.

- **Sediment delivery mitigation (seddel):** This map shows areas of land that would benefit from or be suitable for sediment delivery mitigation efforts. Areas of "opportunity" have CTI values that exceed min threshold and have an unmitigated flow connection to a watercourse, while areas of "high opportunity" have CTI values that exceed max threshold and have an unmitigated flow connection to a watercourse. Areas of "high existing value" provide protection by breaking connections of sediment sources to the stream and "marginal" areas are either at negligible risk of contributing substantial sediment or already benefit from features (land use and soil type) that intercept and hence limit sediment delivery.

## Flood Mitigation

### Summary

This tool maps areas where overland and near surface flow may accumulate as well as "Mitigating features" with the capacity to help mitigate floodsand high stream flow which may follow high intensity precipitation events. Areas with high water storage capacity and/or high infiltration capacity can help to mitigate downstream flood risk by acting as a sink for fast moving overland flow and near-surface subsurface flow; either storing this or routing the water more slowly through subsurface routes. This tool takes information about high storage and/or permeability regions from land use data and corrects flow accumulation using a bespoke algorithm - any flow that accumulates into these mitigating areas is removed from the flow accumulation data and treated as of low priority (mitigation already exists). The tool also calculates the average flow delivery to all points in the river and lake networks, to estimate water supply services.All land use or types that provide flood mitigation are treated as having high existing values; these include woodland, wetland, bog, marsh, scrub and similar natural cover. Areas where a large amount of unmitigated flow mayoccur are treated as priority areas for change. Parameters to define where flow exceeds a threshold for priority can be specified, with default parameters provided.

As input, this tool requires stream network data, a hydrologically consistent digital elevation model (consistent with the stream network and with local depressions removed) and land use data. These inputs are accessed from the folder generated by the **Generate Baseline** tool.

### Input

- **Output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input: Study area baseline folder:** Specify the path and folder where files are stored from running the **Generate Baseline** tool. 

- **Lower threshold for flood mitigation opportunity (relative upstream area caught):** Water accumulation threshold value for land to be considered a significant pathway for transporting water to the stream network. The threshold is specified as a multiplier of the area e.g. if a value of 5 is provided, all land cells that do not have significant mitigation potential (i.e. high permeability and water storage capacity) and that accumulate flow more than 5 times their area from uphill contributions, are considered significant pathways and targets for potential mitigation. These thresholds are used to generate classified maps, to identify areas to target with mitigating interventions, and to evaluate improvement opportunities for synergy and trade-off analysis. *Default value is 5.*

- **Lower threshold for very high flood mitigation opportunity (relative upstream area caught):** Water accumulation threshold value for land to be considered a very significant pathway for transporting water to the stream network. The threshold is specified as a multiplier of the area and works in the same way as the previous threshold, but checks for more significant pathways. These are considered highly important target areas for potential mitigation. *Default value is 20.*

### Output

- **Flood mitigation classification (mitclass):** This map shows the mitigation classification of the current soil/landuse. Areas that are providing mitigation of flow (e.g., trees, ponds, deep permeable soils or other flow sinks) are shown as pale green, areas that receive mitigation (i.e. water and other mass originating there later flow through mitigated areas before reaching a stream, lake or river) are shown as orange, and areas with low permeability and/or storage that do NOT flow through a mitigated area are shown as red. Potential sources of error include inaccuracies in land use input data or LUCI classification of land cover as mitigating or not-mitigating, as well as failure to account for soil permeability. 

- **Flood interception classification (scenflood):** This map shows the flood mitigation layer. High priority areas for targeting modifications are those where unmitigated flood generating land concentrates flow accumulation, and there is potential to make modifications that significantly improve water holding capacity, infiltration capacity, etc. red areas show areas of high flow concentration (large contributing area with no mitigation) and where landscape could benefit from mitigation; areas with negligible flow concentration are shown as orange and areas that are providing mitigation of flow (e.g., trees, ponds, deep permeable soils or other flow sinks) are shown as green. Potential sources of error include inaccuracies in land use input data or LUCI classification of land cover as mitigating or not-mitigating. Failure to account for storage capacity of deep soils in non-wetland areas, or faster runoff in urban areas with paved surface may reduce accuracy of mapping of areas of high and low flood concentration. 

- **Classified average water flow (avgflow_class):** Classified version of average water flow created for display purposes (feature class). Subject to same sources of error as the non-classified version. Accuracy is dependent on the use of representative precipitation data, and the approach used to calculate estimated potential evapotranspiration. Changes in land use which will affect evapotranspiration must be considered. Routing is modelled based on topography and river maps, so any inaccuracies in these may also be important.

## Habitat Connectivity (BEETLE)

### Summary

The habitat connectivity tool can be applied for identification of suitable areas for habitat expansion and protection. The tool follows a cost-distance approach to evaluating habitat connectivity, following the approach outlined by Forest Research's BEETLE project (Biological and Environmental Evaluation Tools for Landscape Ecology). LUCI automates this approach, and uses Forest Research's parameters for selected habitats of interest; see Watts et al. (2010), Eycott et al. (2007a), Eycott et al. (2007b) for further information on the approach and its parameterisation.

It is currently only available for UK applications. The approach can be applied for both "generic focal" and actual species of interest, according to the data available and parameters implemented. The application here is for generic focal woodland species; output is therefore reliant on the parameterisation for these species, as well as the accuracy of user-input landcover data

### Input


- **Output folder:** Specify the path and folder where output from this tool should be stored.

- **Input:** Study area baseline folder: Specify the path and folder where files are stored from running the **Generate Baseline** tool.

- **Species of interest:** Specify the species whose habitat connectivity is being modelled. Currently this model defaults to 11 for broadleaved woodland generic focal species. Parameterisation for further species will take place according to LUCI project needs. *Default value is 11.*

- **Minimum area for focal network (ha):** Minimum area (in hectares) for a feature to be considered large enough to provide significant habitat for species of interest. *Default value set to 2ha.*

- **Maximum cost distance through hostile terrain (km):** Maximum cost distance that can be travelled through hostile terrain, in km. This cost distance is a function of distance and permeability of hostile habitats to species of interest. Default was based on work with stakeholders in Pontbren, comparing mapped output for values between 1 and 5. *Default value set to 2.5km.*

### Output

- **Habitat connectivity for the species of interest (habconn):** This map shows in dark green the areas of existing habitat of interest. Pale green shows other priority areas of other habitat which is not the habitat of interest being considered but are a priority to conserve. Orange areas show where habitat establishment is possible but exceed the maximum cost-distance travelled. Habitat established here would not be connected to existing habitat of interest. Red areas show areas currently accessible to the species of interest; establishing new habitat in this area would act to extend the existing habitat. It is not saying that the entire red area needs to be established with the habitat of interest; rather it is showing the maximal extent within which new habitat would be connected to existing habitat. Establishing habitat at this edge of this extent will improve connectivity because the distance travelled across `hostile' terrain to get to this patch is within the maximum cost-distance through hostile terrain threshold. Outside of this extent, too much hostile terrain would need to be travelled and therefore would not improve connectivity. Patches of existing habitat of interest which are below the minimum area for focal network are not considered large enough to be a priority to improve habitat connectivity.

## Habitat Suitability
### Summary

The habitat suitability tool uses information on soil type, including soil water holding capabilities, water accumulation potential, geology, estimated water table level, slope and climate as appropriate to evaluate suitable areas for habitat extension or creation according to specific habitat requirements. It is currently only available for UK applications. ### Input

### Input

- **Output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input: Study area baseline folder:** Specify the path and folder where files are stored from running the Generate Baseline tool. 

- **Habitat of interest:** Specify the habitat of interest. 
    
    - *1: calcaerous grassland*
    
    - *2: wet grassland/wetland establishment*

### Output

- **Habitat suitability (habsuit):** This map shows areas which are suitable for habitat extension/habitat based on catchment physical properties.

## Nitrogen

### Summary

The fate of nitrogen in LUCI is currently modelled using an export coefficient approach. The tool combined topographic routing and effective precipitation to calculate the accumulation of water flow over the landscape and delivery to all points in the river and lake networks. The cumulative N export is also computed for every point in the landscape, based on the export associated with the land cover and/or land management classification for each grid cell. The ratio of the estimates of cumulative total nitrogen (TN) export and cumulative flow are then calculated to provide an estimate of the annual average accumulated TN concentration.

The current export coefficients included in LUCI databases are estimates of export of total N, rather than dissolved N. Hence the proportion of assumed particulate vs dissolved needs to be entered as a parameter in this approach. Note that the export coefficients do not account for point sources such as from sewage treatment works and septic tanks. These sources are not presently included in the LUCI water quality layer, so model output may be considered indicative of agricultural contribution to water quality issues. Any additional contribution from urban areas and point sources must be taken into account when the model is applied for predictive assessment of water quality against, for example, water framework directive criteria.

The export coefficients were originally calculated at small-catchment scale. At a finer scale, for example looking at an individual 5m square with no surface drainage, the simulated concentrations cannot reliably be taken as an indication of TN concentrations in soil water. However, once hillslope scale aggregation within LUCI is achieved (as has happened by the time loadings reach water bodies), the scale is consistent with the N loading data

### Input



- **Output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input: Study area baseline folder:** Specify the path and folder where files are stored from running the **Generate Baseline** tool. 

- **Proportion dissolved vs particulate:** Specify the proportion of N expected to be in dissolved rather than particulate form. *Default value is 0.8.*

- **N concentration threshold 1 (mg/l):** Specify the threshold in milligrams per litre (mg/L) below which accumulated N concentration is to be considered of no concern. In the absence of site-specific information and requirements, 5mg/L is suggested, based on World Health Organisation recommendation of maximum concentration of 11.3mg/L for drinking water. *Default value is 5mg/L.*

- **N concentration threshold 2 (mg/l):** Specify the threshold in milligrams per litre (mg/L) above which accumulated N concentration is to be considered of significant concern. In the absence of site specific information and requirements, 10mg/L is suggested based on World Health Organisation recommendation of maximum concentration of 11.3mg/L N for drinking water. *Default value is 10mg/L.*

- **N critical load threshold 1 (kg/yr):** Specify the threshold in kilograms N per year (kg/yr) below which accumulated N load is considered of no concern. In the absence of site specific information or requirements, 0.1kg/yr is suggested. *Default value is 0.1kg/yr.*

- **N critical load threshold 2 (kg/yr):** Specify the threshold in kilograms N per year (kg/yr) above which accumulated N load is considered of significant concern. In the absence of site specific information or requirements, 1kg/yr is suggested. *Default value is 1kg/yr.*

- **Root zone to stream attenuation factor:** Specify the proportion of accumulated N remaining in the water that is routed to the stream. This parameter reflects N loss from attenuation in the rooting zone. Values from 0 to 1 are appropriate. The value should be set to reflect the proportion of accumulated N remaining in the water routed to the stream. **Note:** Not currently being used in the UK version. *Default value is 0.5.*

- **In-stream attenuation factor:** Specify the proportion of in-stream N which remains in the water i.e. it is not consumed by in-stream processes. This parameter allows consideration of N loss from attenuation in the river network. The default value for New Zealand is based on values extracted from the OVERSEER tool Trodahl et al. (2016). *Default value is 0.5.*

- **Calculate stream statistics (load, concentration and flow accumulation - average and at exit points):** Check box to ensure in-stream statisitcs are calculated. 

- **Only generate load (i.e. stop tool once load has been generated):** Check to generate load only. **Note:** very few users will wish to take this option. *Default is unchecked.*

### Output

Within the output folder are additional output files showing instream nutrient concentration, input to lakes, and concentrations at the lake outlet.



- **Nitrogen load (N_load):** This map shows the total nitrogen load (in kg/ha/yr) generated at any point within the landscape. Accuracy reflects that of the input data on land use and the relevant LUCI export coefficient. 

- **Nitrogen accumulated load (N_AccLoad):** This map shows the accumulated total N load (in kg/yr), considering the load not just at a point, but also that contributed from "uphill" sources. High values are prime targets for mitigation / interception opportunities. Again, accuracy reflects that of the input data on land use and the relevant LUCI export coefficient, as well as the DEM and topographic routing approach used to model accumulation. 

- **Nitrogen accumulated load (classified) (N_CL_AccLoad):** This map combines the predictions of accumulated N load with user specified thresholds, to categorise the N loading into very low to very high categories. 

- **Nitrogen in-stream concetration (N_StrConc):** This map shows total N concentration (in mg/L) at all points in-stream. High values suggest catchment of this point should be targeted for mitigation/interception opportunities. This map is subject to errors in the input (or modelled intermediate) spatial data layer for the river network, in addition to any sources of inaccuracy in the modelled accumulated terrestrial N concentration. 

- **Classified nitrogen concentration in water (N_StrConcClass):** This map combines the predictions of N stream concentration with the user specified thresholds, to categorise the concentration into very low to very high categories. 

- **Nitrogen input to lakes (N_LakeStats):** This polygon feature class shows estimates of annual average loading and concentration entering lakes from land management only. No sewage etc currently considered. This output subject to the same sources of error as the in-stream value. 

- **Nitrogen at lake outlet (N_LakeOutlet):** This point feature class is the same as N_LakeStats but presents information at lake outlet only. 

- **Stream entry and exit points (entryexitpoints):** This map shows the streams and where they enter/exit the study area. 

- **Stream watersheds (watersheds):** For each of the streams in the study area, this map shows the contributing watershed to that stream.

## Phosphorus

### Summary

The fate of phosphorus in LUCI is currently modelled using an export coefficient approach. The tool combined topographic routing and effective precipitation to calculate the accumulation of water flow over the landscape and delivery to all points in the river and lake networks. The cumulative P export is also computed for every point in the landscape, based on the export associated with the land cover and/or land management classification for each grid cell. The ratio of the estimates of cumulative total phosphorus (TP) export and cumulative flow are then calculated to provide an estimate of the annual average accumulated TP concentration.

The current export coefficients included in LUCI databases are estimates of export of total P, rather than dissolved P. Hence the proportion of assumed particulate vs dissolved needs to be entered as a parameter in this approach. Note that the export coefficients do not account for point sources such as from sewage treatment works and septic tanks. These sources are not presently included in the LUCI water quality layer, so model output may be considered indicative of agricultural contribution to water quality issues. Any additional contribution from urban areas and point sources must be taken into account when the model is applied for predictive assessment of water quality against, for example, water framework directive criteria.

The export coefficients were originally calculated at small-catchment scale. At a finer scale, for example looking at an individual 5m square with no surface drainage, the simulated concentrations cannot reliably be taken as an indication of TP concentrations in soil water. However, once hillslope scale aggregation within LUCI is achieved (as has happened by the time loadings reach water bodies), the scale is consistent with the P loading data. 
### Input

- **Output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input:** Study area baseline folder:** Specify the path and folder where files are stored from running the **Generate Baseline** tool. 

- **Proportion dissolved vs particulate:** Specify the proportion of P expected to be in dissolved rather than particulate form. *Default value is 0.3.*

- **P critical accumulation threshold 1 (mg/l):** Specify the threshold in milligrams per litre (mg/L) below which accumulated P concentration is to be considered of no concern (oligotrophic). In the absence of site-specific information and requirements, 0.025mg/L is suggested, based on guidance from Dodds et al. (1998). *Default value is 0.025mg/L.*

- **P critical accumulation threshold 2 (mg/l):** Specify the threshold in milligrams per litre (mg/L) above which accumulated P concentration is to be considered of no more than moderate concern (mesotrophic). In the absence of site-specific information and requirements, 0.075mg/L is suggested, based on guidance from Dodds et al. (1998). *Default value is 0.075mg/L. P critical load threshold 1 (kg/yr):** Specify the*threshold in kilograms P per year (kg/yr) below which accumulated P load is considered of no concern. In the absence of site-specific information or requirements, 0.01kg/yr is suggested. *Default value is 0.01kg*yr. 

- **P critical load threshold 2 (kg/yr):** Specify the threshold in kilograms P per year (kg/yr) above which accumulated P load is considered of significant concern. In the absence of site-specific information or requirements, 0.1kg/yr is suggested. *Default value is 0.1kg/yr.*

- **Root zone to stream attenuation factor:** Specify the proportion of accumulated P remaining in the water that is routed to the stream. This parameter reflects P loss from attenuation in the rooting zone. Values from 0 to 1 are appropriate. The value should be set to reflect the proportion of accumulated P remaining in the water routed to the stream. **Note:** Not currently being used in the UK version. *Default value is 0.5.*

- **In-stream attenuation factor:** Specify the proportion of in-stream P which remains in the water i.e. it is not consumed by in-stream processes. This parameter allows consideration of P loss from attenuation in the river network. For New Zealand, a value of 0.7 is suggested based on local calibration Trodahl et al. (2016). *Default value is 0.5.*

- **Calculate stream statistics (load, concentration and flow accumulation - average and at exit points):** Check box to ensure in-stream statisitcs are calculated. 

- **Only generate load (i.e. stop tool once load has been generated):** Check to generate load only. **Note:** very few users will wish to take this option. *Default is unchecked.*

### Output

Within the output folder are additional output files showing instream nutrient concentration, input to lakes, and concentrations at the lake outlet.



- **Phosphorus load (P_load):** This map shows the total P load (in g/ha/yr) generated at any point within the landscape. 

- **Phosphorus accumulated load (P_AccLoad):** This map shows the accumulated total P load (in g/yr), considering the load not just at a point, but also that contributed from "uphill" sources. High values are prime targets for mitigation / interception opportunities. 

- **Phosphorus accumulated load (classified) (P_CL_AccLoad):** This map combines the predictions of accumulated P load with user specified thresholds, to categorise the N loading into very low to very high categories. 

- **Phosphorus in-stream concetration (P_StrConc):** This map shows total P concentration (in mg/L) at all points in-stream. High values suggest catchment of this point should be targeted for mitigation/interception opportunities. This map is subject to errors in the input (or modelled intermediate) spatial data layer for the river network, in addition to any sources of inaccuracy in the modelled accumulated terrestrial P concentration. 

- **Phosphorus concentration in water (P_StrConcClass):** This map combines the predictions of P stream concentration with the user specified thresholds, to categorise the concentration into very low to very high categories. 

- **Phosphorus input to lakes (P_LakeStats):** This polygon feature class shows estimates of annual average loading and concentration entering lakes from land management only. No sewage etc currently considered. This output subject to the same sources of error as the in-stream value. 

- **Phosphorus at lake outlet (P_LakeOutlet):** This point feature class is the same as P_LakeStats but presents information at lake outlet only. 

- **Stream entry and exit points (entryexitpoints):** This map shows the streams and where they enter/exit the study area. 

- **Stream watersheds (watersheds):** For each of the streams in the study area, this map shows the contributing watershed to that stream.

## RUSLE

### Summary

This tool estimates the annual soil loss (tons/km2/yr) using the Revised Universal Soil Loss Equation (RUSLE) approach, and sediment delivery vulnerability depending on whether the soil loss is occurring on non-mitigated land. There are multiple approaches to calculating the rainfall erosivity and the slope length-steepness factor.

### Input



- **Output folder:** Specify the path and folder where output from this tool should be stored. 

- **Input:** Study area baseline folder: Specify the path and folder where files are stored from running the **Generate Baseline** tool. 

- **Lower threshold for medium erosion risk (tonnes/km2):** Specify in tonnes/km2/yr the lower threshold of medium soil erosion. *Default is 250.*

- **Lower threshold for high erosion risk (tonnes/km2):** Specify in tonnes/km2/yr the lower threshold of high soil erosion. The default value is based on the unsustainable value of soil loss defined by (**?**). *Default is 500.*

- **Lower threshold for extreme erosion risk (tonnes/km2):** Specify in tonnes/km2/yr the lower threshold of extreme soil erosion. *Default is 1000.*

- **R-factor: Choose method:** Two options are used to estimate rainfall erosivity: 

    - (Klik et al., 2015) is formulated for New Zealand applications and uses different values for a-constant and b-constant depending on the study area's region within NZ. Please specify the values for the a-constant and b-constant below. 

    - (?) produced a global R-factor layer that can be freely downloaded. Please clip and reproject this layer to the study area for input in the parameter below. 

- **R-factor: a constant and b constant:** These constants can be taken from Klik et al. (2015). 

- **R-factor layer from Panagos et al. (2017):** Specify the path and filename of the rainfall erosivity raster that has been clipped and reprojected for the study area. 

- **LS-factor:** Choose method: Two options are used to estimate slope length and steepness: 

    - *Calculate based on slope and length only:* This method only accounts for slope length and steepness as specified by (**?**). 

    - *Include upslope contributing area:* This method includes slope length, steepness, and upslope contributing area as specified by (**?**) and (**?**). 

- **LS-factor:** Cutoff slope angle (degrees): Specify the cutoff angle for calculating the LS-factor. Beyond this slope angle, only rock is expected to be found with no soil on the surface. The value of 26.6 degrees or 50% was suggested by Panagos et al. (2015). *Default value is 26.6.*

### Output

- **Soil loss (tons/km2/yr):** This map shows soil loss from zero to the maximum loss. 

- **Soil loss risk:** This map shows soil loss risk based on the user-defined thresholds set in the inputs. 

    - Low erosion risk 

    - Medium erosion risk 

    - High erosion risk 

    - Extreme erosion risk 

    - Water body 

- **Sediment delivery:** This map shows which areas are vulnerable to sediment delivery based on their location on non-mitigated land. The classification used is: 

    - Mitigating features 

    - Negligible delivery to stream 

    - Moderate delivery to stream 

    - Water body 