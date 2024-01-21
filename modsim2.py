from modsim import *
def bike_to_makati(state):
#     print("Moving to Makati")
    if state.manila == 0:
        state.manila_empty += 1
        return
    bikeshare.makati += 1
    bikeshare.manila -= 1


def bike_to_manila(state):
#     print("Moving to Manila")
    if state.makati == 0:
        state.makati_empty += 1
        return
    bikeshare.makati -= 1
    bikeshare.manila += 1


def step(state, p1, p2):
    if flip(p1):
        bike_to_makati(state)
    if flip(p2):
        bike_to_manila(state)


def run_simulation(state, p1, p2, num_steps):
    makati_results = TimeSeries()
    manila_results = TimeSeries()
    for i in range(num_steps):
        step(state, p1, p2)
        makati_results[i] = bikeshare.makati
        manila_results[i] = bikeshare.manila
    plt.plot(makati_results, label = "Makati")
    plt.plot(manila_results, label = "Manila")
    plt.legend()
    