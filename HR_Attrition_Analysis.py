# ============================================================
# HR Attrition Analysis — Python EDA & Preprocessing Script
# ============================================================
# Dataset  : IBM HR Analytics Employee Attrition & Performance
# Records  : 1,470 employees | 35 features
# Target   : Attrition (Yes / No)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Style ────────────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#0a0e1a",
    "axes.facecolor":   "#1a2235",
    "axes.edgecolor":   "#1f2d45",
    "axes.labelcolor":  "#94a3b8",
    "xtick.color":      "#64748b",
    "ytick.color":      "#64748b",
    "text.color":       "#e2e8f0",
    "grid.color":       "#1f2d45",
    "grid.linestyle":   "--",
    "grid.alpha":       0.6,
    "font.family":      "DejaVu Sans",
})
PALETTE  = ["#f43f5e", "#3b82f6", "#10b981", "#f97316", "#a855f7", "#fbbf24"]
RED, BLU, GRN, ORG, PRP, GLD = PALETTE


# ── 1. LOAD DATA ─────────────────────────────────────────────
def load_data(path: str = "HR_Attrition_Analysis.xlsx") -> pd.DataFrame:
    df = pd.read_excel(path)
    print(f"\n✅  Loaded  →  {df.shape[0]:,} rows × {df.shape[1]} columns")
    return df


# ── 2. EXPLORE ───────────────────────────────────────────────
def explore(df: pd.DataFrame):
    print("\n── Dataset Info ──────────────────────────────────")
    print(df.dtypes.value_counts().to_string())

    print("\n── Missing Values ────────────────────────────────")
    miss = df.isnull().sum()
    print(miss[miss > 0].to_string() if miss.any() else "  No missing values ✓")

    print("\n── Attrition Distribution ────────────────────────")
    vc = df["Attrition"].value_counts()
    pct = df["Attrition"].value_counts(normalize=True) * 100
    print(pd.DataFrame({"Count": vc, "Percent": pct.round(2)}).to_string())

    print("\n── Numeric Summary ───────────────────────────────")
    print(df.describe().round(2).to_string())


# ── 3. PREPROCESS ────────────────────────────────────────────
def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Binary encode target
    df["AttritionBinary"] = (df["Attrition"] == "Yes").astype(int)

    # Bin tenure
    df["TenureBand"] = pd.cut(
        df["YearsAtCompany"],
        bins=[0, 2, 5, 10, 20, 100],
        labels=["0–2 yrs", "3–5 yrs", "6–10 yrs", "11–20 yrs", "20+ yrs"],
        right=True,
    )

    # Bin age
    df["AgeBand"] = pd.cut(
        df["Age"],
        bins=[17, 24, 30, 35, 40, 45, 50, 55, 100],
        labels=["18–24", "25–30", "31–35", "36–40", "41–45", "46–50", "51–55", "55+"],
    )

    # Bin income
    df["IncomeBand"] = pd.cut(
        df["MonthlyIncome"],
        bins=[0, 2000, 4000, 6000, 10000, 999999],
        labels=["<$2K", "$2–4K", "$4–6K", "$6–10K", "$10K+"],
    )

    # Overtime binary
    df["OvertimeBinary"] = (df["OverTime"] == "Yes").astype(int)

    print("\n✅  Preprocessing complete — new columns added:")
    new_cols = ["AttritionBinary", "TenureBand", "AgeBand", "IncomeBand", "OvertimeBinary"]
    for c in new_cols:
        print(f"    • {c}")

    return df


