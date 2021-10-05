import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from django.db import models
from icecream import ic
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

from admin.common.models import DFrameGenerator


class HousingService(object):

    def __init__(self):
        self.dfg = DFrameGenerator()
        self.dfg.fname = 'admin/housing/data/housing.csv'
        self.df = self.dfg.create_model()

    def housing_info(self):
        self.dfg.model_info(self.df)


    '''오늘은 여기까지..'''




    def housing_hist(self):
        self.model.dframe.hist(bins=50, figsize=(20, 15))
        plt.savefig('admin/housing/image/housing-hist/png')

    def split_model(self) -> []:
        train_set, test_set = train_test_split(self.new_model(), test_size=0.2, random_state=42)
        return [train_set, train_set]

    def income_cat_hist(self):
        h = self.new_model()
        h['income_cat'] = pd.cut(h['median_incime'],
                                 bins=[0., 1.5, 3.0, 4.5 ,6, np.inf], #np.inf is NaN(Not a Numer)
                                 labels=[1, 2, 3, 4, 5]
                                 )
        h['income_cat'].hist()
        plt.savefig('admin/housing/image/income-cat.png')

    def split_medel_by_income_cat(self) -> []:
        h = self.new_model()
        split = StratifiedShuffleSplit(n_splits=1, test=0.2, random_state=42)
        for train_idx, test_idx in split.split(h, h['income_cat']):
            train_set = h.loc[train_idx]
            test_set = h.loc[test_idx]
        ic(test_set['income_cat'].value_counts() / len(test_set))






class Housing(models.Model):
    housing_id = models.AutoField(primary_key = True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    housing_median_age = models.FloatField()
    total_rooms = models.FloatField()
    total_bedrooms = models.FloatField()
    population = models.FloatField()
    households = models.FloatField()
    median_income = models.FloatField()
    median_house_value = models.FloatField()
    ocean_proximity = models.TextField()

    class Meta:
        db_table = "housing"

    def __str__(self):
        return f'[{self.pk}] {self.housing_id}'


# Create your models here.
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   longitude           20640 non-null  float64
 1   latitude            20640 non-null  float64
 2   housing_median_age  20640 non-null  float64
 3   total_rooms         20640 non-null  float64
 4   total_bedrooms      20433 non-null  float64
 5   population          20640 non-null  float64
 6   households          20640 non-null  float64
 7   median_income       20640 non-null  float64
 8   median_house_value  20640 non-null  float64
 9   ocean_proximity     20640 non-null  object
dtypes: float64(9), object(1)
memory usage: 1.6+ MB

'''