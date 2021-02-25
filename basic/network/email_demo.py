import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def send_email_demo():
    # 输入email地址和口令
    from_addr = input('from:')
    psd = input('password:')
    # 输入收件人地址
    to_addr = input('to:')
    # 输入smtp服务器地址
    smtp_server = input('smtp server:')
    # smtp协议默认端口25
    server = smtplib.SMTP(smtp_server, 25)
    # 打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    server.login(from_addr, psd)
    # 构造邮件
    '''
    构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
    最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
    '''
    msg = MIMEText('hello,send by kevin', 'plain', 'utf8')
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    server.sendmail(from_addr, [to_addr], msg.as_string())  # 因为可以发给多个人,所以to_addr为list
    server.quit()


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


send_email_demo()
