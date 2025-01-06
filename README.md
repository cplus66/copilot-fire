# copilot-fire
Use the copilot to analysis economy, stock and bond data. 

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

### Year 2000 - 2025 U.S. Bond Picture 

![US 10 year price and yield](../../blob/master/us-bond/pictures/us-10_price_yield.png)
