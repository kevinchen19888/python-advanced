from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date
from enum import Enum
from typing import Optional


class InstrumentType(Enum):
    """
    金融工具类型
    """

    SPOT = "spot", False
    ETP = 'etp', False
    FUTURE = "future", True
    SWAP = "swap", True
    OPTION = "option", True

    def __init__(self, name: str, short_allowed: bool):
        self._name = name
        self._short_allowed = short_allowed

    def supports_short_trading(self) -> bool:
        """
        是否支持做空

        Returns:
            bool: True 支持做空, False 不支持
        """
        return self._short_allowed


class Instrument(ABC):
    """
    金融工具
    """
    __type__: InstrumentType = None  # 交易工具类型

    @classmethod
    def supports_short_trading(cls) -> bool:
        """
        判断此种类型的金融工具是否支持做空交易

        Returns:
            bool: True 支持，False 不支持
        """
        return cls.__type__.supports_short_trading() if cls.__type__ else False

    @classmethod
    @abstractmethod
    def parse(cls, symbol: str) -> Instrument:
        """
        解析字符串并构造交易工具实例

        Args:
            symbol: 交易工具标识符

        Returns:
            Instrument: 交易工具的实例

        Raises:
            ValueError: 参数错误，无法解析

        """

    @property
    @abstractmethod
    def symbol(self) -> str:
        """
        获取符号
        Returns:
            str: 金融工具标识符
        """


class Currency(Instrument):
    """
    现金
    """

    __type__ = InstrumentType.SPOT

    def __init__(self, currency):
        self._currency = currency

    @classmethod
    def parse(cls, symbol: str) -> Currency:
        raise NotImplementedError('Currency.parse')

    @property
    def symbol(self) -> str:
        return self._currency


class EtpCurrency(Currency):
    __type__ = InstrumentType.ETP

    def __init__(self, currency: str, weigh: str):
        super().__init__(currency)
        self.weigh = weigh

    @classmethod
    def parse(cls, symbol: str) -> EtpCurrency:
        raise NotImplementedError("EtpCurrency.parse")

    @property
    def symbol(self) -> str:
        return f"{self._currency}*{self.weigh}"


class Underlying(ABC):
    """标的资产"""

    @property
    @abstractmethod
    def symbol(self) -> str:
        """
        获取符号
        Returns:
            str: 标的资产的标识符
        """


class CustomUnderlying(Underlying):
    """自由格式的标的资产"""

    def __init__(self, underlying_symbol: str):
        self.underlying_symbol = underlying_symbol

    @property
    def symbol(self) -> str:
        return f"_{self.underlying_symbol}"


class SpotUnderlying(Underlying):
    """严格格式的：现货标的资产"""

    def __init__(self, asset: Currency, currency: Currency):
        self.asset = asset  # 现货资产
        self.currency = currency  # 现金

    @property
    def symbol(self) -> str:
        return f"_{self.asset.symbol}${self.currency.symbol}"


class Contract(Instrument, ABC):
    """
    合约
    """

    __type__ = None

    def __init__(self, underlying: Underlying):
        self.underlying = underlying


class FutureAlias(Enum):
    """
    合约别名
    """
    THIS_WEEK = "TW"
    NEXT_WEEK = "NW"
    THIS_QUARTER = "TQ"
    NEXT_QUARTER = "NQ"

    def __init__(self, abbr: str):
        self._abbr = abbr

    @property
    def abbreviation(self):
        """简写"""
        return self._abbr


class FutureContract(Contract):
    """
    交割合约
    """

    __type__ = InstrumentType.FUTURE

    def __init__(self, underlying: Underlying, delivery_date: date, alias: Optional[FutureAlias] = None):
        super().__init__(underlying=underlying)
        self.delivery_date = delivery_date
        self.alias = alias

    @classmethod
    def parse(cls, symbol: str) -> FutureContract:
        raise NotImplementedError('FutureContract.parse')

    @property
    def symbol(self) -> str:
        result = f"{self.underlying.symbol}@{self.delivery_date.strftime('%y%m%d')}"
        if self.alias is not None:
            result += f'[{self.alias.abbreviation}]'
        return result


class SwapContract(Contract):
    """
    永续合约
    """

    __type__ = InstrumentType.SWAP

    @classmethod
    def parse(cls, symbol: str) -> SwapContract:
        raise NotImplementedError('SwapContract.parse')

    @property
    def symbol(self) -> str:
        return f"{self.underlying.symbol}"


class OptionType(Enum):
    """
    期权类型
    """

    CALL = 0  # 看涨期权
    PUT = 1  # 看跌期权


class OptionContract(Contract):
    """
    期权合约
    """

    __type__ = InstrumentType.OPTION

    def __init__(self, underlying: Underlying, option_type: OptionType):
        super().__init__(underlying)
        self.option_type = option_type

    @classmethod
    def parse(cls, symbol: str) -> OptionContract:
        raise NotImplementedError('OptionContract.parse')

    @property
    def symbol(self) -> str:
        raise NotImplementedError('OptionContract.symbol')


class FaitCurrency(Enum):
    """
    法币类型
    """
    USD = 'usd'
    CNY = 'cny'
