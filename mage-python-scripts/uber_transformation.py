import pandas as pd
from datetime import datetime

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df['trip_id'] = df.index
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    datetime_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)
    datetime_dim['datetime_id'] = datetime_dim.index
    #datetime_dim['tpep_pickup_datetime'] = datetime_dim[]
    datetime_dim['tpep_pickup_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['tpep_pickup_week'] = datetime_dim['tpep_pickup_datetime'].dt.week
    datetime_dim['tpep_pickup_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['tpep_pickup_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['tpep_pickup_dayname'] = datetime_dim['tpep_pickup_datetime'].dt.day_name()
    #datetime_dim['tpep_dropoff_datetime'] = 
    datetime_dim['tpep_dropoff_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['tpep_dropoff_week'] = datetime_dim['tpep_dropoff_datetime'].dt.week
    datetime_dim['tpep_dropoff_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['tpep_dropoff_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['tpep_dropoff_dayname'] = datetime_dim['tpep_dropoff_datetime'].dt.day_name()
    
    passenger_dim = df[['passenger_count']].drop_duplicates().reset_index(drop=True)
    passenger_dim['passenger_id'] = passenger_dim.index
    location_dim = df[['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']].drop_duplicates().reset_index(drop=True)
    location_dim['location_id'] = location_dim.index

    rate_dim = df[['RatecodeID']].drop_duplicates().reset_index(drop=True)
    rate_dim['rate_id'] = rate_dim.index
    rate_dim.loc[rate_dim['RatecodeID'] == 1,'rate_code_name'] = 'Standard rate'
    rate_dim.loc[rate_dim['RatecodeID'] == 2,'rate_code_name'] = 'JFK'
    rate_dim.loc[rate_dim['RatecodeID'] == 3,'rate_code_name'] = 'Newark'
    rate_dim.loc[rate_dim['RatecodeID'] == 4,'rate_code_name'] = 'Nassau or Westchester'
    rate_dim.loc[rate_dim['RatecodeID'] == 5,'rate_code_name'] = 'Negotiated fare'
    rate_dim.loc[rate_dim['RatecodeID'] == 6,'rate_code_name'] = 'Group ride'
    
    payment_dim = df[['payment_type']].drop_duplicates().reset_index(drop=True)
    payment_dim['payment_id'] = payment_dim.index
    payment_dim.loc[payment_dim['payment_type'] == 1,'payment_type_name'] = 'Credit card'
    payment_dim.loc[payment_dim['payment_type'] == 2,'payment_type_name'] = 'Cash'
    payment_dim.loc[payment_dim['payment_type'] == 3,'payment_type_name'] = 'No charge'
    payment_dim.loc[payment_dim['payment_type'] == 4,'payment_type_name'] = 'Dispute'
    payment_dim.loc[payment_dim['payment_type'] == 5,'payment_type_name'] = 'Unknown'
    payment_dim.loc[payment_dim['payment_type'] == 6,'payment_type_name'] = 'Voided trip'

    fact_table = df.merge(datetime_dim,on=['tpep_pickup_datetime','tpep_dropoff_datetime']) \
    .merge(location_dim,on=['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']) \
    .merge(passenger_dim,on='passenger_count') \
    .merge(rate_dim,on='RatecodeID') \
    .merge(payment_dim,on='payment_type') \
    [['trip_id','datetime_id','location_id','passenger_id','rate_id','payment_id','trip_distance'
      ,'fare_amount',
       'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
       'improvement_surcharge', 'total_amount'
      ]]

    main_dict = {'datetime_dim':datetime_dim.to_dict(orient='dict'),
             'passenger_dim':passenger_dim.to_dict(orient='dict'),
             'location_dim':location_dim.to_dict(orient='dict'),
             'rate_dim':rate_dim.to_dict(orient='dict'),
             'payment_dim':payment_dim.to_dict(orient='dict'),
             'fact_table':fact_table.to_dict(orient='dict')             
             }
    return main_dict


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
