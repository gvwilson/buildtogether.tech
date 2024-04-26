import logging

def extrapolate(basis, case):
    logging.debug("entering extrapolate...")
    trials = count_basis_width(basis)
    if not trials:
        logging.warning("...no trials!")
        raise InvalidDataException("no trials")
    logging.debug(f"...running {len(trials)} trials")
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    logging.debug(f"...exiting extrapolate with {result}")
