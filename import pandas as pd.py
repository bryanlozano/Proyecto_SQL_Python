import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

conexion = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=LAPTOP-BRYAN;'
    'DATABASE=Proyecto;'
    'Trusted_Connection=yes;'
)

print("Conexión exitosa")


query = """
SELECT TOP 10
    u.PROVINCIA,
    round(AVG(f.PROMEDIO_FINAL),2) AS promedio
FROM Fact_Egresados f
JOIN Dim_Ubicacion u ON f.UBIGEO = u.UBIGEO
GROUP BY u.PROVINCIA
ORDER BY promedio DESC
"""
df = pd.read_sql(query, conexion)

plt.figure(figsize=(10,6))
plt.bar(df['PROVINCIA'], df['promedio'])

plt.xticks(rotation=45)
plt.title('Top 10 Países con Más Ventas')
plt.xlabel('País')
plt.ylabel('Ventas')

plt.show()