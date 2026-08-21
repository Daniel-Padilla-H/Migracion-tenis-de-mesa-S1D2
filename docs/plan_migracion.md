# Plan de migración de MATLAB a Python

## 1. Objetivo de la migración

Convertir el script de MATLAB en un proyecto Python modular, documentado y verificable. Posteriormente, sus funciones se usarán desde un notebook interactivo con *sliders*, sin duplicar la lógica física.

## 2. Descripción del código original

El archivo simula durante 1.5 s el vuelo de una pelota de tenis de mesa mediante pasos de 0.005 s. Considera gravedad, arrastre aerodinámico, efecto Magnus, amortiguamiento de la rotación, rebote con la mesa y una colisión simplificada con la red. También anima una escena 3D con la mesa, la red, la pelota y vectores de velocidad/aceleración, y genera gráficas temporales de posición, velocidad, orientación y velocidad angular.

## 3. Entradas y condiciones iniciales

| Parámetro | Valor original | Unidad declarada | Función dentro de la simulación |
|---|---:|---|---|
| `ball_mass` | 2.7 | g | Masa de la pelota. |
| `ball_radius` | 20.25 | mm | Radio de la pelota y umbral de contacto con la mesa/red. |
| `ball_rot_inertia` | `2/3·m·r²` | g·mm² | Inercia rotacional. |
| `table_restitution` | 0.77 | sin unidad | Pérdida de velocidad vertical en el rebote. |
| `net_restitution` | 0.5 | sin unidad | Amortiguamiento al colisionar con la red. |
| `drag` | 2.7 | mN/(mm/s) | Fuerza de arrastre lineal. |
| `rot_drag` | 350.0 | mN·mm/(rad/s) | Torque de arrastre rotacional. |
| `magnus` | 0.01 | mN/(mm/s²) | Escala de la fuerza de Magnus. |
| `table_friction` | 0.25 | proporción | Acopla velocidad lineal y angular durante el rebote. |
| `table_length`, `table_width`, `table_height` | 2740, 1525, 760 | mm | Geometría de la mesa. |
| `net_height`, `net_extra` | 152.5, 180 | mm | Geometría y extensión lateral de la red. |
| `g` | 9800 | mm/s² | Aceleración gravitacional. |
| `dt` y `t` | 0.005; `0:dt:1.5` | s | Paso y horizonte temporal. |
| `x(:,1)` | `[0; 762.5; 1065]` | mm | Posición inicial. |
| `v(:,1)` | `[7000; -3000; -3000]` | mm/s | Velocidad inicial. |
| `omega(:,1)` | `[0; 0; 75]·2π` | rad/s | Velocidad angular inicial. |
| `animate`, `plot_period`, `yaw`, `pitch` | `true`, 5, -45, `23,5` | —, pasos, grados, grados | Configuración de la animación y la cámara. |

## 4. Variables de salida

Con 301 instantes de tiempo, las salidas principales son arreglos de dimensión `(3, 301)` en MATLAB: `t` tiene dimensión `(1, 301)`; `x` es posición (mm), `v` velocidad (mm/s) y `a` aceleración (mm/s²); `theta` es orientación acumulada (rad), `omega` velocidad angular (rad/s) y `alpha` aceleración angular (rad/s²). Cada fila representa los ejes x, y y z.

## 5. Problemas identificados en el código original

- Mezcla responsabilidades: parámetros, integración, colisiones, animación y gráficas están en un único archivo.
- Los parámetros están codificados directamente y no se pueden cambiar de forma controlada.
- Las constantes geométricas de mesa, red y radio se duplican en la función de dibujo.
- `pitch = 23,5` usa una coma; en MATLAB esto no representa de forma segura el decimal 23.5 y puede producir un vector o un comportamiento no previsto.
- Hay inconsistencias o ambigüedades de unidades, especialmente en los coeficientes de arrastre, torque y Magnus; las gráficas convierten mm a m, pero no normalizan el modelo completo.
- El rebote con la mesa detecta penetración después del paso de integración, no comprueba la dirección de impacto y usa una aproximación simple para fricción y giro.
- La colisión con la red solo refleja/amortigua la componente x y la rotación; no calcula normal de contacto, penetración ni geometría detallada.
- La animación vuelve a dibujar superficies, líneas y vectores en cada muestra, por lo que puede acumular objetos y degradar el rendimiento.
- No existen pruebas automatizadas que validen dimensiones, fuerzas, colisiones o equivalencia numérica.

