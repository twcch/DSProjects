import pandas as pd
import sqlite3


class CreateGapminderDB:
    def __init__(self):
        self.file_names = [
            'ddf--datapoints--gdp_pcap--by--country--time',
            'ddf--datapoints--lex--by--country--time',
            'ddf--datapoints--pop--by--country--time',
            'ddf--entities--geo--country'
        ]

        self.table_names = [
            'gdp_per_capita',
            'life_expectancy',
            'population',
            'geography'
        ]

        self.conn = sqlite3.connect('raw_data/gapminder.db')

    def import_as_dataframe(self):
        df_dict = {}
        for file_name, table_name in zip(self.file_names, self.table_names):
            file_path = f'raw_data/{file_name}.csv'
            df = pd.read_csv(file_path)
            df_dict[table_name] = df
        return df_dict

    def create_database(self):
        conn = sqlite3.connect('raw_data/gapminder.db')
        df_dict = self.import_as_dataframe()
        for table_name, values in df_dict.items():
            values.to_sql(name=table_name, con=conn, if_exists='replace', index=False)

        drop_view_sql = '''
                        DROP VIEW IF EXISTS plotting;
                        '''

        create_view_sql = '''
                          CREATE VIEW plotting AS
                          SELECT geography.name          AS country_name,
                                 geography.world_4region AS continent,
                                 gdp_per_capita.time     AS dt_year,
                                 gdp_per_capita.gdp_pcap AS gdp_per_capita,
                                 life_expectancy.lex     AS life_expectancy,
                                 population.pop          AS population
                          FROM gdp_per_capita
                                   INNER JOIN geography
                                              ON gdp_per_capita.country = geography.country
                                   INNER JOIN life_expectancy
                                              ON gdp_per_capita.country = life_expectancy.country
                                                  AND gdp_per_capita.time = life_expectancy.time
                                   INNER JOIN population
                                              ON gdp_per_capita.country = population.country
                                                  AND gdp_per_capita.time = population.time
                          WHERE gdp_per_capita.time < 2024;
                          '''

        cur = conn.cursor()
        cur.execute(drop_view_sql)
        cur.execute(create_view_sql)
        conn.commit()

        conn.close()

create_gapminder_db = CreateGapminderDB()
create_gapminder_db.create_database()

