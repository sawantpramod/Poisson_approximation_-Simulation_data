# Poisson_approximation_-Simulation_data
The Data Decoder: Discrete, Continuous, and the Two Distributions Everyone Misuses
From a 20-student classroom to a live e-commerce store-a practical walkthrough of binomial, Poisson, and the normality tests most analysts get wrong.
I see the same mistake year after year. Students and junior analysts obsess over which statistical test to run, without first asking the far more fundamental question: "What kind of data am I actually holding?"
This single distinction-discrete vs. continuous-dictates everything, from the type of graph you build to the mathematical engine under your hypothesis test. Ignore it, and you are not just getting a homework problem wrong; you are mispricing risk, burning payroll, and chasing false alarms.
Connect With Me
If you found this analysis valuable:
Share your thoughts in the comments
Connect with me on Medium.com

Footnote: Strictly speaking, the exact calculation uses the Binomial PMF with n=150, p=0.02. The Poisson approximation (λ=np=3) is used here because n is large (>50) and p is small (<0.1), yielding a result accurate to within a fraction of a percentage point-perfectly acceptable for business decisions.
# The Data Decoder: Discrete, Continuous, and the Two Distributions Everyone Misuses

## 🎯 Purpose
This repository contains reproducible code and data for the article **"The Data Decoder: Discrete, Continuous, and the Two Distributions Everyone Misuses"** - a practical guide to understanding Binomial, Poisson distributions, and normality testing.

## 📊 What's Included

### Code Files
- **Frequency Distribution** - Visualize and analyze classroom exam scores
- **Normality Tests** - Shapiro-Wilk and Kolmogorov-Smirnov implementations
- **E-Commerce Analysis** - Poisson and Binomial modeling for sales data
- **Approximation Breakdown** - When Poisson approximates Binomial poorly
- **Full Analysis** - Complete reproducible pipeline

### Data
- `ecommerce_poisson_binomial_dataset.csv` - 500 hours of simulated e-commerce data

### Outputs
- Charts and visualizations
- Statistical test results
- Simulation data

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/yourusername/data-decoder-reproducible.git
cd data-decoder-reproducible
pip install -r requirements.txt
