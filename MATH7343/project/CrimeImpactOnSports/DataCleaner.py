import datetime
import os

import pandas as pd


def get_baseball_date(day, year):
    day_components = day.split(" ")
    day_components[0] = day_components[0][:3]
    day_components = day_components[:3]
    return datetime.datetime.strptime(' '.join(day_components) + ' ' + year, '%a %b %d %Y').strftime('%d/%m/%Y')


def get_basketball_date(day):
    return datetime.datetime.strptime(day, '%a %b %d %Y').strftime('%d/%m/%Y')


def get_hockey_date(day):
    return datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%d/%m/%Y')


def get_soccer_date(day, year):
    day_components = day.split(" ")
    day_components[0] = day_components[0][:3]
    return datetime.datetime.strptime(' '.join(day_components) + ' ' + year, '%b %d %Y').strftime('%d/%m/%Y')


def get_crime_date_new(date):
    date = date.split(" ")[0]
    return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')


def get_crime_date_old(date):
    date = date.split(" ")[0]
    return datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%d/%m/%Y')


class Constants:
    BASEBALL_DIR_NAME = "baseball"
    BASKETBALL_DIR_NAME = "basketball"
    CRIME_DIR_NAME = "crime"
    HOCKEY_DIR_NAME = "hockey"
    SOCCER_DIR_NAME = "soccer"
    FOLDER_SEPARATOR = "/"
    SPORTS_DIR_NAME = "sports"
    LATEST_YEARS = ["2015", "2016", "2017", "2018"]


class DataCleaner():

    def __init__(self, data_folder_path):
        self.data_folder_path = data_folder_path
        c1 = pd.Series(data=None, dtype='datetime64[ns]', name='Date')
        c2 = pd.Series(data=None, dtype='str', name='Won')
        c3 = pd.Series(data=None, dtype='int64', name='Crimes')

        self.df = pd.concat([c1, c2, c3], axis=1)
        self.sports_df = pd.concat([c1, c2], axis=1)
        self.crime_df = pd.concat([c1, c3], axis=1)

    def clean_sports_data(self):
        for root, dirs, files in os.walk(self.data_folder_path):
            for directory in dirs:
                if directory == Constants.SPORTS_DIR_NAME:
                    for sub_root, sub_dirs, sub_files in os.walk(
                            self.data_folder_path + Constants.FOLDER_SEPARATOR + directory):
                        for sub_dir in sub_dirs:
                            for sub_sub_root, sub_sub_dirs, sub_sub_files in os.walk(
                                    self.data_folder_path + Constants.FOLDER_SEPARATOR + directory + Constants.FOLDER_SEPARATOR + sub_dir):
                                for file in sub_sub_files:
                                    full_file_path = self.data_folder_path + Constants.FOLDER_SEPARATOR + directory + Constants.FOLDER_SEPARATOR + sub_dir + Constants.FOLDER_SEPARATOR + file
                                    sport_df = pd.read_csv(full_file_path, names=['Actual Date', 'Won'])
                                    if sub_dir == Constants.BASEBALL_DIR_NAME:
                                        year = file.split("_")[-1].split(".")[0]
                                        sport_df['Date'] = pd.to_datetime(
                                            sport_df['Actual Date'].apply(lambda x: get_baseball_date(x, year)))
                                    elif sub_dir == Constants.BASKETBALL_DIR_NAME:
                                        sport_df['Date'] = pd.to_datetime(
                                            sport_df['Actual Date'].apply(lambda x: get_basketball_date(x)))
                                    elif sub_dir == Constants.HOCKEY_DIR_NAME:
                                        sport_df['Date'] = pd.to_datetime(
                                            sport_df['Actual Date'].apply(lambda x: get_hockey_date(x)))
                                    elif sub_dir == Constants.SOCCER_DIR_NAME:
                                        year = file.split("_")[1].split(".")[0]
                                        sport_df['Date'] = pd.to_datetime(
                                            sport_df['Actual Date'].apply(lambda x: get_soccer_date(x, year)))
                                    self.sports_df = self.sports_df.append(sport_df[['Date', 'Won']])
                                    self.sports_df = self.sports_df.groupby('Date').head(1).reset_index(drop=True)
                elif directory == Constants.CRIME_DIR_NAME:
                    for sub_root, sub_dirs, sub_files in os.walk(
                            self.data_folder_path + Constants.FOLDER_SEPARATOR + directory):
                        for file in sub_files:
                            full_file_path = self.data_folder_path + Constants.FOLDER_SEPARATOR + directory + Constants.FOLDER_SEPARATOR + file
                            crime_df = pd.read_csv(full_file_path, low_memory=False)
                            year = file.split("-")[-1].split(".")[0]
                            if year in Constants.LATEST_YEARS:
                                crime_df = crime_df[['OCCURRED_ON_DATE']][pd.notnull(crime_df['OCCURRED_ON_DATE'])]
                                crime_df['Date'] = pd.to_datetime(crime_df['OCCURRED_ON_DATE'].apply(lambda x: get_crime_date_new(x)))
                            else:
                                crime_df = crime_df[['FROMDATE']][pd.notnull(crime_df['FROMDATE'])]
                                crime_df['Date'] = pd.to_datetime(crime_df['FROMDATE'].apply(lambda x: get_crime_date_old(x)))
                            crime_df = crime_df['Date'].value_counts(dropna=True, sort=True)
                            crime_df = pd.DataFrame(crime_df).reset_index()
                            crime_df.columns = ['Date', 'Crimes']
                            self.crime_df = self.crime_df.append(crime_df)


if __name__ == '__main__':
    data_cleaner = DataCleaner("./data")
    data_cleaner.clean_sports_data()
    output_df = pd.merge(data_cleaner.sports_df, data_cleaner.crime_df, on='Date', how='left')
    output_df = output_df.sort_values(by=["Date"])
    output_df.to_csv("data.csv", index=False)
