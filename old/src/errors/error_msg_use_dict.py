if fname[-4:] != '.csv':
    raise OSError(ERRORS['not_csv_suffix'].format(fname=fname))
