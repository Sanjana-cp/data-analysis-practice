import numpy as np
import pandas as pd

# load dataset
df = pd.read_csv("superstore.csv", encoding="latin1")


def full_analysis():

    # basic dataset info
    shape = df.shape
    info = df.info()
    null_values = df.isnull().sum()
    duplicates = df.duplicated().sum()

    # total sales and profit
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    mean_sales = df["Sales"].mean()
    mean_profit = df["Profit"].mean()

    # region analysis
    group_region = df.groupby(by="Region")
    sales_by_region = group_region["Sales"].sum().sort_values(ascending=False)
    profit_by_region = group_region["Profit"].sum().sort_values(ascending=False)

    # sub-category analysis 
    group_sub = df.groupby(by="Sub-Category")
    sales_by_subcategory = group_sub["Sales"].sum().sort_values(ascending=False)
    profit_by_subcategory = group_sub["Profit"].sum().sort_values(ascending=False)

    # top products by sales
    group_product = df.groupby(by="Product Name")
    top_products = group_product["Sales"].sum().sort_values(ascending=False).head()

    # numpy calculations
    array = np.array(df["Sales"])

    minimum = np.min(array)
    maximum = np.max(array)

    norm = (array - minimum) / (maximum - minimum)

    sale_mean = np.mean(array)
    sale_std = np.std(array)

    zscore = (array - sale_mean) / sale_std

    # outlier detection
    out = abs(zscore)
    count = 0

    for i in out:
        if i > 3:
            count = count + 1

    # add zscore column to dataframe
    df["Sales_Zscore"] = zscore

    # save new csv file
    df.to_csv("superstore_with_zscore.csv", index=False)

    # store everything in dictionary 
    results = {
        "shape": shape,
        "null_values": null_values,
        "duplicates": duplicates,
        "total_sales": total_sales,
        "total_profit": total_profit,
        "mean_sales": mean_sales,
        "mean_profit": mean_profit,
        "sales_by_region": sales_by_region,
        "profit_by_region": profit_by_region,
        "sales_by_subcategory": sales_by_subcategory,
        "profit_by_subcategory": profit_by_subcategory,
        "top_products": top_products,
        "normalized_values": norm,
        "zscore": zscore,
        "outlier_count": count
    }

    return results


# function call
result = full_analysis()

print("Analysis Done")
# print(result)
print("Outliers found:", result["outlier_count"])
    