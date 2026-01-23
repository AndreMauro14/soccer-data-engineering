# ⚽ Soccer Data Engineering - Brasileirão 2024

Pipeline de coleta, limpeza e transformação de dados de jogadores do Campeonato Brasileiro 2024, integrando informações financeiras do Transfermarkt com estatísticas de performance.

## 📊 Sobre o Projeto

Este projeto implementa um **pipeline completo de ETL (Extract, Transform, Load)** para criar um dataset limpo e estruturado a partir de múltiplas fontes de dados do futebol brasileiro.

### O que foi desenvolvido:
- **Web Scraping** automatizado de valores de mercado (Transfermarkt via ScraperFC)
- **Limpeza e padronização** de dados brutos (normalização de strings, tratamento de tipos)
- **Agregação de estatísticas** por jogador (soma de gols, assistências, métricas avançadas)
- **Merge inteligente** entre bases de dados usando chaves padronizadas

---

## 🛠️ Tecnologias

- Python 3.13
- Pandas
- ScraperFC

---

## 📁 Fontes de Dados

**Transfermarkt** (`dados_transfermarkt_2024.csv`)  
Valores de mercado, nomes e posições dos jogadores

**Kaggle - Brasileirão 2024** (`database.csv`)  
Estatísticas de performance (Gols, xG, Assistências, Bloqueios, etc.)

---

## 🔄 Pipeline Implementado

### 1. Coleta
Extração automatizada de dados do Transfermarkt usando ScraperFC

### 2. Limpeza Inicial
- Normalização de nomes (lowercase + strip)
- Remoção de duplicatas
- Tratamento de idades (extração apenas do número)

### 3. Tratamento Numérico
- Conversão de colunas numéricas (Gols, xG, Assistências, etc.)
- Preenchimento de valores nulos com 0

### 4. Agregação
Agrupamento por jogador com soma de estatísticas da temporada usando `groupby().agg()`

### 5. Unificação
Merge entre base financeira e base de performance, gerando dataset final com 514 jogadores e 10 features

---

## 📊 Dataset Final

**514 jogadores** × **10 colunas**

| Coluna      | Tipo    | Descrição                    |
|-------------|---------|------------------------------|
| Name        | object  | Nome do jogador              |
| Idade       | int64   | Idade                        |
| Position    | object  | Posição                      |
| Time        | object  | Clube                        |
| Value       | object  | Valor de mercado (€)         |
| Gols        | int64   | Total de gols                |
| Assis.      | int64   | Assistências                 |
| xG          | float64 | Expected Goals               |
| xAG         | float64 | Expected Assisted Goals      |
| Bloqueios   | float64 | Bloqueios defensivos         |

---

## 👨‍💻 Autor

**André Mauro**  
Estudante de Sistemas para Internet - UNICAP  
[GitHub](https://github.com/AndreMauro14)
