# Numerical source tables

CSV files are UTF-8. `data_block` separates row types in each file; unused fields are empty. Source numeric strings are retained without rounding. `SUB`/`subbasin` are model subbasin identifiers, not station IDs. `region` uses UJS (upper Jinsha), LJS (lower Jinsha), MT (Min–Tuo), JL (Jialing), WR (Wujiang), YR (upper Yangtze mainstem); Basin denotes the whole model domain.

| File | Contents |
|---|---|
| Figure_01.csv | Six hydrological stations, 271 meteorological stations, 68 subbasin centroids/areas and six regional subbasin counts. No raster or polygon geometry. |
| Figure_02_simulated.csv | 2,808 simulated monthly flows (m³/s): 348 calibration and 120 validation months per station. No observed flow values. |
| Figure_02_metrics.csv | Twelve station–period R², NSE, PBIAS and RMSE rows. Uncertainty statistics remain in Supplementary Table S4. |
| Figure_03.csv | Subbasin mean ET comparison and basin annual ET series; GLEAM-informed pan estimates are not a wholly independent validation source. |
| Figure_04.csv | Regional annual water-resource series and monthly climatologies; raw ET is used, without deprecated offset columns. |
| Figure_05.csv | Twelve wavelet summaries and 64 × 39 grid values per series; 500 AR(1) surrogates in the source analysis. |
| Figure_06.csv | Subbasin BW/GW means and trends plus diagnostic significance fields; a stored adjusted p-value does not establish that the final figure used that threshold. |
| Figure_07.csv | 49 basin P–T response nodes and 24 GCM–SSP projection points. |
| Figure_08.csv | Four P–T corners × 68 subbasins, including changes in the GW fraction. |
| Figure_09.csv | Spatial P, T and interaction coefficients and fit R-squared diagnostics. |
| Figure_10.csv | Six land-use conversions at basin and six-region scales. |
| Figure_11.csv | Regional future annual ensemble medians/minima/maxima and historical reference values. |
| Figure_12.csv | Future subbasin changes and cross-model direction agreement. |
| Figure_13.csv | BW matched outcomes, absolute basin response summaries and basin/regional interaction summaries. |
| Figure_14.csv | Corresponding GW results; unrelated resource components are omitted. |
| Figure_15.csv | 408 plotted BWSC values and the corresponding consumption and simulated outlet-water inputs. |
| Figure_16.csv | 408 plotted GWSC values with archived display flags; undefined/near-zero-denominator flags must be retained. |

`_mm` denotes millimetres of water or, for `sw_mean_mm`, mean soil-water state. `_pct` denotes percentage change; `delta_GWC` is an unscaled change in GW/(BW+GW), not a percentage. Trend units are specified by `_per_year`; Figure 9 P coefficients are per 10 percentage points of precipitation perturbation and T coefficients per 1 °C. BWSC and GWSC are dimensionless. Figure 15 consumption, outlet water and available water are m³; `available_water_m3 = 0.2 * outlet_Q_volume_m3`.

In Figures 13–14, Y00 is historical climate/baseline land use, Y01 historical climate/changed land use, Y10 future climate/baseline land use, and Y11 future climate/changed land use. Climate = Y10−Y00; historical land-use effect = Y01−Y00; interaction = Y11−Y10−Y01+Y00; total = Y11−Y00. The matched rows include 144 cases at each of seven scales (Basin and six regions). Basin absolute summaries concern the 144 Basin cases; interaction summaries use six-model medians/minima/maxima for each SSP/conversion/scale. Full model ranges are not confidence intervals; sign disagreement is not a significance test.

Figure 15 panels are mean 2006–2020, wet 2014, normal 2008, dry 2015, wettest 2020, and driest 2006. The mean panel is not the arithmetic mean of annual BWSC. Full annual inputs are retained by the authors but not included in this compact deposit. No regional sum of reach outlet flow should be inferred.

In Figure 1, hydrological point coordinates use `longitude`/`latitude`; meteorological points use `LONG`/`LAT`; subbasin centroids use `centroid_lon_E`/`centroid_lat_N`. Coordinates are decimal degrees east/north as recorded in the source, without a new coordinate transformation. Centroids are spatial indices, not observations or raster pixels. Without polygons and elevation rasters this index cannot recreate the complete map.

Figure 2 panels a–f are Shigu (reach57), Pingshan (53), Gaochang (39), Wulong (55), Beibei (27) and Yichang (28). Aggregate metrics retain source precision; the article rounds them. Original observed monthly flow is not bundled; its redistribution status must be established with the providers. To recompute metrics using separately obtained observations, run `python scripts/check_streamflow.py --pairs path/to/pairs.csv`. Required columns are `period`, `station_en`, `observed_m3_s`, `simulated_m3_s`; periods are `calibration` or `validation`, flows are m³/s, and inputs must cover the corresponding station-period months. PBIAS = 100 × (sum(observed)−sum(simulated))/sum(observed), following the archived metrics. P/R-factor cannot be recalculated from a single trajectory and are not recomputed by the script.

The numerical tables support inspection of final results; they exclude basemap pixels/polygons, raw flow/weather observations, all individual simulations and full upstream computation inputs. Supplementary-figure source tables remain outside this compact deposit; published supporting results are in the article/Supplementary Information.
