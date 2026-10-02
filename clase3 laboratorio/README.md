# Laboratorio 01 --- Análisis del funcionamiento de una aplicación web

> **Curso:** Aplicaciones y Servicios Web\
> **Modalidad:** Práctica de laboratorio\
> **Entrega:** Repositorio GitHub --- archivo `README.md`\
> **Evidencias:** Carpeta `evidencias/`

------------------------------------------------------------------------

## Objetivo de la práctica

Analizar el funcionamiento de una aplicación web real mediante las
herramientas de desarrollo del navegador, identificando los recursos
cargados, las solicitudes y respuestas HTTP, la estructura DOM y las
interacciones entre cliente y servidor.

## Resultado esperado

Al finalizar la práctica, el estudiante deberá poder reconstruir y
documentar el flujo observado entre:

``` mermaid
flowchart LR
    U[Usuario] --> N[Navegador]
    N --> H[HTTP]
    H --> S[Servidor]
    S --> R[Respuesta]
    R --> N
    N --> D[DOM]
    D --> I[Interfaz]
    I --> U
```

> El diagrama anterior representa los **componentes que serán
> analizados**. El diagrama final de la práctica deberá ser construido
> por el estudiante a partir de sus propias observaciones.

------------------------------------------------------------------------

# 1. Preparación del entorno

1.  Ingrese a la aplicación web indicada por el docente.
2.  Abra las **herramientas de desarrollo** del navegador.
3.  Identifique las herramientas **Red / Network** y **Elementos /
    Elements**.
4.  Cree la siguiente estructura dentro del repositorio:

``` text
laboratorio-01/
├── README.md
└── evidencias/
```

El archivo `README.md` será el informe de la práctica. La carpeta
`evidencias/` contendrá las capturas utilizadas para sustentar los
resultados.

------------------------------------------------------------------------

# 2. Identificación de recursos de la aplicación

Abra la herramienta **Red / Network** y recargue completamente la
aplicación.

Observe las solicitudes generadas durante la carga e identifique como
mínimo **cinco recursos**, procurando seleccionar tipos diferentes:
documento HTML, CSS, JavaScript, imágenes, fuentes u otros.

## Resultados

Complete la tabla:

  Recurso   Tipo   Dominio     Tamaño
  --------- ------ --------- --------
 gob_linea_logo.jpg  --jpg --    --itm.edu.co--  --18255--
 rs6.css?ver        --css--   --itm.edu.co--       58327      
imagesloaded.min.js?ver  --js--  --itm.edu.co--   --5520 --
01-Programas.gif      --gif--     --itm.edu.co--   --181535--                   
 24px.svg             --svg--      --fonts.gstatic.com--  --3340--
                             
                             

**Total de solicitudes observadas:** `_121____`

## Evidencia

Guarde una captura de la pestaña Network como:

``` text
evidencias/network.png
```

Inclúyala aquí:

``` markdown
![Recursos cargados por la aplicación](evidencias/network.png)
```

### Análisis

**¿Por qué una sola URL puede generar múltiples solicitudes HTTP?**

> Escriba aquí su respuesta.
porque una url tiene una web que trae multiples recursos diferentes
------------------------------------------------------------------------

# 3. Análisis de una solicitud HTTP

En **Network**, seleccione una de las solicitudes realizadas por el
navegador, preferiblemente la correspondiente al documento principal.

Identifique la información solicitada a continuación.

  Elemento              Resultado
  --------------------- -----------
  URL https://www.itm.edu.co//wp-content/uploads/2021/09/01-Programas.gif
  
  Método HTTP GET       
  Código de estado  200 ok     
  Host / dominio   itm.edu.co      
  Tipo de recurso  gif      
  Tiempo de respuesta   0 ms

## Flujo que se está observando

``` mermaid
sequenceDiagram
    participant N as Navegador
    participant S as Servidor
    N->>S: Solicitud HTTP
    S-->>N: Respuesta HTTP
```

## Evidencia

Guarde una captura de los detalles de la solicitud como:

``` text
evidencias/request.png
```

Inclúyala en el informe:

``` markdown
![Análisis de la solicitud HTTP](evidencias/request.png)
```

