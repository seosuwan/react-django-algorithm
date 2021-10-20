import pandas as pd

from admin.common.models import ValueObject, Reader, Printer
from icecream import ic

class CrimeCctvModel():
    vo = ValueObject()
    reader = Reader()
    printer = Printer()

    def __init__(self):
        '''
        Raw Data 의  features 를 가져온다.
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.vo.context = 'admin/crime/data/'
        self.crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생'] # Nominal
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'] # Nominal
        self.crime_rate_column = ['살인 검거율', '강도 검거율', '강간 검거율', '절도 검거율', '폭력 검거율'] # Ratio

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        print(f'파일명: {crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model

    def create_police_position(self) -> object:
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        # for name in crime['관서명']:
        #     station_names.append('서울'+str(name[:-1] + '경찰서'))
        [station_names.append('서울'+str(name[:-1] + '경찰서'))for name in crime['관서명']]
        station_address = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_address.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_address:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        crime.to_csv(self.vo.context+'new_data/police_position.csv')

        '''
        경찰서
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 31 entries, 0 to 30
        Data columns (total 11 columns):
         #   Column  Non-Null Count  Dtype
        ---  ------  --------------  -----
         0   관서명     31 non-null     object
         1   살인 발생   31 non-null     int64
         2   살인 검거   31 non-null     int64
         3   강도 발생   31 non-null     int64
         4   강도 검거   31 non-null     int64
         5   강간 발생   31 non-null     int64
         6   강간 검거   31 non-null     int64
         7   절도 발생   31 non-null     int64
         8   절도 검거   31 non-null     int64
         9   폭력 발생   31 non-null     int64
         10  폭력 검거   31 non-null     int64
        dtypes: int64(10), object(1)
        memory usage: 2.8+ KB
        ic| this.info(): None

        '''
    def create_cctv_model(self) -> object:
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        print(f'파일명: {cctv_file_name}')
        cctv_model= reader.csv(cctv_file_name)
        cctv_model.rename(columns={'기관명': '구별'}, inplace=True)
        cctv_model.to_csv(self.vo.context + 'new_data/CCTV_in_Seoul.csv')
        printer.dframe(cctv_model)
        return cctv_model

    def create_population_model(self) -> object:
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = 'population_in_Seoul'
        popu_file_name = reader.new_file(vo)
        print(f'파일명: {popu_file_name}')
        population = reader.xls(popu_file_name, 2, ("b, d, g, j, n"))
        # list = ['구별','인구수','한국인','외국인','고령자']
        # population.columns = list
        population.rename(columns={'자치구': '구별', '계':'인구수', '계.1':'한국인', '계.2':'외국인', '65세이상고령자':'고령자'}, inplace=True)
        population.drop([26], inplace= True)
        population.to_csv(self.vo.context + 'new_data/population2.csv')
        printer.dframe(population)
        return population

    def merge_model(self):
        pop = self.create_population_model()
        cctv = self.create_cctv_model()
        cctv_pop_model = pd.merge(cctv,pop)
        ic(cctv_pop_model.corr())

        '''
           r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''
        # cctv_pop_model.to_csv(self.vo.context + 'new_data/merge_model.csv')
        '''
       ic| cctv_pop_model.corr():                  CCTV소계  2013년도 이전  2014년    2015년    2016년     인구수     한국인     외국인     고령자
                                       소계        1.000000   0.862756  0.450062  0.624402  0.593398  0.306342  0.304287 -0.023786  0.255196
                                       2013년도이전 0.862756   1.000000  0.121888  0.257748  0.355482  0.168177  0.163142  0.048973  0.105379
                                       2014년      0.450062   0.121888  1.000000  0.312842  0.415387  0.027040  0.025005  0.027325  0.010233
                                       2015년      0.624402   0.257748  0.312842  1.000000  0.513767  0.368912  0.363796  0.013301  0.372789
                                       2016년      0.593398   0.355482  0.415387  0.513767  1.000000  0.144959  0.145966 -0.042688  0.065784
                                       인구수      [0.306342]  0.168177  0.027040  0.368912  0.144959  1.000000  0.998061 -0.153371  0.932667
                                       한국인      [0.304287]  0.163142  0.025005  0.363796  0.145966  0.998061  1.000000 -0.214576  0.931636
                                       외국인      [-0.023786] 0.048973  0.027325  0.013301 -0.042688 -0.153371 -0.214576  1.000000 -0.155381
                                       고령자      [0.255196]  0.105379  0.010233  0.372789  0.065784  0.932667  0.931636 -0.155381  1.000000
                    '''

    def sum_crime(self):
        crime = pd.read_csv(self.vo.context + 'new_data/police_position.csv')
        crime['발생'] = crime.loc[:, self.crime_columns].sum(axis=1)
        crime['검거'] = crime.loc[:, self.arrest_columns].sum(axis=1)
        ic(crime.corr())
        grouped = crime.groupby('구별')
        crime_filter = grouped['발생', '검거'].sum()
        self.printer.dframe(crime_filter)
        crime_filter.to_csv(self.vo.context + 'new_data/new_crime_arrest.csv')