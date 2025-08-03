# Thermal-property profiles from well-logs in sedimentary rocks: a physically informed Machine-Learning based prediction tool (`ThermoProfiler`)
## Overview
<h1>
  Thermal-property profiles from well-logs in sedimentary rocks: a physically informed Machine-Learning based prediction tool (<code>ThermoProfiler</code>)
  <a href="https://doi.org/10.1093/gji/ggaf260">
    <img src="https://img.shields.io/badge/DOI-10.1093%2Fgji%2Fggaf260-blue" alt="DOI">
  </a>
</h1>
Predicting thermal properties such as thermal conductivity, specific heat capacity, and thermal diffusivity is crucial for understanding heat flow in subsurface environments, particularly in sedimentary rock formations. These properties are essential for applications in geothermal energy, hydrocarbon exploration, and underground storage systems. Accurate predictions of thermal properties from well-log data enhance the ability to model subsurface temperature distributions, which are vital for assessing the viability of geothermal resources and optimizing drilling operations. The ThermoProfiler, a machine learning-based prediction tool, leverages well-logs to generate precise thermal-property profiles. By integrating physical principles with advanced machine learning techniques, ThermoProfiler provides a reliable and efficient method to estimate these critical thermal properties, ultimately aiding in the effective management and utilization of subsurface energy resources.

## Guide
1- Create virtual environment (⚠️ python 3.9.12): <br />
```
python -m venv thermal-venv
```
```
thermal-venv\Scripts\activate
```
2- Install below versions library: <br />
```
pip install pandas
```
```
pip install numpy
```
```
pip install joblib==1.2.0
```
```
pip install matplotlib==3.8.1
```
```
pip install scikit-learn==1.2.1
```
```
pip install xgboost==1.6.1
```
3- Add venv to ipykernel (if use jupyter notebook) <br />
```
pip install ipykernel
```
```
python -m ipykernel install --user --name=thermal-venv
```
### Examples
Find multiple examples under:
[https://github.com/Hamid-Reza-Mousavi/SHC-TC-TD-Prediction-using-petrophysical-well-logs/tree/main/notebook
](https://github.com/Hamid-Reza-Mousavi/SHC-TC-TD-Prediction-using-petrophysical-well-logs/tree/main/notebook
)

<p align="center">
  <img width="800" src="https://github.com/Hamid-Reza-Mousavi/SHC-TC-TD-Prediction-using-petrophysical-well-logs/blob/main/img/fig-guide1.jpg" />
</p>

${\color{red} 1-Log}$   <br />
1-  ['RHOB'] <br />
2-  ['PHIN'] <br />
3-  ['VSH']<br />
4-  ['Vp'] <br />
<br />
${\color{red} 2-Log}$	 <br />
5-  ['RHOB', 'PHIN'] <br />
6-  ['RHOB', 'VSH'] <br />
7-  ['RHOB', 'Vp'] <br />
8-  ['PHIN', 'VSH'] <br />
9-  ['PHIN', 'Vp'] <br />
10- ['VSH', 'Vp'] <br />
<br />
${\color{red} 3-Log}$	 <br />
11- ['RHOB', 'PHIN', 'VSH'] <br />
12- ['RHOB', 'PHIN', 'Vp'] <br />
13- ['RHOB', 'VSH', 'Vp'] <br />
14- ['PHIN', 'VSH', 'Vp'] <br />
<br />
${\color{red} 4-Log}$	 <br />
15- ['RHOB', 'PHIN', 'VSH', 'Vp'] <br />

## Acknowledgments
This research was partially supported by Iran University of Science & Technology (IUST) and by the German project ThermoBase (BGE).


