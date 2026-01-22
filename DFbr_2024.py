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
    
df_kaggle = pd.read_csv('database.csv')
df_dadosFut = pd.read_csv("dados_transfermarkt_2024.csv")

df_kaggle["nome_join"] = df_kaggle["Jogador"].str.lower().str.strip()
df_kaggle['Idade'] = df_kaggle['Idade'].apply(lambda x: str(x).split('-')[0])
df_dadosFut["nome_join"] = df_dadosFut["Name"].str.lower().str.strip()
df_precos_limpo = df_dadosFut.drop_duplicates(subset=['nome_join'], keep='first')

cols_numericas = ['Gols','xG','Assis.','xAG','Bloqueios']
for col in cols_numericas:
    df_kaggle[col] = pd.to_numeric(df_kaggle[col], errors='coerce').fillna(0)
        
df_stats_limpo = df_kaggle.groupby('nome_join').agg({
    'Gols': 'sum',
    'xG': 'sum',
    'Assis.': 'sum',
    'xAG': 'sum',
    'Bloqueios': 'sum',
    'Time': 'first',
    'Idade': 'first'
}).reset_index()      