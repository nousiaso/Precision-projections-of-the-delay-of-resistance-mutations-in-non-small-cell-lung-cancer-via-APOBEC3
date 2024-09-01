# Precision projections of the delay of resistance mutations in non-small cell lung cancer via APOBEC3A suppression
The code (along with Supplementary files and Figures) that was used for the analyses of the Precision projections of the delay of resistance mutations in non-small cell lung cancer via APOBEC3A suppression, using cancereffectsizeR a software package developed from Mandell, J. D., Cannataro, V. L. & Townsend, J. P. of the Townsend lab at the Department of Biostatistics, Yale School of Public Health.

R studio is suggested to be installed with the latest R version. While R studio is not mandatory it makes the process easier.

Install cancereffectsizeR following the instructions at https://townsend-lab-yale.github.io/cancereffectsizeR/ . Additional libraries are widely used R packages like dplyr and ggplot.
The data that are needed to run the analyses are downloaded via R code in the .rmd script therefore, having installed all necessary libraries the user can just run the code and produce the results. Open the APOBEC.rmd file with R studio and follow the instructions.

Some parts of the code need to be run multiple times altering the input file name in the .rmd script to generate different output files.
Please read the comments denoted with # in the APOBEC.rmd script slowly and diligently. Some parts of the code contain commented out code, this code should be ignored.

For the ones that would like to delve deeper into cancereffectsizeR this is the paper: Mandell, J. D., Cannataro, V. L. & Townsend, J. P. Estimation of Neutral Mutation Rates and Quantification of Somatic Variant Selection Using cancereffectsizeR. Cancer Res. 83, 500–505 (2023).
