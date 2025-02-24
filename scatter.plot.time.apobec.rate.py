import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from matplotlib.ticker import LogLocator, FuncFormatter

# Patient identifiers
patients = ["MGH086", "MGH953", "TH067_E7", "TH29_Post", "TH287E2", "TH171_E3",
           "TH016E3", "TH079E2", "TH11_post_2", "TH153E3",
           "TH74_2", "TH51_A2", "TH019E5", "MGH987", "MGH808"]

# Apobec rate average values
apobec_rate_average = np.array([
    2.40E-05,  # MGH086
    1.77E-06,  # MGH953
    7.70E-06,  # TH067_E7
    5.34E-06,  # TH29_Post
    6.27E-06,  # TH287E2
    1.08E-05,  # TH171_E3
    3.03E-06,  # TH016E3
    6.04E-07,  # TH079E2
    1.82E-06,  # TH11_post_2
    2.55E-06,  # TH153E3
    1.68E-06,  # TH74_2
    1.49E-06,  # TH51_A2
    1.77E-06,  # TH019E5
    1.45E-07,  # MGH987
    1.07E-06   # MGH808
])

# Time gained values
time_gained = np.array([1073.3, 21.5, 50.4, 2.06, 37.5, 30.4, 3.26, 0.1, 0.7, 1.1,
                       1.7, 5.9, 3.5, 3.6, 3.1])

# Create figure and axis
fig, ax = plt.subplots()

# Adjusting default font sizes
plt.rcParams.update({'font.size': 14})

# Scatter plot with log scales
ax.set_xscale('log')
ax.set_yscale('log')
scatter = ax.scatter(apobec_rate_average, time_gained, color="darkviolet")

# Custom tick formatter
def format_func(value, tick_number):
    if value == 0:
        return "0"
    else:
        return r"$10^{%d}$" % np.log10(value)

# Customizing log scale ticks
ax.xaxis.set_major_locator(LogLocator(base=10.0, numticks=12))
ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=12))
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=np.linspace(2, 10, 9)/10, numticks=100))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.linspace(2, 10, 9)/10, numticks=100))
ax.xaxis.set_major_formatter(FuncFormatter(format_func))
ax.yaxis.set_major_formatter(FuncFormatter(format_func))

# Labeling axes
ax.set_xlabel('Component of mutation rate attributable to APOBEC', fontsize=14)
ax.set_ylabel('Time gained', fontsize=14)

# List of patients to annotate
patients_to_annotate = ["MGH953", "MGH808", "MGH086", "MGH987"]

# Annotating only selected points
for i, patient in enumerate(patients):
    if patient in patients_to_annotate:
        ax.annotate(patient, (apobec_rate_average[i], time_gained[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=14)

# Linear regression on log-transformed data
log_apobec = np.log10(apobec_rate_average)
log_time_gained = np.log10(time_gained)
slope, intercept, r_value, p_value, std_err = linregress(log_apobec, log_time_gained)
line = 10**(slope * log_apobec + intercept)
plt.plot(apobec_rate_average, line, linestyle='--', color='darkviolet', label=f'Fit: y = 10^({slope:.2f} * log(x) + {intercept:.2f})\np-value = {p_value:.3f}')

# Display legend
plt.legend()

# Save plot in multiple formats
plt.savefig('Figure3.pdf', format='pdf', dpi=200, bbox_inches='tight')
plt.savefig('Figure3.svg', format='svg', dpi=200, bbox_inches='tight')
plt.savefig('Figure3.png', format='png', dpi=200, bbox_inches='tight')

# Show plot
plt.show()

# Print statistical analysis
print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value**2)
print("P-value:", p_value)
print("Standard Error of the Estimate:", std_err)
print("\nPlot saved as: Figure3.pdf, Figure3.svg, and Figure3.png")
