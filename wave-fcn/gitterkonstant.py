def gitterkonstant(wave_lambda=532, m=1):
    """
    This should help you solve Aufgabe 5, or any question that involved
    needing to calculate the g-value.
    This can stand for the dimensions of a hole,
    or the uniform distance between holes in a matrix.

    wave_lambda: Wellenlänge Lambda default:532 for ND:Yg Laser
    d_1: Abstand zwischen Maxima in Abbildung auf Schirm
    d_proj: Abstand zwischen Gitter und Schirm


    """
    #inputs

    try:
        d_proj = input('Input Schirmabstand in centimeter:\n')
        d_1 = input('Input d_1 in cm:\n')
    except NameError as ne:
        print('So..something went wrong')
        print(ne)

    #treat iputs

    try:
        d_1 = float(d_1)
        d_proj = float(d_proj)
    except TypeError as te:
        print('Enter something caclculable')
        print(te)

    wave_lambda = wave_lambda*(10**(-9))  #wavelength in m
    d_1 = d_1*(10**(-2))  #cm to m
    d_proj = d_proj*(10**(-2))  #cm to m

    theta = math.atan(d_1/d_proj)  #bending angle

    #gitter value
    g = wave_lambda / math.sin(theta)

    g = g*(10**(6))  #in um angeben

    #Gaussian Fehlerfortpflanzung
    if wave_delta:
        delta_wave = wave_delta
    else:
        delta_wave = float(input('Input Unischerheit für lambda-Wert in nanometer:\n'))
    
    try:
        delta_d_1 = float(input('Input Unischerheit für d1-Wert in centimeter:\n'))
        delta_d_proj = float(input('Input Unischerheit für d_proj-Wert in centimeter:\n'))
    except ValueError as ve: 
        print('Yo motherfucker do a better job at using my script')
        print(ve)

    #idea for later. make it able to sense unit input and be flexible for multi inputs

    #deltas in m

    delta_wave = delta_wave*(10**(-9))
    delta_d_1 = delta_d_1*(10**(-2))
    delta_d_proj = delta_d_proj*(10**(-2))

    #Ableitungen für Kleinwinkelnäherung

    dd_lambda = 1 / math.sin(theta)
    ddd_1 = (-wave_lambda*math.cos(theta)) / ((1+(d_1/d_proj)**2)*d_proj*((math.sin(theta))**2))
    ddd_proj = (wave_lambda*d_1*math.cos(theta)) / ((d_proj**2)*(1+((d_1/d_proj)**2))*((math.sin(theta))**2))

    term_lambda = (dd_lambda*delta_wave)**2
    term_d_1 = (ddd_1*delta_d_1)**2
    term_d_proj = (ddd_proj*delta_d_proj)**2

    delta_g = math.sqrt(term_lambda + term_d_1 + term_d_proj)

    delta_g = delta_g*(10**(6))  #in micrometer angeben

    print(f'Die Gitterkonstante g beträgt {g}±{delta_g}um')

    return g