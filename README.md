# Machine Learning-Based Prediction of Thermal Properties of Sedimentary Rocks from Well-Log Data
### Abstract <br />
In this study, models are developed that predict for sedimentary rocks (clastics,
carbonates and evapourates) thermal properties comprising thermal conductivity, speciﬁc heat
capacity and thermal diffusivity.

Keyword: Thermal conductivity; Thermal diffusivity; Heat capacity; Machine learning; Well-logging downhole methods; Sedimentary basin 

### Guide <br />
If have problem with load model <br />
1- Create virtual envirnment: <br />
-m venv thermal-venv <br />
thermal-venv\Scripts\activate <br />
2- Install below versions library: <br />
pip install pandas==1.4.4 <br />
pip install scikit-learn==1.2.1 <br />
pip install xgboost==1.6.1 <br />
3- Add venv to ipykernel (if use jupyter notebook) <br />
pip install ipykernel <br />
python -m ipykernel install --user --name=thermal-venv <br />

<hr />
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

<hr />

