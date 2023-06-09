import in_dat
import mensajes

if len(in_dat.jugadorN1 + in_dat.jugadorN2) >= 6:
    print("""
    ------------------------------
    ¡Bienvenido al juego de piedra
    papel y tijera!
    ---------+---------+----------
    """)
    eleccion_jugador1 = input(f'{in_dat.jugadorN1} elige uno piedra, papel o tijera! ')
    eleccion_jugador2 = input(f'{in_dat.jugadorN2} elige uno piedra, papel o tijera! ')

    match eleccion_jugador1:
        case 'piedra' if eleccion_jugador2 == 'papel': print(f'Gana {in_dat.jugadorN2} porque, el papel tapa a la piedra')
        case 'piedra' if eleccion_jugador2 == 'piedra': print(f'{in_dat.jugadorN1} y {in_dat.jugadorN2} quedan empatados')
        case 'piedra' if eleccion_jugador2 == 'tijera': print(f'Gana {in_dat.jugadorN1} porque, la piedra golpea a latijera')
        case 'papel' if eleccion_jugador2 == 'papel': print(f'{in_dat.jugadorN1} y {in_dat.jugadorN2} quedan empatados')
        case 'papel' if eleccion_jugador2 == 'piedra': print(f'Gana {in_dat.jugadorN1} porque, el papel tapa a la piedra')
        case 'papel' if eleccion_jugador2 == 'tijera': print(f'Gana {in_dat.jugadorN2} porque, la tijera corta al papel')
        case 'tijera' if eleccion_jugador2 == 'papel': print(f'Gana {in_dat.jugadorN1} porque, la tijera corta al papel')
        case 'tijera' if eleccion_jugador2 == 'piedra': print(f'Gana {in_dat.jugadorN2} porque, la piedra golpea a la tijera')
        case 'tijera' if eleccion_jugador2 == 'tijera': print(f'{in_dat.jugadorN1} y {in_dat.jugadorN2} quedan empatados')
        case _: print('error, has escrito algo mal :)')

else:
    print('error')