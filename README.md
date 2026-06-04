# Normalizing the *Historico-Etymological Dataset on Obstruent-Lateral Clusters in Ibero-Romance*

> **⚠ Work in Progress**
> This repository documents an ongoing normalization process and is in an early state. The content and structure described here are subject to change and will be updated as the project develops.

## Overview

This repository contains the ongoing work to restructure and normalize the historico-etymological dataset on obstruent-lateral (OL) clusters in Ibero-Romance, originally compiled and published as a single spreadsheet (García-Covelo 2026).

The normalization project restructures the original `corpus_olclusters.csv` into a relational schema (comprising several main, lookup, and junction tables) in order to eliminate information redundancy, enforce label consistency, dissolve multidimensional cell values, and improve querability and analytical coverage of the data.

Once this process is finished, the normalized dataset will be formally released on Zenodo.

## Important note on the data files
Any version of `corpus_olclusters.csv` in this repository is a working copy undergoing active revision ans should not be cited. Changes relative to the original are documented. The original citable dataset is available on Zenodo:

García-Covelo, Andrea. 2026. *Historico-etymological dataset on the development of obstruent-lateral clusters in Ibero-Romance* (Version 1.0) [Dataset]. 10.5281/zenodo.18818049

## Related resources

**Dissertation (compilation and analysis):**
García-Covelo, Andrea. 2025. *The development of obstruent plus lateral clusters in Ibero-Romance: a historical-phonetic approach to cluster palatalization*. PhD dissertation. LMU München: Fakultät für Sprach- und Literaturwissenschaften. 10.5282/edoc.36176

**Related papers**:
(to be added)

## Repository structure and file contents

```
├── README.md                   - This file
├── code                        - Python scripts restructuring the original corpus_olclusters into 
                                main, lookup, and junction tables.
├── data                        - corpus_olclusters.csv (unmodified version in Zenodo: 10.5281/zenodo.18818049)
├── output/                     - Output (different tables) of the scripts in code
```

## License

This dataset is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Version history

- **v1.0** (2026): Original single-table dataset (https://doi.org/10.5281/zenodo.18818049).
- **v2.0** *(forthcoming)*: Normalized relational version.
