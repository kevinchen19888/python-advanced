import random


def check_condition(condition):
    print("检查入场条件")
    return True


def trade(one_asset, middle_line, stop_loss_line, floating_stop_profit):
    print("进行交易,使用资金:%s,middle_line:%s,stop_loss_line:%s,floating_stop_profit:%s" %
          (one_asset, middle_line, stop_loss_line, floating_stop_profit))
    pass


def get_new_price():
    price = random.randint(0, 1000)
    print("获取最新价格:%s" % price)
    return price


def close_out():
    print("账户所有持仓进行平仓")
    pass


# 趋势型网格交易法则的规则：
# （1）将资金分为10份
# （2）达到入场条件（做多或做空），使用一份资金入场
# （3）以做多为例：设置中线（等于入场价），按着一定规则（如：止损线=0.9*入场价）浮动止盈线和止损线，一般来说，（浮动止盈线-中线）=1.1*（中线-止损线）
# （4）当后续的股价触发止损线，所有资金平仓出局
# （5）当后续股价触到浮动止盈线，将中线上移到浮动止盈线，同时根据此时的中线计算新的止损线和浮动止盈线，与此同时，加码一份资金
# （6）重复（5），直到达到条件（4），平所有仓位

# 趋势型网格交易法核心算法
def trend_grid(asset, condition, trade_role):
    """
    趋势型网格交易法核心算法
    :param asset: 投入资金
    :param condition: 入场条件
    :param trade_role: 交易规则
    """
    if asset == 0:
        return
    equation_assets = [asset / 10 for x in range(10)]
    # 检查入场条件
    if check_condition(condition):
        middle_line = get_new_price()
        stop_loss_line = trade_role.get_stop_loss_factor() * middle_line
        floating_stop_profit = middle_line + trade_role.get_floating_stop_profit_factor() * (
                middle_line - stop_loss_line)
        # 如果价格没有触发止损线
        new_price = get_new_price()
        while new_price > stop_loss_line:
            new_price = get_new_price()
            if new_price >= floating_stop_profit:
                middle_line = floating_stop_profit
                stop_loss_line = trade_role.get_stop_loss_factor() * middle_line
                floating_stop_profit = middle_line + trade_role.get_floating_stop_profit_factor() * (
                        middle_line - stop_loss_line)
                # 进行下单交易
                one_asset = equation_assets.pop()
                trade(one_asset, middle_line, stop_loss_line, floating_stop_profit)
                # 加码资金
                new_one_asset = one_asset
                equation_assets.append(new_one_asset)
        # 触发止损线,平仓
        close_out()


# 入场条件封装(简单封装了多空类型&触发价格)
class Condition(object):
    def __init__(self, long_short_type, price) -> None:
        self.price = price
        self.long_short_type = long_short_type

    def get_long_short_type(self):
        return self.long_short_type

    def get_price(self):
        return self.price


# 交易规则基类(其他规则继承此类)
class TradeRole(object):

    def __init__(self, stop_loss_factor, floating_stop_profit_factor) -> None:
        self.stop_loss_factor = stop_loss_factor
        self.floating_stop_profit_factor = floating_stop_profit_factor

    def get_stop_loss_factor(self):
        return self.stop_loss_factor

    def get_floating_stop_profit_factor(self):
        return self.floating_stop_profit_factor


def run():
    condition = Condition(1, get_new_price())
    trade_role = TradeRole(0.9, 1.1)
    trend_grid(100, condition, trade_role)


# 运行方法 todo
run()
