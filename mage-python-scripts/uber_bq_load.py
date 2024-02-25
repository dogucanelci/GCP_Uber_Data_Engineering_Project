from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data_dict, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    for key,value in data_dict.items():

        table_id = 'uber_data_eng_projectno1_db.{}'.format(key)
        config_path = path.join(get_repo_path(), 'io_config.yaml')
        config_profile = 'default'

        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(data_dict[key]),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
