def handle_cardiac_arrest(all_actors):
    for actor in all_actors:
        if actor.kind == 'nurse':
            ...do something...
        elif actor.kind == 'doctor':
            ...do something else...
        else:
            ...do some default action...
