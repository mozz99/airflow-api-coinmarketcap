Engenharia de Dados na Prática: Pipeline ETL de dados do coin market cap - Nível Iniciante (adaptado de https://www.youtube.com/watch?v=I8qPqbXQBDU&t=2126s)

```
graph TD
    subgraph External_API [Data Source]
        CMC[CoinMarketCap API]
    end

    subgraph Airflow_Orchestrator [Airflow DAG]
        Start(Start) --> CheckAPI{Check API Availability}
        CheckAPI -- Success --> Extract[Extract JSON]
        Extract --> Transform[Clean & Format Data]
        Transform --> Load[Insert/Upsert Data]
        Load --> End(End)
    end

    subgraph Storage [Database]
        PG[(PostgreSQL)]
    end

    %% Relationships
    CMC -.->|HTTP GET / JSON| Extract
    Load -->|SQL Insert| PG

    %% Styling
    style CMC fill:#f9f,stroke:#333,stroke-width:2px
    style PG fill:#00758f,stroke:#333,stroke-width:2px,color:#fff
    style Airflow_Orchestrator fill:#e1f5fe,stroke:#01579b,stroke-dasharray
```
## ✒️ 
Para mais informações sobre como implementar esse projeto, visite https://github.com/vbluuiza/pipeline_etl_weather_data_tutorial_youtube