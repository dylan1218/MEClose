import datetime
import pandas as pd
from pandas.tseries.offsets import BDay
import calendar
import os
from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User
#Note to self -- this is where you'll define the database schema
#For example, for a task checklist I would create var fields defined like
#"TaskID", "Task Description", "Task Due Data" "Task Owner" etc
#each class represents a database table, for each checklist should likely have a table
