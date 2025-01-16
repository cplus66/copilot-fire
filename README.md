# copilot-fire
Use the copilot to analysis economy, stock and bond data. 

## Chart

### World Top 5 Revenue

![World Top 5 Revenue](../../blob/master/world-revenue/pictures/world-revenue.png)

### World Top 5 Debt

![World Top 5 Revenue](../../blob/master/world-debt/pictures/world-debt.png)

### U.S. Accounting

![U.S. Accounting](../../blob/master/us-account/pictures/us-account.png)

### U.S. Debt

![U.S. Debt](../../blob/master/us-debt/pictures/us-debt.png)

### U.S. Revenue

![U.S. Revenue](../../blob/master/us-revenue/pictures/us-revenue.png)

### U.S. Debt and 10-year Bond Yeild Rate

![U.S. Debt and 10-year Bond Yeild Rate](../../blob/master/us-debt/pictures/us-debt-10-year-bond.png)

### Year 2000 - 2025 U.S. Bond Picture

![US 10 year price and yield](../../blob/master/us-bond/pictures/us-10_price_yield.png)

### Year 2015 - 2024 U.S. Bond Yield and Exchange Rate to NTD (New Taiwan Dollars)

![US 10 year yield and exchange rate Taiwan](../../blob/master/us-bond/pictures/us-bond-exchange-ntd.png)

### U.S. Inflation Rate Monthly

![US Inflation Rate Monthly](../../blob/master/us-inflation/pictures/us-inflation-rate-monthly.png)

### U.S. CPI(Consumer Price Index) Monthly

![US CPI Monthly](../../blob/master/us-inflation/pictures/us-cpi-monthly.png)

### U.S. USD to EUR Exchange Rate

![USD to EUR Exchange Rate Quarterly](../../blob/master/us-dollar-index/pictures/exchange-rate-usd-to-eur-quarter.png)

### U.S. USD to NTD Exchange Rate

![USD to NTD Exchange Rate Quarterly](../../blob/master/us-dollar-index/pictures/exchange-rate-usd-to-ntd-quarterly.png)

## Taiwan Stock

### Required Python Library

```
pip install twstock
```

### Prompt

* Show current taiwan stock market prices.
* Please provide the source code to show current stock prices in Taiwan.
* The code shows error message "AttributeError: 'Stock' object has no attribute 'name'".


## U.S. Bond 

### Required Python Library

```
pip install pandas
pip install matplotlib
pip install pandas_datareader
```

### Prompt

* List US bond price.
* List US 10 year bond price during 2000 to today.
* Could you share the code to me?
* It shows error message below ModuleNotFoundError: No module named 'pandas'.
* Coud we get the price and yield from library instead of using data array?
* Sorry, it shows the following error message ModuleNotFoundError: No module named 'pandas_datareader'.
* Could you use matplotlib to generate the chart for US 10-year treasury bonds?
* Could you also add bond price in the same chart?
* Sorry, it shows the following error message ValueError: All arrays must be of the same length.

## U.S. Inflation Rate and CPI

### Required Python Library

```
pip install fredapi
```

## U.S. Dollars Index

### Required Python Library

```
pip install alpha_vantage
```

## Analysis

### Bond Yields

- Interest Rates: When central banks, like the Federal Reserve, adjust interest rates, bond yields often follow. Higher interest rates typically lead to higher bond yields as new bonds are issued at these higher rates.
- Inflation: Rising inflation erodes the purchasing power of future bond payments, leading investors to demand higher yields to compensate for this risk.
- Economic Growth: Strong economic growth can lead to higher bond yields as investors expect higher inflation and interest rates in the future.
- Investor Sentiment: When investors are optimistic about the economy, they may sell bonds in favor of riskier assets, driving bond prices down and yields up. Conversely, during economic uncertainty, investors may flock to bonds, pushing prices up and yields down.
- 利率：當聯準會等中央銀行調整利率時，債券殖利率通常也會隨之調整。由於新債券以較高的利率發行，因此較高的利率通常會導致較高的債券收益率。
- 通貨膨脹：通貨膨脹上升會侵蝕未來債券支付的購買力，導致投資者要求更高的收益率來補償這種風險。
- 經濟成長：強勁的經濟成長可能帶來更高的債券殖利率，因為投資人預期未來通膨和利率將會上升。
- 投資人情緒：當投資人對經濟感到樂觀時，他們可能會拋售債券，轉而購買風險較高的資產，導致債券價格下跌、殖利率上升。相反，在經濟不確定時期，投資者可能會湧向債券，導致價格上漲而殖利率下降。

### Exchange Rates

- Interest Rate Differentials: Differences in interest rates between countries can drive exchange rates. Higher interest rates in the U.S. can attract foreign capital, increasing demand for the USD and raising its value relative to other currencies.
- Economic Indicators: Indicators such as GDP growth, employment rates, and trade balances can influence exchange rates. Strong economic performance in the U.S. can boost the USD against other currencies.
- Political Stability: Political events and stability can impact investor confidence. Political uncertainty can lead to currency depreciation as investors seek safer assets.
- Market Sentiment: Investor perceptions and speculative activities can also drive exchange rates. Positive sentiment towards the U.S. economy can strengthen the USD, while negative sentiment can weaken it.
- 利率差異：國家之間的利率差異會影響匯率。美國較高的利率可以吸引外國資本，增加對美元的需求並提高其相對於其他貨幣的價值。
- 經濟指標：GDP 成長、就業率和貿易平衡等指標都會影響匯率。美國強勁的經濟表現可以提振美元兌其他貨幣的匯率。
- 政治穩定性：政治事件和穩定性會影響投資者信心。由於投資者尋求更安全的資產，政治不確定性可能導致貨幣貶值。
- 市場情緒：投資人的看法和投機活動也會影響匯率。對美國經濟的正面情緒可以推高美元，而負面情緒則會使美元貶值。
