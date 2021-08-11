#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from beugungo5 import wavelength.wavelength as wavelength
from beugungo5 import gitterkonstant.gitterkonstant as gitterkonstant




prompt_wavelength = input('Are you solving for the wavelength lambda as in Aufgabe 4? Enter to skip\n')

if prompt_wavelength:

    wave_lambda , wave_delta= wavelength()

prompt_g = input('Are you solving for a Gitterkonstante g? Enter to skip\n')

if prompt_g:

    prompt_use = input('Do you want to use your Lambda from the previous calculation? Enter to skip and use Data Sheet value.\n')
    if prompt_use:
        try:
            g = gitterkonstant(wave_lambda=wave_lambda) 
        except NameError as ne:
            print('Seems like you didn’t calculate a wavelength in the previous prompt.')
            print(ne)
    else:
        g = gitterkonstant()

