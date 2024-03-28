# Response-article-to-Hideko-Isozaki-et-al.-APOBEC3A-drives-evolution-of-persistent-cancer-cells. __Nature__ 2023
The code (along with Supplementary file 1) that was used for the analyses of the Response article to Isozaki et. al. 2023, using cancereffectsizeR a software package developed from the Townsend group at the Department of Biostatistics, Yale School of Public Health.

R studio should is advised to be installed with the latest R version. While R studio is not mandatory it makes the process easier.

Install cancereffectsizeR following the instructions at https://townsend-lab-yale.github.io/cancereffectsizeR/ . The additional libraries that are required to be installed are widely used R packages like dplyr and ggplot.
The data that are needed to run the analyses are downloaded via R code in the .rmd script therefore, having installed all necessary libraries the user can just run the code and produce the results.

Some parts of the code need to be run multiple times altering the input files to generate different output files. 
Please read the comments denoted with # in the .rmd script slowly and diligently. Some parts of the code contain commented out code, this code should be ignored.

For the ones that would like to delve deeper into cancereffectsizeR this is the paper: Mandell, J. D., Cannataro, V. L. & Townsend, J. P. Estimation of Neutral Mutation Rates and Quantification of Somatic Variant Selection Using cancereffectsizeR. Cancer Res. 83, 500–505 (2023).
