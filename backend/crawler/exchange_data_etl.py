import datetime
import logging
import sys
from typing import Any, Dict, List, Optional
import requests
from models import Exchange
from app import db  


def get_utc_from_unix_time(unix_ts: Optional[Any], second: int = 1000) -> Optional[datetime.datetime]:
    return (
        datetime.datetime.utcfromtimestamp(int(unix_ts) / second)
        if unix_ts
        else None
    )


def get_exchange_data() -> List[Dict[str, Any]]:
    url = 'https://api.coincap.io/v2/exchanges'
    try:
        r = requests.get(url)
    except requests.HTTPError as e:
        logging.error(f"There was an error with the request, {e}")
        sys.exit(1)
    return r.json().get('data', [])


def insert_exchange_data() -> None:
    print("Inserting data...")
    data = get_exchange_data()
    records = []
    for item in data:
        item['id'] = item["exchangeId"]
        del item["exchangeId"]
        item['updated_utc'] = get_utc_from_unix_time(item.get('updated'))
        item['updated_unix_millis'] = item['updated']
        del item['updated']
        item['socket'] = True if item['socket'] == 'true' else False
        records.append(Exchange(**item))
    db.session.add_all(records)
    db.session.commit()

    # with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        # p.execute_batch(curr, _get_exchange_insert_query(), data)
# def _get_exchange_insert_query() -> str:
#     return '''
#     INSERT INTO bitcoin.exchange (
#         id,
#         name,
#         rank,
#         percenttotalvolume,
#         volumeusd,
#         tradingpairs,
#         socket,
#         exchangeurl,
#         updated_unix_millis,
#         updated_utc
#     )
#     VALUES (
#         %(exchangeId)s,
#         %(name)s,
#         %(rank)s,
#         %(percentTotalVolume)s,
#         %(volumeUsd)s,
#         %(tradingPairs)s,
#         %(socket)s,
#         %(exchangeUrl)s,
#         %(updated)s,
#         %(update_dt)s
#     );
#     '''

# insert
# >>> from yourapp import User
# >>> me = User('admin', 'admin@example.com')
# >>> db.session.add(me)
# >>> db.session.commit()

# delete
# >>> db.session.delete(me)
# >>> db.session.commit()

# get
# >>> peter = User.query.filter_by(username='peter').first()
# >>> peter.id
# 2
# >>> peter.email

