def extrapolate(basis, case):
    print "entering extrapolate..."
    trials = count_basis_width(basis)
    if not trials:
        print "...no trials!"
        raise InvalidDataException("no trials")
    print "...running", len(trials), "trials"
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    print "...exiting extrapolate with", result
