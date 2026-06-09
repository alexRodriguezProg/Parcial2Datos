# Hito 3 – Visualización Dinámica y Análisis

## Descripción

Este hito corresponde a la etapa de visualización y análisis de datos de vuelos del año 2024 (`flight_data_2024(act).csv`). 
Se trabajó con dos tecnologías de visualización: **Python (Matplotlib + Seaborn)** para gráficos estáticos y **Grafana + MySQL** para un dashboard interactivo.

##Dashboard de Grafana

<img width="1896" height="868" alt="image" src="https://github.com/user-attachments/assets/7c668e74-de6f-4a61-bce9-5245bb30d260" />

### Análisis

**Panel 1 – Top 10 Rutas Más Frecuentes**
Las rutas Hawaii dominan el ranking. La simetría entre rutas de ida y vuelta refleja un flujo equilibrado de pasajeros. JFK->LAX aparece como el corredor continental más importante.

**Panel 2 – Top 10 Ciudades de Destino**
Dallas/Fort Worth lidera con 607 vuelos, seguido de Atlanta y New York. Los tres son los principales hubs del sistema aéreo estadounidense, lo que explica su alta frecuencia como destinos.

**Panel 3 – Distribución por Aerolínea**
American Airlines (AA) domina con 2.495 vuelos, seguida de Delta (DL) con 2.027. Entre ambas concentran más del 60% del total, característica típica del mercado aéreo estadounidense.

**Panel 4 – Distancia Promedio por Estado**
Los territorios del Pacífico lideran con 2.599 millas promedio por su aislamiento geográfico. California y Washington también muestran distancias altas por su posición en la costa oeste.
