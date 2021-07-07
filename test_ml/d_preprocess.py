import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#rainfall data
pk_rainfall = pd.DataFrame(pd.read_csv('pr_1991_2020_PAK.csv'), columns=['rainfall', 'year', 'month'])
pk_rainfall.to_csv('pk_rainfall.csv', index = False)

#temperature data
pk_temp = pd.DataFrame(pd.read_csv('tas_1991_2020_PAK.csv'), columns=['temperature', 'year', 'month'])
pk_temp.to_csv('pk_temp.csv', index = False)

#crop yield data
pk_crop_yield = pd.DataFrame(pd.read_csv('FAOSTAT_data_6-2-2021_Y.csv'), columns=['crop', 'year', 'value'])
cy_test = np.array(pk_crop_yield['crop'])
cy_unique = np.unique(cy_test)
cy_codes =[]
for i in range (len(cy_unique)):
    cy_codes.append(i)
cy_dict = dict(zip(cy_unique, cy_codes))
encoded_cy = []

for i in range (len(pk_crop_yield['crop'])):  
        encoded_cy.append(cy_dict.get(pk_crop_yield['crop'].iloc[i]))
pk_crop_yield['crop_val'] = encoded_cy
pk_crop_yield.to_csv('pk_crop_yield.csv', index = False)

#crop value data
pk_crop_value = pd.DataFrame(pd.read_csv('FAOSTAT_data_6-2-2021_PV.csv'), columns=['crop', 'year', 'value'])

cv_test = np.array(pk_crop_value['crop'])
cv_unique = np.unique(cv_test)
cv_codes =[]
for i in range (len(cv_unique)):
    cv_codes.append(i)
cv_dict = dict(zip(cv_unique, cv_codes))
encoded_cv = []

for i in range (len(pk_crop_value['crop'])):  
        encoded_cv.append(cv_dict.get(pk_crop_value['crop'].iloc[i]))
pk_crop_value['crop_val'] = encoded_cv
pk_crop_value.to_csv('pk_crop_value.csv', index = False)

#rainfall split
pk_rainfall_train, pk_rainfall_test = train_test_split(pk_rainfall, test_size = 0.3)
pk_rainfall_train.to_csv('pk_rainfall_train.csv', index = False)
pk_rainfall_test.to_csv('pk_rainfall_test.csv', index = False)

#temp split
pk_temp_train, pk_temp_test = train_test_split(pk_temp, test_size = 0.3)
pk_temp_train.to_csv('pk_temp_train.csv', index = False)
pk_temp_test.to_csv('pk_temp_test.csv', index = False)

#crop yield split
pk_crop_yield_train, pk_crop_yield_test = train_test_split(pk_crop_yield, test_size = 0.3)
pk_crop_yield_train.to_csv('pk_crop_yield_train.csv', index = False)
pk_crop_yield_test.to_csv('pk_crop_yield_test.csv', index = False)

#crop value split
pk_crop_value_train, pk_crop_value_test = train_test_split(pk_crop_value, test_size = 0.3)
pk_crop_value_train.to_csv('pk_crop_value_train.csv', index = False)
pk_crop_value_test.to_csv('pk_crop_value_test.csv', index = False)