## 6. Estrategia de migración

Primero se conservará el comportamiento numérico original como línea base y se documentarán sus defectos. Las correcciones físicas o mejoras se realizarán posteriormente de forma separada y trazable, evitando corregir silenciosamente el modelo durante la traducción.

## 7. Módulos Python propuestos

- `parameters.py`: parámetros físicos, geometría y condiciones iniciales.
- `physics.py`: gravedad, arrastre, efecto Magnus, dinámica angular, rebote y colisión con la red.
- `simulation.py`: vector temporal, integración numérica y coordinación de la simulación.
- `visualization.py`: trayectoria 3D, animación y gráficas temporales.
- `__init__.py`: exposición de las funciones principales del paquete.

No se propondrán archivos adicionales para la primera versión.

## 8. Correspondencia MATLAB–Python

| MATLAB | Python | Observación |
|---|---|---|
| Vectores/matrices | `numpy.ndarray` | Se recomienda representar magnitudes vectoriales como `(3, n_muestras)`. |
| `zeros(3,length(t))` | `numpy.zeros((3, len(t)))` | Crea arreglos inicializados en cero. |
| `cross(a,b)` | `numpy.cross(a, b, axis=0)` | El eje debe especificarse si se conservan columnas como vectores. |
| `for k = 2:length(t)` | `for k in range(1, len(t)):` | Ajusta el inicio por la indexación. |
| Índices desde 1 | Índices desde 0 | `x(:,1)` pasa a `x[:, 0]`. |
| `plot`, `subplot`, `plot3` | Matplotlib (`plot`, `subplots`, ejes 3D) | La apariencia puede requerir ajustes. |

## 9. Riesgos de la migración

Los riesgos principales son errores de indexación, orientación de matrices y *broadcasting* de NumPy; cambios involuntarios en el vector de tiempo; confusión de unidades; diferencias en los criterios de colisión; diferencias de visualización entre MATLAB y Matplotlib; y modificar accidentalmente el comportamiento original mientras se intenta mejorar el modelo.

## 10. Criterios mínimos de verificación

- Obtener 301 muestras entre 0 y 1.5 segundos.
- Verificar las dimensiones esperadas de todos los arreglos.
- Ejecutar una prueba sin fuerzas.
- Ejecutar una prueba solo con gravedad.
- Ejecutar una prueba de arrastre.
- Ejecutar una prueba de efecto Magnus.
- Ejecutar una prueba de rebote con la mesa.
- Ejecutar una prueba de colisión con la red.
- Confirmar ausencia de `NaN` e infinitos.
- Comparar numéricamente los resultados con MATLAB para las mismas entradas.

## 11. Decisiones iniciales

- `legacy/TableTennisTests.mlx` se conservará intacto.
- `pitch` se interpretará como 23.5 únicamente en la versión Python y quedará documentado.
- La primera traducción conservará las unidades y el comportamiento numérico del original.
- Las mejoras físicas se harán después de obtener una versión reproducible.
- El notebook importará las funciones desde `src` y no duplicará la física.

## 12. Resultado esperado

El resultado será un paquete Python reproducible que genere las mismas series temporales de referencia, con física, simulación y visualización separadas. Esta base permitirá construir después un notebook interactivo que ajuste parámetros con *sliders*, ejecute la simulación y muestre sus trayectorias y gráficas de manera trazable.
