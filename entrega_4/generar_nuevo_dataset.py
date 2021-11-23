import numpy as np
from numpy import savetxt
from scipy.stats import lognorm
from scipy.stats import johnsonsu
from scipy.stats import cauchy

DATASET_SIZE = 1000

# variable artist_familiarity
af_lognorm_params = {'s': 0.0028675926750397467, 'loc': -51.90086685333819, 'scale': 52.49200076109122}
artist_familiarity_random_variables = lognorm.rvs(af_lognorm_params['s'], af_lognorm_params['loc'], af_lognorm_params['scale'], size=DATASET_SIZE)

# variable tempo
tempo_lognorm_params = {'s' : 0.12149743292683457, 'loc' : -161.797363168444, 'scale' : 283.1280555801535}
tempo_random_variables = lognorm.rvs(tempo_lognorm_params['s'], tempo_lognorm_params['loc'], tempo_lognorm_params['scale'], size = DATASET_SIZE)

# variable artist_hottness
ah_johnsonsu_params = {'a' : -0.2534054635372592, 'b' : 1.0551224337979752, 'loc' : 0.3790529638553469, 'scale' : 0.08396549809827072}
ah_random_variables = johnsonsu.rvs(ah_johnsonsu_params['a'], ah_johnsonsu_params['b'], ah_johnsonsu_params['loc'], ah_johnsonsu_params['scale'], size=DATASET_SIZE)

# variable duration
duration_cauchy_params = {'loc' : 223.78064819624245, 'scale' : 44.655732450396606}
duration_random_variables = cauchy.rvs(duration_cauchy_params['loc'], duration_cauchy_params['scale'], size=DATASET_SIZE)

random_variables = [ah_random_variables, duration_random_variables, artist_familiarity_random_variables, tempo_random_variables]
random_variables = np.transpose(random_variables)

savetxt('random_variables.csv', random_variables, delimiter=',', header='Artis Hottness,Duration,Artist Familiarity,Tempo', comments='')