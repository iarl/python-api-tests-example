from colorama import Fore, Style, init
from datetime import datetime, timedelta, timezone


class Logger():
    init(autoreset=True)

    def time(self):
        date = datetime.now(timezone.utc).astimezone()
        utc_offset = date.utcoffset() // timedelta(hours=1)
        utc_format = f'+{utc_offset}' if utc_offset > 0 else str(utc_offset)
        format_date = date.strftime('%d-%b-%Y %H:%M:%S UTC') + utc_format
        return format_date

    def logger(self, request, response):
        duration = Style.NORMAL + Fore.WHITE + \
            str(response.elapsed.total_seconds())
        format_date = self.time()
        status = str(response.status_code)
        url = Style.NORMAL + Fore.BLUE + f'{request.url}'
        method = Style.BRIGHT + Fore.WHITE + f'{request.method}'
        if status.startswith('1') or status.startswith('3'):
            status = Style.BRIGHT + Fore.BLUE + \
                f'status = {response.status_code}'
        elif status.startswith('2'):
            status = Style.BRIGHT + Fore.GREEN + \
                f'status = {response.status_code}'
        else:
            status = Style.BRIGHT + Fore.RED + \
                f'status = {response.status_code}'
        test_result = Style.NORMAL + Fore.BLUE + 'test result:'
        parameters = f"{method} {url} {status} {duration}s"
        print(
            f'\n[{format_date}] Sending request {parameters} {test_result}',
            end=' ')
