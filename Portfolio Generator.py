# importing necessary packages.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from testing.models import param_sweep

# Defining a function to rate the crypto assets based on financial and sustainability parameters
def rate_assets(df):
    # List of financial parameters
    fin_params = ['Price', 'Return', 'Volatility', 'Market Cap', 'Liquidity']

    # List of sustainability parameters
    sust_params = ['Alignment to Impact Investment Definition', 'Organization', 'Strategy', 'Risk', 'Technology']

    # Calculating the financial rating
    fin_rating = df[fin_params].sum(axis=1) / len(fin_params) * 100

    # Calculating the sustainability rating
    sust_rating = df[sust_params].sum(axis=1) / len(sust_params) * 100

    # Calculating the overall rating
    df['Rating'] = (fin_rating + sust_rating) / 2 / 100

    return df


# Defining a function to weight the crypto assets based on ratings
def weight_assets(df):
    # Calculating the total rating
    total_rating = df['Rating'].sum()

    # Calculating the weight of each asset
    df['Weight'] = df['Rating'] / total_rating

    return df


# Defining a function to create the crypto assets investment portfolios
def create_portfolio(df, num_assets):
    # Creating a new dataframe to store the portfolios
    portfolio_df = pd.DataFrame()

    # Looping through the assets and creating the portfolios
    for asset in df['Asset']:
        # Filtering the dataframe by the asset
        asset_df = df[df['Asset'] == asset]

        # Adding the asset to the portfolio dataframe
        portfolio_df = pd.concat([portfolio_df, asset_df])

    return portfolio_df



# Dataframe for the crypto assets
data = {'Asset': ['MIN', 'SUNDAE', 'MELD', 'VYFI', 'AADA', 'CLAP', 'cNETA'],
        'Price': [np.random.randint(1, 100) for i in range(7)],
        'Return': [np.random.randint(1, 100) for i in range(7)],
        'Volatility': [np.random.randint(1, 100) for i in range(7)],
        'Market Cap': [np.random.randint(1, 100) for i in range(7)],
        'Liquidity': [np.random.randint(1, 100) for i in range(7)],
        'Alignment to Impact Investment Definition': [np.random.randint(1, 100) for i in range(7)],
        'Organization': [np.random.randint(1, 100) for i in range(7)],
        'Strategy': [np.random.randint(1, 100) for i in range(7)],
        'Risk': [np.random.randint(1, 100) for i in range(7)],
        'Technology': [np.random.randint(1, 100) for i in range(7)]}

# Creating the dataframe
df = pd.DataFrame(data)

# Rating the crypto assets
df = rate_assets(df)

# Weighting the crypto assets
df = weight_assets(df)

# Creating the crypto assets investment portfolios
portfolio_df = create_portfolio(df, rate_assets)

# Printing the portfolios
print(tabulate(portfolio_df, headers='keys', tablefmt='psql'))

# Plotting the portfolios
portfolio_df.plot(kind='pie', x='Asset', y='Weight')
plt.show()
