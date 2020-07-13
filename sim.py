
params = dict(
   n=1000,
   steps=125,
   initially_infected=4,
   mu_add_at_step=0.0,
   mu_remove_at_step=0.0,
   vel_std=0.1,
   mortality_thresh=0.8,
   isolate_thresh=0.4,
   severity_score_mean=0.1,
   severity_score_std=0.4,
   infection_length_mean=31,
   infection_length_std=3.0,
   infection_prob_mean=0.8,
   infection_prob_std=0.2,
   partial_isolate_frac=0.4,
)

import run_sim
run_sim.run_sim_for_animation(**params)