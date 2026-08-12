"""
E-Commerce Deep Dive — Poisson Meets Binomial
----------------------------------------------------
Matches the article's revised scenario:
  - Traffic:    ~150 visitors/hour (lambda = 150)
  - Conversion: 2% historical conversion rate (p = 0.02)
  - Because n is large and p is small, sales/hour ~ Poisson(lambda_sales = n*p = 3)

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# ----------------------------------------------------------------------
# Scenario parameters
# ----------------------------------------------------------------------
LAMBDA_VISITORS = 150     # average visitors/hour
P_CONVERT = 0.02          # historical conversion rate
LAMBDA_SALES = LAMBDA_VISITORS * P_CONVERT  # = 3, the Poisson approx rate
N_HOURS = 500

# ----------------------------------------------------------------------
# The "zero sales" panic, quantified and corrected
# ----------------------------------------------------------------------
p_zero_exact = stats.binom.pmf(0, n=LAMBDA_VISITORS, p=P_CONVERT)   # exact
p_zero_approx = stats.poisson.pmf(0, mu=LAMBDA_SALES)               # approx

p_zero_2_in_a_row = p_zero_approx ** 2
p_zero_3_in_a_row = p_zero_approx ** 3

print("=" * 65)
print("THE 'ZERO SALES' PANIC")
print("=" * 65)
print(f"P(0 sales in ONE hour)      exact Binomial : {p_zero_exact:.4%}")
print(f"P(0 sales in ONE hour)      Poisson approx : {p_zero_approx:.4%}")
print(f"-> ~1 in {1/p_zero_approx:.0f} hours. Unlucky, but common -- expect")
print(f"   it at least once most days.\n")
print(f"P(0 sales, 2 CONSECUTIVE hours) : {p_zero_2_in_a_row:.4%}  (~1 in {1/p_zero_2_in_a_row:,.0f})")
print(f"P(0 sales, 3 CONSECUTIVE hours) : {p_zero_3_in_a_row:.4%}  (~1 in {1/p_zero_3_in_a_row:,.0f})")
print(f"-> THIS is the real signal: a single quiet hour is noise,")
print(f"   three quiet hours in a row is a genuine red flag.\n")

# ----------------------------------------------------------------------
# "Exactly 5 sales this hour": exact Binomial vs Poisson approx
# ----------------------------------------------------------------------
p_five_exact = stats.binom.pmf(5, n=LAMBDA_VISITORS, p=P_CONVERT)
p_five_approx = stats.poisson.pmf(5, mu=LAMBDA_SALES)

print("=" * 65)
print("EXACT VS. APPROXIMATE: P(exactly 5 sales in the hour)")
print("=" * 65)
print(f"Exact Binomial(n=150, p=0.02) : {p_five_exact:.4%}")
print(f"Poisson(lambda=3) approx      : {p_five_approx:.4%}")
print(f"-> Nearly identical -- this is 'Binomial approximates Poisson")
print(f"   when n is large and p is small' made concrete.\n")

# ----------------------------------------------------------------------
# Combined dataset: hourly traffic (Poisson) feeds hourly
# sales (Binomial conditioned on that hour's actual visitor count)
# ----------------------------------------------------------------------
hourly_visitors = np.random.poisson(lam=LAMBDA_VISITORS, size=N_HOURS)
hourly_sales = np.random.binomial(n=hourly_visitors, p=P_CONVERT)

combined_df = pd.DataFrame({
    "hour_id": range(1, N_HOURS + 1),
    "visitors": hourly_visitors,
    "sales": hourly_sales,
})
combined_df["conversion_rate"] = (combined_df["sales"] / combined_df["visitors"]).round(4)
combined_df.to_csv("ecommerce_poisson_binomial_dataset_v2.csv", index=False)
print(f"Saved dataset -> ecommerce_poisson_binomial_dataset_v2.csv")
print(f"Simulated avg sales/hour: {hourly_sales.mean():.2f} (target lambda_sales={LAMBDA_SALES})")

# ----------------------------------------------------------------------
# Charts
# ----------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Panel 1: Exact Binomial vs Poisson approximation overlay
x = np.arange(0, 13)
pmf_binom = stats.binom.pmf(x, n=LAMBDA_VISITORS, p=P_CONVERT)
pmf_pois = stats.poisson.pmf(x, mu=LAMBDA_SALES)

axes[0].bar(x - 0.2, pmf_binom, width=0.4, label="Exact Binomial(150, 0.02)", color="#4C72B0")
axes[0].bar(x + 0.2, pmf_pois, width=0.4, label="Poisson approx (λ=3)", color="#DD8452")
axes[0].set_title("Sales per Hour: Exact vs. Poisson Approximation")
axes[0].set_xlabel("Sales in the hour")
axes[0].set_ylabel("Probability")
axes[0].legend()

# Panel 2: Probability of N consecutive zero-sales hours
n_consec = np.arange(1, 6)
p_consec = p_zero_approx ** n_consec
axes[1].bar(n_consec, p_consec, color="#55A868")
for xi, yi in zip(n_consec, p_consec):
    axes[1].text(xi, yi, f"{yi:.3%}", ha="center", va="bottom", fontsize=9)
axes[1].set_title("How Rare Is a Zero-Sales Streak?")
axes[1].set_xlabel("Consecutive zero-sales hours")
axes[1].set_ylabel("Probability")
axes[1].set_xticks(n_consec)

plt.tight_layout()
plt.savefig("poisson_binomial_chart_v2.png", dpi=150)
print("Saved chart   -> poisson_binomial_chart_v2.png")
