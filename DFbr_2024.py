import pandas as pd
import ScraperFC as sfc

scraper = sfc.Transfermarkt()

try:
    df = scraper.scrape_players(year = '2024', league = 'Brazil Serie A')
    if not df.empty:
        print("df criado e salvo")
        df.to_csv("dados_transfermarkt_2024.csv", index=False) 
    
except Exception as e:
    print(f"erro na execução: {e}")    