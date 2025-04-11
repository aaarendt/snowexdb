from insitupy.campaigns.snowex import SnowExPrimaryVariables, SnowExProfileData


def read_csv():

    fnames = [
    "/home/arendta/git/snow/snowex_db/scripts/download/data/SNOWEX/SNEX20_TS_SP.001/2020.04.27/SNEX20_TS_SP_20200427_0845_COERAP_data_temperature_v01.csv",
    # "/home/arendta/git/snow/snowex_db/scripts/download/data/SNOWEX/SNEX20_TS_SP.001/2020.04.27/SNEX20_TS_SP_20200427_0845_COERAP_data_LWC_v01.csv",
    # "/home/arendta/git/snow/snowex_db/scripts/download/data/SNOWEX/SNEX20_TS_SP.001/2020.04.27/SNEX20_TS_SP_20200427_0845_COERAP_data_LWC_v01.csv",
    # "/home/arendta/git/snow/snowex_db/scripts/download/data/SNOWEX/SNEX20_TS_SP.001/2020.04.27/SNEX20_TS_SP_20200427_0845_COERAP_data_density_v01.csv",
    ]
    variables = [
        SnowExPrimaryVariables.SNOW_TEMPERATURE,
        #SnowExPrimaryVariables.LWC,
        #SnowExPrimaryVariables.PERMITTIVITY,
        #SnowExPrimaryVariables.DENSITY
    ]

    obj = SnowExProfileData.from_csv(fname, variable, allow_map_failures=True)
    profile = obj.get_profile()
    return profile