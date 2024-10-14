# Tabla Datos Ejemplo

| Fecha    | ID Cliente (4 dígitos)     | Tipo de Cliente    | Cant KW consumidos en el dia. |
| ------------ | ------------ | ------------ | ------------ |
| 1/8/24      | 3245       | RESIDENCIAL      | 25 |
| 1/8/24      | 4700      | COMERCIO       | 32 |
| 5/8/24      | 1000      | ESTATAL       | 63 |
| 16/8/24      | 8587      | ESTATAL       | 150 |

Aclaraciones: 

- Cada cliente, tiene que tener las 28/29/30/31 muestras correspondientes, una por cada mes (depende el mes y año ingresado, se sabrá cuantos días tiene el mes) 
- No puede un mismo cliente tener mas de un tipo de cliente.  El cliente es del mismo tipo durante todo el mes.  
- El ID de cliente es un numero de 4 dígitos, comenzando desde 1000 hasta 9999. 
- La empresa tiene como mínimo 100 clientes al mes y como máximo 300.  Depende cada mes.  
- La cantidad de KW consumidos por día es de un mínimo de 10 hasta un máximo de 200. 
- Los datos serán generados por números al azar ya que la carga manual se complejiza para la ejecución. Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos. 
- La cantidad de clientes, el mes y el año serán leídos por teclado, luego a partir de esa información, se generan los datos al azar. 