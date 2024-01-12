# Machine Learning-Based Prediction of Thermal Properties of Sedimentary Rocks from Well-Log Data
### Abstract <br />
In this study, equations are developed that predict for synthetic sedimentary rocks (clastics,
carbonates and evapourates) thermal properties comprising thermal conductivity, speciﬁc heat
capacity and thermal diffusivity.

Keyword: Downhole methods; Heat ﬂow; Sedimentary basin processes; Heat generation and transport; Europe. 

### Guide <br />
<hr />
<p align="center">
  <img width="800" src="https://github.com/Hamid-Reza-Mousavi/SHC-TC-TD-Prediction-using-petrophysical-well-logs/blob/main/img/fig-guide.jpg" />
</p>

${\color{red} ONE-Log}$   <br />
1-  ['RHOB'] <br />
2-  ['PHIN'] <br />
3-  ['VSH']<br />
4-  ['U'] <br />
5-  ['DT'] <br />
6-  ['AI'] <br />
<br />
${\color{red} TWO-Log}$	 <br />
7-  ['RHOB', 'PHIN'] <br />
8-  ['RHOB', 'VSH'] <br />
9-  ['RHOB', 'U'] <br />
10- ['RHOB', 'DT'] <br />
11- ['RHOB', 'AI'] <br />
12- ['PHIN', 'VSH'] <br />
13- ['PHIN', 'U'] <br />
14- ['PHIN', 'DT'] <br />
15- ['PHIN', 'AI'] <br />
16- ['VSH', 'U'] <br />
17- ['VSH', 'DT'] <br />
18- ['VSH', 'AI'] <br />
19- ['U', 'DT'] <br />
20- ['U', 'AI'] <br />
21- ['DT', 'AI'] <br />
<br />
${\color{red} THREE-Log}$	 <br />
22- ['RHOB', 'PHIN', 'VSH'] <br />
23- ['RHOB', 'PHIN', 'U'] <br />
24- ['RHOB', 'PHIN', 'DT'] <br />
25- ['RHOB', 'PHIN', 'AI'] <br />
26- ['RHOB', 'VSH', 'U'] <br />
27- ['RHOB', 'VSH', 'DT'] <br />
28- ['RHOB', 'VSH', 'AI'] <br />
29- ['RHOB', 'U', 'DT'] <br />
30- ['RHOB', 'U', 'AI'] <br />
31- ['RHOB', 'DT', 'AI'] <br />
32- ['PHIN', 'VSH', 'U'] <br />
33- ['PHIN', 'VSH', 'DT'] <br />
34- ['PHIN', 'VSH', 'AI'] <br />
35- ['PHIN', 'U', 'DT'] <br />
36- ['PHIN', 'U', 'AI'] <br />
37- ['PHIN', 'DT', 'AI'] <br />
38- ['VSH', 'U', 'DT'] <br />
39- ['VSH', 'U', 'AI'] <br />
40- ['VSH', 'DT', 'AI'] <br />
41- ['U', 'DT', 'AI'] <br />
<br />
${\color{red} FOUR-Log}$	 <br />
42- ['RHOB', 'PHIN', 'VSH', 'U'] <br />
<hr />
** Carbonates >>> Top SHC for each model (For Six-log) **

| Model                                         | R2          | MAE            |      RMS       | 
|-----------------------------------------------|:----------: |--------------- |----------------|
| LinearRegression                              | **0.9980**  | **23.8965**    | **30.642**     | 
| Polynomial regression (degree=2)              | **0.9993**  | **13.4732**    | **17.808**     |
| XGB                                           | **0.9999**  | **1.4636**     | **2.4706**     | 

** Carbonates >>> Top TC for each model (For Six-log) **

| Model                                         | R2           | MAE            |      RMS       | 
|-----------------------------------------------|:----------:  |--------------- |----------------|
| LinearRegression                              | **0.9617**   | **0.1146**     | **0.156**      | 
| Polynomial regression (degree=2)              | **0.9929**   | **0.0433**     | **0.067**      |
| XGB                                           | **0.9995**   | **0.0102**     | **0.0174**     | 


** Carbonates >>> Top TD for each model (For Six-log) **

| Model                                         | R2          | MAE           |      RMS   | 
|-----------------------------------------------|:----------: |---------------|----------------|
| LinearRegression                              | **0.9724**  | **0.0490**    | **0.069**      | 
| Polynomial regression (degree=2)              | **0.9912**  | **0.0236**    | **0.039**      |
| XGB                                           | **0.9996**  | **0.0042**    | **0.0080**     | 


