# Upper Yangtze blue–green water: selected source data

Source data accompanying *Hydroclimatic background regulates blue–green water responses to climate and land-use change in the Upper Yangtze River Basin* (manuscript dated 28 October 2026).

This compact deposit contains a spatial index for Figure 1, simulated monthly flow and aggregate evaluation metrics for Figure 2, derived numerical data for Figures 3–16, scenario definitions, basic model settings and lightweight calculation-check scripts. It supports inspection of deposited results and selected calculations rather than a complete SWAT rerun.

## Contents and use

- `data/`: Figure 1 spatial index; Figure 2 simulated series and metrics; Figures 3–16 derived numerical tables. No raw streamflow observations or GIS backgrounds.
- `config/`: 49 P–T scenarios, six prescribed land-use conversions and 24 GCM–SSP combinations.
- `MODEL_CONFIGURATION.md`: basic settings and Supplementary Information references.
- `DATA_GUIDE.md`: data blocks, units and limitations.
- `scripts/check_results.py`: checksum and selected numerical-calculation checks.
- `scripts/check_streamflow.py`: simulation coverage and optional fit checks using separately supplied observations.
- `SOURCE_PROVENANCE.csv`, `DATA_INVENTORY.json`, `SHA256SUMS.csv`: source provenance and file integrity.

Run with Python 3.11 or later, using only the standard library:

```text
python scripts/check_results.py
python scripts/check_streamflow.py
```

These scripts check files and selected calculations; they do not run SWAT, reproduce climate bias correction, recompute wavelet significance or recreate publication layouts. Figure 2 fit metrics require separately obtained observed–simulated pairs for recalculation; the default check verifies simulation coverage only.

## Complementary materials

The article's Supplementary Information contains Tables S1–S7 and Figures S1–S12. In particular, Tables S1–S3 report parameter definitions and physical bounds, archived sensitivity statistics, fitted CUP adjustments and final applied physical values; Table S4 provides streamflow evaluation and calibration uncertainty; Tables S5–S7 cover bias-correction evaluation, representative years and regional water use/consumption. These materials are not duplicated here.

Additional model files, full forcing and scenario inputs, upstream processing scripts, supplementary-figure source tables and large model outputs can be requested from the corresponding author identified in the article. Original hydrological observations and other third-party data remain subject to their providers' access and redistribution conditions; their omission from this deposit does not imply unrestricted author redistribution.

This deposit retains source numerical strings and reduces redundant metadata. Missing cells are not zero. GIS polygons, raw hydrological observations, daily station archives, climate NetCDF files, executables, model-run folders and internal manuscript correspondence are not included.