# ── 4. KPI SUMMARY ───────────────────────────────────────────
def print_kpis(df: pd.DataFrame):
    total       = len(df)
    churned     = df["AttritionBinary"].sum()
    rate        = churned / total * 100
    retained    = total - churned
    avg_income  = df["MonthlyIncome"].mean()
    churn_inc   = df[df["AttritionBinary"] == 1]["MonthlyIncome"].mean()

    print("\n" + "═" * 50)
    print("  HR ATTRITION — KEY METRICS")
    print("═" * 50)
    print(f"  Total Employees   : {total:,}")
    print(f"  Attrition Count   : {churned:,}")
    print(f"  Attrition Rate    : {rate:.1f}%")
    print(f"  Retained          : {retained:,}  ({100-rate:.1f}%)")
    print(f"  Avg Monthly Income: ${avg_income:,.0f}")
    print(f"  Avg Income (Left) : ${churn_inc:,.0f}")
    print("═" * 50)


# ── 5. VISUALISATIONS ────────────────────────────────────────

def _bar(ax, x, y, color=None, title="", xlabel="", ylabel="", pct=False, horizontal=False):
    colors = color if isinstance(color, list) else [color or BLU] * len(x)
    if horizontal:
        bars = ax.barh(x, y, color=colors, height=0.6, edgecolor="none")
        ax.set_xlabel(ylabel or "")
    else:
        bars = ax.bar(x, y, color=colors, width=0.6, edgecolor="none")
        ax.set_ylabel(ylabel or "")
    ax.set_title(title, fontsize=12, fontweight="bold", pad=10)
    if not horizontal:
        ax.set_xlabel(xlabel or "")
    if pct:
        ax.yaxis.set_major_formatter(mticker.PercentFormatter())
    ax.spines[["top", "right"]].set_visible(False)
    return bars


