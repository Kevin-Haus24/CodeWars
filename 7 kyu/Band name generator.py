def band_name_generator(name):
    if name[0] != name[-1]:
        return 'The ' + name.capitalize()
    else:
        return name.capitalize() + name[1:]

print(band_name_generator('knifek'))