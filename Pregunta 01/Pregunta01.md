


## Single Responsability 

Cada clase debe tener una sola responsabilidad. El aumento de funcionalidad hace que se genere mayor acoplamiento de dos o mas funcionalidades que pueden cambiar en momentos diferentes o por razones diferentes

Como en el caso de `Main()` que realiza tres funciones: Mostrar Informacion Cines, Peliculas, Guardar entradas

## Open Close

Se deben crear clases Bases de las cuales se debe extender las demas para modificarlas.

Como es el caso de la clase `CinePlaneta` y `CineStark`. Modificar una funcionalidad en el codigo conlleva a serie de cambios en modulos dependientes y esto afecta negativamente el codigo si se encuentra muy acoplado.


## Interface Segregation

Es recomendable usar muchas interfaces pequeñas en vez de una muy grande

En el codigo las clases `Cine` pueden implementar interfaces pequeñas que vayan de acuerdo a los requerimientos de cada clase Cine
