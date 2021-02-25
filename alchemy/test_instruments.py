from datetime import date

from fight.market import (Currency, FutureContract, SpotUnderlying, FutureAlias, SwapContract, CustomUnderlying,
                          EtpCurrency)


def test_spot_instrument():
    asset = Currency('btc')
    assert asset.symbol == 'btc'

    etp = EtpCurrency('btc', 'down')
    assert etp.symbol == 'btc*down'
    etp = EtpCurrency('btc', '3')
    assert etp.symbol == 'btc*3'
    etp = EtpCurrency('btc', '(-3)')
    assert etp.symbol == 'btc*(-3)'


def test_future_instrument():
    asset = Currency('btc')
    future_contract = FutureContract(SpotUnderlying(asset, Currency('usdt')), delivery_date=date(2021, 3, 26),
                                     alias=FutureAlias.THIS_QUARTER)
    assert future_contract.symbol == '_btc$usdt@210326[TQ]'

    future_contract = FutureContract(SpotUnderlying(asset, Currency('usd')), delivery_date=date(2021, 3, 26))
    assert future_contract.symbol == '_btc$usd@210326'

    future_contract = FutureContract(CustomUnderlying('DOTUSDT'), delivery_date=date(2021, 3, 26))
    assert future_contract.symbol == '_DOTUSDT@210326'

    swap_contract = SwapContract(SpotUnderlying(asset, Currency('usdt')))
    assert swap_contract.symbol == '_btc$usdt'


def test_parse_instrument():
    raise NotImplementedError('test_parse_instrument')
