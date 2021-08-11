def wavelength(d_proj=1, m=1):

    import math
    
    """
    Relevant to solve Exercise 4 in Beugung O5 Experiment
    Give all units in meters, m

    __Small Angle Assumption__
    
    g: Gitterkonstante in micrometer, um
    d_1: Distance from the 0th to 1st Maxima in centimeter, cm
    d_proj: Distance from Matrix to Projection in meter, m (default: d_proj=1m)

    __Generale__
    
    theta: curvature angle
    m: ordnungszahl (default: m=1)

    Uncertainty calculations done with Gaussian Error Balance
    
    __Outputs__
    
    (1) wavelength in small angle assumption and (2) uncertainty
    
    __Example__

    wavelength() 

    wavelength(d_proj=2, m=3)

    """

    try:
        g = input('Input Gitterkonstante in micrometer:\n')
        d_1 = input('Input d_1 in cm:\n')
    except NameError as ne:
        print('So..something went wrong')
        print(ne)

    try:
        d_1 = float(d_1)*(10**(-2))  #convert d_1 from cm to m
        g = float(g)*(10**(-6))  #convert g from micrometer to m
    except TypeError as tp: #value error if '' entered
        print('Please enter a proper value')
        print(tp)

    theta = math.atan(d_1/d_proj)  #curvature angle

    wavelength_kn = (g*d_1) / (d_proj)
    wavelength_kn = wavelength_kn * (10**(9))  #show wavelength in nm

    wavelength = (g*math.sin(theta))/m
    wavelength = wavelength*(10**(9))  # in nm angeben

    #Gauss Uncertainty for Kleinwinkelnäherung

    #delta_lambda = input('Unsicherheit für Wellenlänge in cm:\n')

    delta_g = float(input('Input Unischerheit für g-Wert in micrometer:\n'))
    delta_d_1 = float(input('Input Unischerheit für d1-Wert in centimeter:\n'))
    delta_d_proj = float(input('Input Unischerheit für d_proj-Wert in centimeter:\n'))

    #idea for later. make it able to sense unit input and be flexible for multi inputs

    #deltas in m

    delta_g = delta_g*(10**(-6))
    delta_d_1 = delta_d_1*(10**(-2))
    delta_d_proj = delta_d_proj*(10**(-2))

    #Ableitungen für Kleinwinkelnäherung

    ddg = d_1/d_proj
    ddd_1 = g/d_proj
    ddd_proj = (-g*d_1) / (d_proj**2)

    term_g = (ddg*delta_g)**2
    term_d_1 = (ddd_1*delta_d_1)**2
    term_d_proj = (ddd_proj*delta_d_proj)**2

    delta_lambda = math.sqrt(term_g + term_d_1 + term_d_proj)

    delta_lambda = delta_lambda*(10**(9))  #in nm eingeben


    print(f'Die Wellenlänge Lambda unter Kleinwinkelnäherung beträgt {wavelength_kn} ± { delta_lambda} nm')
    print(f'Die Wellenlänge Lambda unter normalen Bedingungen beträgt {wavelength} ± N/A nm')

    return wavelength_kn, delta_lambda