def plot_overview(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("Attrition Overview", fontsize=16, fontweight="bold", y=1.02)

    # Donut
    ax = axes[0]
    sizes = df["Attrition"].value_counts()
    wedges, texts, autotexts = ax.pie(
        sizes, labels=sizes.index, autopct="%1.1f%%",
        colors=[RED, GRN], startangle=90,
        wedgeprops=dict(width=0.55, edgecolor="#0a0e1a"),
    )
    for t in autotexts: t.set_fontsize(11); t.set_color("white")
    ax.set_title("Overall Attrition Rate", fontsize=12, fontweight="bold")

    # By Department
    dept = df.groupby("Department")["AttritionBinary"].mean() * 100
    _bar(axes[1], dept.index, dept.values,
         color=[RED, BLU, PRP],
         title="Attrition Rate by Department", ylabel="Rate (%)", pct=True)

    # By Job Role
    role = (df.groupby("JobRole")["AttritionBinary"].mean() * 100
              .sort_values(ascending=True).tail(7))
    _bar(axes[2], role.index, role.values,
         color=[RED if v > 25 else ORG if v > 15 else GLD for v in role.values],
         title="Attrition Rate by Job Role", ylabel="Rate (%)", horizontal=True)

    plt.tight_layout()
    plt.savefig("plot_overview.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.show()
    print("  📊 Saved: plot_overview.png")


def plot_demographics(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Demographics Analysis", fontsize=16, fontweight="bold")

    # Gender
    gen = df.groupby("Gender")["AttritionBinary"].mean() * 100
    _bar(axes[0, 0], gen.index, gen.values, color=[BLU, RED],
         title="Attrition Rate by Gender", ylabel="Rate (%)", pct=True)

    # Marital Status
    mar = df.groupby("MaritalStatus")["AttritionBinary"].mean() * 100
    _bar(axes[0, 1], mar.index, mar.values, color=[ORG, PRP, GRN],
         title="Attrition Rate by Marital Status", ylabel="Rate (%)", pct=True)

    # Education Field
    edu = (df.groupby("EducationField")["AttritionBinary"].mean() * 100
             .sort_values(ascending=False))
    _bar(axes[1, 0], edu.index, edu.values,
         color=[RED if v > 20 else ORG if v > 15 else GRN for v in edu.values],
         title="Attrition Rate by Education Field", ylabel="Rate (%)", pct=True)
    axes[1, 0].tick_params(axis="x", rotation=30)

    # Age Band
    age = df.groupby("AgeBand", observed=True)["AttritionBinary"].mean() * 100
    _bar(axes[1, 1], age.index.astype(str), age.values, color=BLU,
         title="Attrition Rate by Age Band", ylabel="Rate (%)", pct=True)

    plt.tight_layout()
    plt.savefig("plot_demographics.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.show()
    print("  📊 Saved: plot_demographics.png")


def plot_tenure(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("Tenure & Career Analysis", fontsize=16, fontweight="bold")

    # Tenure histogram
    axes[0].hist(df["YearsAtCompany"], bins=20, color=BLU, edgecolor="#0a0e1a", alpha=0.85)
    axes[0].set_title("Tenure Distribution (Histogram)", fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Years at Company")
    axes[0].set_ylabel("Employee Count")
    axes[0].spines[["top", "right"]].set_visible(False)

    # Tenure band vs attrition (line-ish via bar)
    ten = df.groupby("TenureBand", observed=True)["AttritionBinary"].mean() * 100
    axes[1].plot(ten.index.astype(str), ten.values, color=RED, marker="o",
                 linewidth=2.5, markersize=8)
    axes[1].fill_between(range(len(ten)), ten.values, alpha=0.15, color=RED)
    axes[1].set_title("Attrition Rate by Tenure Band", fontsize=12, fontweight="bold")
    axes[1].set_ylabel("Attrition Rate (%)")
    axes[1].yaxis.set_major_formatter(mticker.PercentFormatter())
    axes[1].spines[["top", "right"]].set_visible(False)

    # Years since last promotion
    promo = df["YearsSinceLastPromotion"].value_counts().sort_index().head(10)
    _bar(axes[2], promo.index.astype(str), promo.values, color=PRP,
         title="Years Since Last Promotion", xlabel="Years", ylabel="Count")

    plt.tight_layout()
    plt.savefig("plot_tenure.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.show()
    print("  📊 Saved: plot_tenure.png")


def plot_churn_factors(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Churn Factor Analysis", fontsize=16, fontweight="bold")

    # Overtime
    ot = df.groupby("OverTime")["AttritionBinary"].mean() * 100
    _bar(axes[0, 0], ot.index, ot.values, color=[GRN, RED],
         title="Attrition Rate: Overtime vs No Overtime", ylabel="Rate (%)", pct=True)

    # Income Band
    inc = df.groupby("IncomeBand", observed=True)["AttritionBinary"].mean() * 100
    _bar(axes[0, 1], inc.index.astype(str), inc.values,
         color=[RED if v > 25 else ORG if v > 15 else GRN for v in inc.values],
         title="Attrition Rate by Income Band", ylabel="Rate (%)", pct=True)

    # Business Travel
    trav = df.groupby("BusinessTravel")["AttritionBinary"].mean() * 100
    _bar(axes[1, 0], trav.index, trav.values, color=[GRN, ORG, RED],
         title="Attrition Rate by Business Travel", ylabel="Rate (%)", pct=True)

    # Work-Life Balance
    wlb = df.groupby("WorkLifeBalance")["AttritionBinary"].mean() * 100
    _bar(axes[1, 1], wlb.index.astype(str), wlb.values,
         color=[RED, ORG, GRN, BLU],
         title="Attrition Rate by Work-Life Balance (1=Bad, 4=Best)",
         ylabel="Rate (%)", pct=True)

    plt.tight_layout()
    plt.savefig("plot_churn_factors.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.show()
    print("  📊 Saved: plot_churn_factors.png")


def plot_heatmap(df: pd.DataFrame):
    pivot = df.pivot_table(
        values="AttritionBinary", index="Department",
        columns="JobLevel", aggfunc="mean"
    ) * 100

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.heatmap(
        pivot, annot=True, fmt=".1f", cmap="RdYlGn_r",
        linewidths=0.5, linecolor="#0a0e1a",
        ax=ax, cbar_kws={"label": "Attrition Rate (%)"},
    )
    ax.set_title("Heatmap: Department × Job Level Attrition Rate (%)",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Job Level")
    ax.set_ylabel("Department")
    plt.tight_layout()
    plt.savefig("plot_heatmap.png", dpi=150, bbox_inches="tight",
                facecolor="#0a0e1a")
    plt.show()
    print("  📊 Saved: plot_heatmap.png")


def plot_correlation(df: pd.DataFrame):
    num_cols = [
        "Age", "MonthlyIncome", "YearsAtCompany", "TotalWorkingYears",
        "YearsSinceLastPromotion", "YearsWithCurrManager", "NumCompaniesWorked",
        "PercentSalaryHike", "JobSatisfaction", "EnvironmentSatisfaction",
        "WorkLifeBalance", "JobInvolvement", "OvertimeBinary", "AttritionBinary",
    ]
    corr = df[num_cols].corr()

    fig, ax = plt.subplots(figsize=(12, 9))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm",
        center=0, linewidths=0.4, linecolor="#1f2d45",
        ax=ax, annot_kws={"size": 8},
    )
    ax.set_title("Correlation Matrix — HR Attrition Features",
                 fontsize=13, fontweight="bold", pad=12)
    plt.tight_layout()
    plt.savefig("plot_correlation.png", dpi=150, bbox_inches="tight",
                facecolor="#0a0e1a")
    plt.show()
    print("  📊 Saved: plot_correlation.png")


def print_insights(df: pd.DataFrame):
    print("\n" + "═" * 55)
    print("  TOP INSIGHTS")
    print("═" * 55)

    # Highest churn role
    role_rate = df.groupby("JobRole")["AttritionBinary"].mean() * 100
    top_role  = role_rate.idxmax()
    print(f"  🔴 Highest Churn Role  : {top_role} ({role_rate.max():.1f}%)")

    # OT vs non-OT
    ot_yes = df[df["OverTime"] == "Yes"]["AttritionBinary"].mean() * 100
    ot_no  = df[df["OverTime"] == "No"]["AttritionBinary"].mean() * 100
    print(f"  🔴 Overtime Attrition  : {ot_yes:.1f}% vs {ot_no:.1f}% (no OT)")

    # Tenure risk
    t0 = df[df["YearsAtCompany"] <= 2]["AttritionBinary"].mean() * 100
    print(f"  🔴 0–2 yr Tenure Risk  : {t0:.1f}%")

    # Marital status
    mar = df.groupby("MaritalStatus")["AttritionBinary"].mean() * 100
    print(f"  🟡 Single Churn Rate   : {mar.get('Single', 0):.1f}%")
    print(f"  🟢 Married Churn Rate  : {mar.get('Married', 0):.1f}%")

    # Income
    low_inc = df[df["MonthlyIncome"] < 2000]["AttritionBinary"].mean() * 100
    print(f"  🔴 Low Income (<$2K)   : {low_inc:.1f}% attrition rate")

    # Dept
    dept = df.groupby("Department")["AttritionBinary"].mean() * 100
    print(f"  🟡 Sales Dept Rate     : {dept.get('Sales', 0):.1f}%")
    print(f"  🟢 R&D Dept Rate       : {dept.get('Research & Development', 0):.1f}%")
    print("═" * 55 + "\n")


# ── MAIN ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  HR ATTRITION ANALYSIS  —  Python EDA Script")
    print("=" * 55)

    df_raw  = load_data("HR_Attrition_Analysis.xlsx")
    explore(df_raw)

    df = preprocess(df_raw)
    print_kpis(df)
    print_insights(df)

    print("\n📊 Generating visualisations …\n")
    plot_overview(df)
    plot_demographics(df)
    plot_tenure(df)
    plot_churn_factors(df)
    plot_heatmap(df)
    plot_correlation(df)

    print("\n✅  All plots saved as PNG files.")
    print("🌐  Open HR_Attrition_Dashboard.html in your browser for the interactive version.\n")
