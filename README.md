# Engenharia de Dados na Prática: Pipeline ETL de dados do coin market cap - Nível Iniciante 
(adaptado de https://www.youtube.com/watch?v=I8qPqbXQBDU&t=2126s)

```mermaid
graph TD
    %% Configurações Gerais para fundo claro
    accTitle: Fluxo ETL Dólar CoinMarketCap
    accDescr: Diagrama de fluxo de dados usando Airflow, Python e Postgres

    subgraph Fonte_Dados [Fonte de Dados Externa]
        CMC["fa:fa-cloud-download API CoinMarketCap"]
    end

    subgraph Orquestrador_Airflow [DAG do Apache Airflow]
        Inicio((Início)) --> ValidarAPI{Validar API?}
        
        ValidarAPI -- Sim --> Extracao[PythonOperator: Extração JSON]
        ValidarAPI -- Não --> Falha([Falha/Alerta])

        Extracao --> Transformacao[PythonOperator: Tratamento e Limpeza]
        Transformacao --> Carga[PostgresOperator: Inserção/Upsert]
        
        Carga --> Fim(Fim)
    end

    subgraph Armazenamento [Banco de Dados]
        DB[("fa:fa-database PostgreSQL")]
    end

    %% Relacionamentos e Fluxo de Dados
    CMC -.->|Requisição HTTP| Extracao
    Carga -->|Comando SQL| DB

    %% Estilização Minimalista (Fundo Branco)
    style Fonte_Dados fill:#ffffff,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style Orquestrador_Airflow fill:#ffffff,stroke:#01579b,stroke-width:2px
    style Armazenamento fill:#ffffff,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    
    style CMC fill:#fff,stroke:#333
    style DB fill:#fff,stroke:#333
    style Inicio fill:#dfd,stroke:#333
    style Fim fill:#fdd,stroke:#333
    style ValidarAPI fill:#fffbe6,stroke:#d4a017
```
## ✒️ 
Para mais informações sobre como implementar esse projeto, visite https://github.com/vbluuiza/pipeline_etl_weather_data_tutorial_youtube
