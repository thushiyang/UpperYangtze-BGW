# Upper Yangtze blue–green water: source data

Source data and supporting scripts for *Hydroclimatic background regulates blue–green water responses to climate and land-use change in the Upper Yangtze River Basin*.

This repository provides numerical data for Figures 1–16, scenario definitions, basic model settings, and calculation scripts.

## Contents

- `data/`: numerical data for Figures 1–16.
- `config/`: P–T, land-use and climate scenario definitions.
- `MODEL_CONFIGURATION.md`: basic model settings.
- `DATA_GUIDE.md`: data fields and units.
- `scripts/`: calculation and data-checking scripts.
- `SOURCE_PROVENANCE.csv`, `DATA_INVENTORY.json`, `SHA256SUMS.csv`: source records, file inventory and checksums.

## Use

Python 3.11 or later:

```text
python scripts/check_results.py
python scripts/check_streamflow.py
```

## Supplementary materials

Calibration parameters and supporting evaluation results are provided in the article's Supplementary Information (Tables S1–S7 and Figures S1–S12). Additional model files and large datasets are available from the corresponding author upon reasonable request.
