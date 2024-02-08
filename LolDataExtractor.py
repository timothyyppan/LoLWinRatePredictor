import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
import ApiKeyGetter as akg
import PuuidExtractor as pe
import MatchIDExtractor as mide
import MatchInfoExtractor as mie

summoner_name = input("Enter your summoner name: ")
api_key = akg.get_api_key()
puuid = pe.get_puuid(summoner_name, api_key)
match_id = mide.get_match_id(puuid, api_key)

data = []
target = []
print(match_id[1])
result = mie.get_match_info(match_id[1], summoner_name, api_key)
data.append(result[0])
target.append(result[1])

print(data)
print(target)

#for i in range(0, 10):
#    result = mie.get_match_info(match_id[i], summoner_name, api_key)
#    data.append(result[0])
#    target.append(result[1])
#    result = []



#x = np.array(data)
#y = np.array(target)

#imputer = SimpleImputer(strategy='mean')
#x = imputer.fit_transform(x)

#scaler = StandardScaler()
#x_scaled = scaler.fit_transform(x)

#model = LogisticRegression()

#model.fit(x_scaled, y)

#probabilities = model.predict_proba(x_scaled)
#win_probabilities = probabilities[:, 1]
#print(win_probabilities)
#features = [[0.0, 8.0, 2.0, 1, 0, 2375.0, 0.0, 7.716049383, 30, 0.0]]
#features = [[0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0, 0.0]]
#features_array = np.array(features)

#features_scaled = scaler.transform(features_array)

#win_probability = model.predict_proba(features_scaled)[0, 1]

#print(win_probability * 100, "%")