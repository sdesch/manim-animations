class DBifurcacion(Scene):
    def construct(self):
        # Definir los valores iniciales y la cantidad de iteraciones
        x_inicial = -1.2  # Valor inicial del eje x
        x_final = 3.2     # Valor final del eje x
        iteraciones = 100 # Cantidad de iteraciones

        # Listas para almacenar los valores de x e y
        x_valores = []
        y_valores = []

        # Crear ejes con un rango específico
        ejes = Axes(
            x_range=[x_inicial, x_final, 0.5],  # Rango del eje x: de x_inicial a x_final con incrementos de 0.5
            y_range=[-2, 2, 0.5],              # Rango del eje y: de -2 a 2 con incrementos de 0.5
        )

        # Generar valores de bifurcación
        for l in np.linspace(x_inicial, x_final, iteraciones):
            x = np.random.random()
            for n in range(100):
                x = l * x - x**3
            x_valores.append(l)
            y_valores.append(x)

        # Convertir los valores de (x, y) en puntos en las coordenadas de la escena
        puntos = [ejes.c2p(x, y) for x, y in zip(x_valores, y_valores)]

        # Crear un grupo de puntos (puntos en el diagrama de bifurcación)
        diagrama_de_bifurcacion = VGroup(*[Dot(punto, radius=0.05) for punto in puntos])

        # Agregar los ejes a la escena
        self.add(ejes)

        # Animar la creación del diagrama de bifurcación durante 5 segundos
        self.play(Create(diagrama_de_bifurcacion), run_time=5)
