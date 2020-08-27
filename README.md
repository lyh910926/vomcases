# The Vegetation Optimality Model along a precipitation gradient: 
# influence of carbon costs and benefits on vegetation properties

Ecological and hydrological processes are strongly interlinked by vegetation and its properties. Models often use static values for vegetation properties, that are in reality highly dynamic, or prescribe vegetation properties based on remotely sensed data. 

The Vegetation Optimality Model (VOM, Schymanski et al., 2009) optimizes vegetation properties in order the optimize the Net Carbon Profit, i.e. the difference between the total carbon taken up by photosynthesis and all the carbon costs of the plants. The VOM schematizes perennial trees and seasonal grasses each as a single big leaf with an associated root system, and optimizes rooting depths, foliage cover, photosynthetic capacity and water use strategies. More details of the model can be found [here](https://vom.readthedocs.io/en/latest/).

In this repository, the Vegetation Optimality Model is applied along the North-Australian Tropical Transect (NATT). The NATT consists of six study sites with an increasing rainfall amount from North to South. Long-term data on evaporation and CO2-measurements are available at these sites, which are used to validate the modelling results. 


In this study, we hypothesize that:

- Conventional models capture the temporal and spatial variation of carbon and water fluxes better compared to the optimality-driven model. 

- Optimality-based prognostic dynamics of vegetation cover will lead to worse reproduction of fluxes compared to using mean monthly vegetation cover values for each site obtained from remote sensing time series. 

- Optimality-based prognostic rooting depths for each site will not result in better reproduction of carbon and water fluxes compared to a prescribed, homogeneous rooting depth. %You could just re-run the VOM with prescribed rooting depths.

- Re-calibration of water transport costs for each site will not result in a large variation of the cost parameter for these costs.

## How to use this project
This project contains all pre- and post-processing scripts for the model runs of the VOM along the NATT. All final figures are in the notebooks, as well as the supplementary analysis. These scripts can be re-used for other VOM-applications. To use this repository for your own analysis, create a free login for renku, then fork the project and modify it to your liking. Please consult the various documentation sources for [renkulab](https://renkulab.io/).


## Contents
* data/: All data used to run and evaluate the model, in addition to the model results.

    - data/boreholes/: Borehole data for several locations close to the NATT-sites, from 
    - data/data\_from_a\_model\_inter/: Raw data from the model-intercomparison study of Whitley et al. (2016).
    - data/DINGO/: Flux tower data from OzFlux 
    - data/DINGO2/: Meteorological parameters measured at the flux towers
    - data/DINGO_QC/: Quality flags of the flux data
    - data/DINGO_SWS/: Soil moisture values at the flux tower sites.
    - data/fPAR/: fPAR-data from Donohue et al. (2008), to derive vegetation cover.
    - data/img/: Final figures
    - data/MaunaLoa/: Atmosperic CO2-levels
    - data/MODIS: MODIS fPar-data for comparison with the fPar-data of Donohue et al. 
    - data/SavMIP_extracted/: Data from Whitley et al. (2016) extracted.
    - data/Silo/: Meteorological data
    - data/vegmachine/: Vegetation cover data from ...
    - data/VOM_input/: Meteorological input data for the VOM (dailyweather.prn) per study site.
    - data/VOM_output/: Results of the model runs.
    - data/VOM_soils/: Input files for the VOM containing the soil profiles per study site.
* notebooks/: all notebooks with the analysis
    - notebooks/results.ipynb: Notebook containing all the figures with the final results
    - notebooks/additional_analyses\: Notebooks containing all additional analysis
* src/: Release of the VOM used for the experiments.
* src_py/: All python pre- and post-processing scripts:
    - src_py/adj_dailyweather.py
    - src_py/plot_mass_balance.py
    - src_py/plot_smprofile.py
    - src_py/calc_vp.py
    - src_py/plot_meanannuals.py
    - src_py/plot_timeseries.py
    - src_py/sce_best_param_defaults.py
    - src_py/dingo_dailyweather.py
    - src_py/plot_meanannuals_vom.py
    - src_py/plot_vegetation.py
    - src_py/sce_best_param.py
    - src_py/model_stats.py
    - src_py/plot_model_stats.py
    - src_py/plot_water_retention_curve.py
    - src_py/sce_stats_best.py
    - src_py/plot_costfactors.py
    - src_py/plot_residuals.py
    - src_py/plot_watpot_depth.py
    - src_py/sce_stats.py
    - src_py/plot_costs_climates.py
    - src_py/plot_roots_costfactors.py
    - src_py/proc_sce2.py
    - src_py/sce_uncertainty.py
    - src_py/plot_cover.py
    - src_py/plot_roots.py
    - src_py/proc_sce_pc_restart.py
    - src_py/write_dailyweather.py
    - src_py/plot_ensembleyears.py
    - src_py/plot_rootzone_states_2.py
    - src_py/proc_sce_presc_cov.py
    - src_py/write_namelist.py
    - src_py/plot_fluxpartitions.py
    - src_py/plot_rootzone_states.py
    - src_py/proc_sce.py
    - src_py/write_pcseries_meanmonthly.py
    - src_py/plot_gw.py
    - src_py/plot_smdifferences.py
    - src_py/proc_sce_restart.py
    - src_py/write_pcseries.py

* src_sh/: All shell pre- and post-processing scripts
* work/: Work directory with all model set-ups and intermediate results.

## References

Schymanski, S.J., Sivapalan, M., Roderick, M.L., Hutley, L.B., Beringer, J., 2009. An optimality‐based model of the dynamic feedbacks between natural vegetation and the water balance. Water Resources Research 45. https://doi.org/10.1029/2008WR006841

Schymanski, S.J., Roderick, M.L., Sivapalan, M., 2015. Using an optimality model to understand medium and long-term responses of vegetation water use to elevated atmospheric CO2 concentrations. AoB PLANTS 7, plv060. https://doi.org/10.1093/aobpla/plv060
Schymanski, S.J., Sivapalan, M., Roderick, M.L., Hutley, L.B., Beringer, J., 2009. An optimality‐based model of the dynamic feedbacks between natural vegetation and the water balance. Water Resources Research 45. https://doi.org/10.1029/2008WR006841

Whitley, R., Beringer, J., Hutley, L.B., Abramowitz, G., De Kauwe, M.G., Duursma, R., Evans, B., Haverd, V., Li, L., Ryu, Y., Smith, B., Wang, Y.-P., Williams, M., Yu, Q., 2016. A model inter-comparison study to examine limiting factors in modelling Australian tropical savannas. Biogeosciences 13, 3245–3265. https://doi.org/10.5194/bg-13-3245-2016




