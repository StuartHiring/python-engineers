import sys
from pathlib import Path
import pytest

sys.path.insert(1, str(Path(__file__).parents[1]))
from courier import Courier
from datetime import datetime

@pytest.fixture
def valid_courier(scope='session'):
    return Courier(first_name='Danny',
                surname='DeVito',
                city='london',
                country='UK',
                valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'),
                vehicle='unicycle',
                courier_id= 44
                )