### Análisis

**¿Qué recurso solicitó el navegador?**

> Escriba aquí su respuesta.
   gif
**¿Qué información permite determinar si la solicitud fue atendida
correctamente?**

> Escriba aquí su respuesta.
 el status code 200 ok
------------------------------------------------------------------------

# 4. Inspección del DOM

Seleccione un elemento visible de la aplicación, por ejemplo:

-   un botón;
-   un título;
-   un enlace;
-   un campo de formulario;
-   un elemento del menú.

Utilizando **Elementos / Elements**:

1.  Localice el elemento dentro del DOM.
2.  Identifique la etiqueta HTML utilizada.
3.  Modifique temporalmente su contenido desde las herramientas de
    desarrollo.
4.  Observe el cambio producido en la interfaz.
5.  Registre la evidencia.

## Resultados

**Elemento seleccionado:** `boton____________________________`

**Etiqueta HTML:** `_______________a_____________`

**Contenido original:** `__________descargar__________________`

**Modificación realizada:** `____________nombre boton Santy________________`

El proceso observado puede representarse conceptualmente así:

``` mermaid
flowchart LR
    H[HTML] --> B[Navegador]
    B --> D[DOM]
    J[JavaScript / DevTools] -->|consulta o modifica| D
    D --> I[Interfaz]
```

## Evidencia

Guarde la captura como:

``` text
evidencias/dom.png
```

Inclúyala aquí:

``` markdown
![Inspección y modificación del DOM](evidencias/dom.png)
```

### Análisis

**¿La modificación realizada sobre el DOM alteró permanentemente la
aplicación o los archivos almacenados en el servidor? Justifique.**

> Escriba aquí su respuesta.
No. La modificación no alteró permanentemente la aplicación ni modificó en absoluto los archivos almacenados en el servidor.Es un cambio  local y temporal 
------------------------------------------------------------------------

# 5. Análisis de una interacción dinámica

Regrese a **Network** y limpie las solicitudes registradas.

Realice una acción dentro de la aplicación que pueda generar una
interacción con el servidor, por ejemplo:

-   consultar;
-   buscar;
-   filtrar;
-   seleccionar una opción;
-   enviar información.

Observe si aparece una nueva solicitud en Network.

## Resultados

  Elemento                       Resultado
  ------------------------------ -----------
  Acción realizada :    Clic en el botón flotante de WhatsApp para desplegar el cuadro de chat.
  ¿Generó una nueva solicitud?   :
  URL solicitada  data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 24 24'%3E%3Cpath d='M24 2.4 21.6 0 12 9.6 2.4 0 0 2.4 9.6 12 0 21.6 2.4 24l9.6-9.6 9.6 9.6 2.4-2.4-9.6-9.6z'/%3E%3C/svg%3E 

  Método HTTP  Get    
  Código de estado 200 ok               
  Tipo de respuesta image/svg+xml

## Ciclo de interacción

Utilice este esquema únicamente como referencia conceptual para
interpretar lo observado:

``` mermaid
flowchart LR
    U[Usuario] -->|interacción| J[JavaScript]
    J -->|Solicitud HTTP| S[Servidor]
    S -->|Respuesta HTTP| J
    J -->|actualiza| D[DOM]
    D --> I[Interfaz actualizada]
    I --> U
```

## Evidencia

Guarde la captura como:

``` text
evidencias/interaccion.png
```

Inclúyala aquí:

``` markdown
![Interacción observada en Network](evidencias/interaccion.png)
```

### Análisis

**Explique la relación entre la acción realizada por el usuario y la
solicitud observada.**

> Escriba aquí su respuesta.
Al hacer clic en el botón flotante de WhatsApp, el script de la página (joinchat.min.js) capturó el evento de interacción del usuario y ejecutó el código para desplegar la ventana flotante de chat.
------------------------------------------------------------------------

# 6. Reconstrucción del flujo observado

A partir de **sus propias evidencias**, construya un diagrama Mermaid
que represente el funcionamiento de la aplicación analizada.

El diagrama deberá incluir, cuando corresponda:

