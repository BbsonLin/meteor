from settings import app_config, AppConfig, DatabaseConfig
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session, ScopedSession
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine


class SQLAlchemyAdapter(object):
    def __init__(self, config: DatabaseConfig) -> None:
        self._engine = create_engine(config.CONNECTION_STRING)
        # 建立 Session 類別
        session_factory = sessionmaker(self._engine)
        # 透過 scoped_session 加工對 Session 類別註冊，使得 Session 未釋放時可以再利用，而不需要每一個請求建立一個 Session
        self._session_regisetry: ScopedSession = scoped_session(session_factory)
        self._curr_session = None

    def register_session(self) -> None:
        self._curr_session = self._session_regisetry()

    @property
    def session(self) -> Session:
        if self._curr_session is None:
            self.register_session()
        return self._curr_session

    def remove_session(self) -> None:
        self._session_regisetry.remove()


database_adapter = SQLAlchemyAdapter(app_config.DATABASE)
