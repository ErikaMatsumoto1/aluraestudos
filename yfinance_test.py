import yfinance


def extrair_dados(ticker, start_date, end_date):
    caminho = f"/home/erikayumi/Documents/acoes/{ticker}.csv"
    hist = yfinance.Ticker(ticker).history(
        period = '1d',
        interval = '1h',
        start = start_date,
        end = end_date,
        prepost = True
    ).to_csv(caminho)


extrair_dados("AAPL", "2024-08-01", "2024-08-15")
extrair_dados("GOOG", "2024-08-16", "2024-08-31")