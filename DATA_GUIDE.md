# Numerical source tables

CSV files are UTF-8. `data_block` identifies row types; unused fields are empty. `SUB`/`subbasin` identify model subbasins. Regions are UJS (upper Jinsha), LJS (lower Jinsha), MT (Min–Tuo), JL (Jialing), WR (Wujiang), YR (upper Yangtze mainstem), and Basin (whole domain).

| File | Contents |
|---|---|
| Figure_01.csv | Hydrological and meteorological station coordinates, subbasin centroids/areas, and regional subbasin counts. |
| Figure_02_simulated.csv | 2,808 simulated monthly flows (m³/s): 348 calibration and 120 validation months per station. |
| Figure_02_metrics.csv | Twelve station–period R², NSE, PBIAS and RMSE records; uncertainty statistics are in Supplementary Table S4. |
| Figure_03.csv | Subbasin ET comparisons using SWAT, GLEAM and GLEAM-informed pan-derived estimates, plus basin annual series. |
| Figure_04.csv | Regional annual water-resource series and monthly climatologies. |
| Figure_05.csv | Twelve wavelet summaries and 64 × 39 grid values per series. |
| Figure_06.csv | Subbasin BW/GW means and trends; hatching uses `p_BH_136`, the BH-adjusted `p_two_sided`. The `*_tfpw_mk_p` values are diagnostics. |
| Figure_07.csv | 49 basin P–T response nodes and 24 GCM–SSP climate points for 2021–2050 relative to 1982–2020, using the 56 SWAT input stations. |
| Figure_08.csv | Four P–T corners × 68 subbasins, including changes in the GW fraction. |
| Figure_09.csv | Spatial P, T and interaction coefficients and fitted R². |
| Figure_10.csv | Six land-use conversions at basin and six-region scales. |
| Figure_11.csv | Regional annual ensemble medians/minima/maxima and historical reference values. |
| Figure_12.csv | Future subbasin changes and cross-model direction agreement. |
| Figure_13.csv | BW matched outcomes, basin absolute summaries and basin/regional interaction summaries. |
| Figure_14.csv | Corresponding GW results. |
| Figure_15.csv | 408 BWSC panel values, consumption and simulated outlet-water inputs. |
| Figure_16.csv | 408 GWSC panel entries and display/undefined-value flags. |

## Fields and calculations

`_mm` denotes millimetres of water; `sw_mean_mm` is mean soil-water content. `_pct` denotes percentage change. `delta_GWC` is the change in GW/(BW+GW). Trend units use `_per_year`; Figure 9 coefficients use precipitation perturbations of 10% and temperature perturbations of 1°C. BWSC and GWSC are dimensionless. Figure 15 water volumes are m³, with `available_water_m3 = 0.2 * outlet_Q_volume_m3`.

For Figures 13–14, Y00 is historical climate/baseline land use, Y01 historical climate/changed land use, Y10 future climate/baseline land use, and Y11 future climate/changed land use. Climate = Y10−Y00; historical land-use effect = Y01−Y00; interaction = Y11−Y10−Y01+Y00; total = Y11−Y00. Each of seven scales has 144 matched cases. Interaction summaries give six-model medians/minima/maxima by SSP, conversion and scale.

Figure 15 panels are mean 2006–2020, wet 2014, normal 2008, dry 2015, wettest 2020 and driest 2006. The mean panel uses mean consumption divided by mean available BW over 2006–2020.

Figure 1 coordinates are decimal degrees east/north: `longitude`/`latitude` for hydrological stations, `LONG`/`LAT` for meteorological stations, and `centroid_lon_E`/`centroid_lat_N` for subbasins.

Figure 2 panels a–f are Shigu, Pingshan, Gaochang, Wulong, Beibei and Yichang. Streamflow PBIAS = 100 × (sum(observed)−sum(simulated))/sum(observed). Optional paired-data checks use `python scripts/check_streamflow.py --pairs path/to/pairs.csv`, with columns `period`, `station_en`, `observed_m3_s`, `simulated_m3_s`; periods are `calibration` or `validation`.
