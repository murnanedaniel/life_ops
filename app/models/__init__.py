from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# import all models here
from .check_in import CheckIn
from .comment import Comment
from .issue import Issue
from .issue_activity import IssueActivity
from .life_document import LifeDocument
from .merge_request import MergeRequest
from .mr_activity import MRActivity
from .reminder import Reminder
from .test import Test
from .user import User