`Usuario` · `Navegador` · `JavaScript` · `Solicitud HTTP` · `Servidor` ·
`Respuesta HTTP` · `DOM` · `Interfaz`

> **No copie los diagramas anteriores.** Esta sección debe representar
> el flujo que usted pudo comprobar durante la práctica.

Reemplace el siguiente bloque con su diagrama:


```mermaid
flowchart LR
    U[Usuario] -->|1. Clic en botón de WhatsApp| I[Interfaz]
    I -->|2. Dispara evento| JS[JavaScript]
    JS -->|3. Solicita icono SVG| N[Navegador]
    N -->|4. Petición GET| REQ[Solicitud HTTP]
    REQ -->|5. Consulta recurso| S[Servidor / Cache]
    S -->|6. Estado 200 OK| RES[Respuesta HTTP]
    RES -->|7. Entrega datos| N
    N -->|8. Actualiza árbol| D[DOM]
    D -->|9. Muestra ventana de chat| I
```


# 7. Observado vs. inferido

Una herramienta de desarrollo permite observar una parte del sistema,
pero no necesariamente todo lo que ocurre en el servidor.

Clasifique sus hallazgos:

## Elementos observados directamente

- Peticiones HTTP registradas en la pestaña Network con sus métodos (GET), códigos de estado (200 OK), rutas de URL y tipos MIME de los recursos (image/jpeg, text/css, image/svg+xml).

- Recursos servidos directamente desde la memoria caché del navegador (from memory cache) y tiempos de respuesta de cada transferencia.

- Estructura jerárquica del árbol DOM en la pestaña Elements y la actualización visual inmediata de la interfaz al modificar etiquetas o texto localmente.   


## Elementos inferidos

-   Procesamiento de scripts del lado del servidor (lenguaje PHP en WordPress) para interpretar solicitudes y armar las respuestas HTML.

- Consultas a bases de datos relacionales en el servidor para recuperar el contenido dinámico del portal.

- Reglas internas de optimización, seguridad y encabezados de caché configurados en el servidor web (Nginx o Apache).
   


> No presente como observado un proceso interno que las herramientas del
> navegador no permitan comprobar directamente.

------------------------------------------------------------------------

# 8. Conclusiones

Redacte **tres conclusiones técnicas** derivadas de la práctica.

1.  El DOM es una copia temporal en el cliente: Editar elementos en DevTools solo modifica la memoria RAM local del navegador. Al recargar la página (F5), todo vuelve a su estado original porque los archivos del servidor nunca cambian.

2. Carga modular mediante peticiones HTTP: Una URL no trae la web completa en un solo archivo. El HTML actúa como plantilla guía para que el navegador pida de forma independiente cada CSS, JS o imagen necesaria.

3. Interacciones dinámicas y optimización con caché: JavaScript captura los clics del usuario para solicitar solo los recursos específicos sin recargar toda la página, usando la memoria caché (200 OK from memory cache) para responder al instante.

Las conclusiones deben explicar lo aprendido a partir de la evidencia y
no limitarse a describir las actividades realizadas.

------------------------------------------------------------------------

# 9. Entrega

La estructura final esperada es:

``` text
laboratorio-01/
├── README.md
└── evidencias/
    ├── network.png
    ├── request.png
    ├── dom.png
    └── interaccion.png
```

Antes de entregar, verifique:

-   [ ] El `README.md` se visualiza correctamente en GitHub.
-   [ ] Las imágenes se muestran dentro del README.
-   [ ] Se documentaron al menos cinco recursos.
-   [ ] Se analizó una solicitud HTTP.
-   [ ] Se identificó y modificó un elemento del DOM.
-   [ ] Se analizó una interacción de la aplicación.
-   [ ] El diagrama final corresponde a lo observado.
-   [ ] Se diferenciaron elementos observados e inferidos.
-   [ ] Se redactaron tres conclusiones técnicas.
-   [ ] Se realizó `commit` y `push` al repositorio.

------------------------------------------------------------------------

## Criterio de documentación

> **Las capturas son evidencia, no la respuesta.**

Cada evidencia debe estar acompañada por una explicación que indique
**qué se observó, qué significa y cómo se relaciona con el
funcionamiento de la aplicación web**.
