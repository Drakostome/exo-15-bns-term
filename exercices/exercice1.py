def rechercheMinMax(tab):
    if tab == [] :
        return {'min' : None, 'max ': None}
    else :
        for i in tab :
            max = tab[0]
            if i >= max :
                max = i
        for j in tab:
            min = tab[0]
            if j<= min :
                min = j
    return {'min' : min,' max ': max}
