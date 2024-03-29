"""
This is the main script which is used for the Web3 portfolio analysis
"""
import pandas as pd
import keplr
import metamask
import phantom
import sui
import yaml
import logging
from functions import calculate_metrics


def run():
    logging.basicConfig(level=logging.INFO, format='\033[92m%(asctime)s - %(levelname)s: %(message)s\033[0m')
    logging.info('Maxu farmu activated...')
    logging.info('Remember to close excel data file!!!')
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)

    # read in wallet data
    wallets_file = 'data/Web3 wallets.xlsx'
    wallets = pd.read_excel(wallets_file, sheet_name=['phantom', 'keplr', 'metamask', 'sui', 'investment'])

    # calculate dollar value for all wallets
    logging.info("Running the analysis for Phantom wallet...")
    phantom_data = phantom.run(data=wallets['phantom'], config=config['phantom'])
    logging.info("Running the analysis for Keplr wallet...")
    keplr_data = keplr.run(data=wallets['keplr'], config=config['keplr'])
    logging.info("Running the analysis for Metamask wallet...")
    metamask_data = metamask.run(data=wallets['metamask'], config=config['metamask'])
    logging.info("Running the analysis for Sui wallet...")
    sui_data = sui.run(data=wallets['sui'], config=config['sui'])

    # create df with relevant metrics
    metrics = calculate_metrics(investments=wallets['investment'], phantom_data=phantom_data, keplr_data=keplr_data,
                      metamask_data=metamask_data, sui_data=sui_data)

    logging.info('Maxu farmu ran succesfully...')


if __name__ == "__main__":
    run()
