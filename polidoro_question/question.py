import datetime
import re

import dateutil.parser
from functools import lru_cache

from polidoro_terminal import Format, getch, up_lines
from polidoro_terminal.getch import Key
from polidoro_terminal.manipulation import clear_to_end_of_screen, move_right, move_left

try:
    import i18n
    import locale

    @lru_cache
    def _(text):
        return i18n.t(text)
    lc, encoding = locale.getdefaultlocale()

    i18n.set('locale', lc)
    i18n.set('filename_format', '{locale}.{format}')
    i18n.load_path.append('locale')
except ImportError:
    _ = str


class Question:
    def __init__(self, question, type=str, default=None, options=None, options_alias=None, auto_complete=False,
                 **kwargs):
        self.question = _(question)
        self.type = type
        self.use_getch = False

        self.default = default

        self.options = options
        self.translated_options = {}
        self._normalize_options()

        self.auto_complete = auto_complete

        self.options_alias = options_alias or {}
        if not auto_complete:
            self._define_options_alias()

    def ask(self):
        extra_info = self._build_extra_info()

        print_answer = False
        prompt = f'{self.question}{extra_info}: '
        if self.auto_complete:
            resp = self.auto_complete_ask(prompt)
        else:
            if self.use_getch:
                print_answer = True
                print(prompt, end='', flush=True)
                resp = getch()
            else:
                resp = input(prompt)

            resp = resp.strip()
            if not resp:
                resp = self.default

            if resp is not None:
                resp = self.options_alias.get(resp, resp)
        if print_answer:
            print(resp)

        if resp is None:
            return
        if isinstance(resp, str):
            resp = self.options_alias.get(resp.upper(), self.options_alias.get(resp.lower(), resp))
            resp = self.translated_options.get(resp, resp)
            if self.type in [int, float]:
                return self.type(resp)
            if self.type in [datetime.date]:
                return dateutil.parser.parse(resp)
        return resp

    def auto_complete_ask(self, prompt):
        options = self.options
        options_filter = ''
        resp = None
        while resp is None:
            print(f'{prompt}{options_filter}')
            for index, o in enumerate(options[:10]):
                print(f'{index} -> {o}')
            up_lines(min(len(options), 10) + 1)
            move_right(len(prompt) + len(options_filter))
            try:
                user_input = getch(translate_commands=True)
            finally:
                move_left(len(prompt) + len(options_filter))
                clear_to_end_of_screen()

            if isinstance(user_input, Key):
                if user_input == Key.BACKSPACE:
                    options_filter = options_filter[:-1]
                elif user_input == Key.ENTER:
                    resp = options[0]
            elif user_input.isdigit():
                resp = options[int(user_input)]
            else:
                options_filter += user_input
            if resp is None:
                options = list(filter(lambda _o: re.search(f'{options_filter.lower()}.*', _o.lower()), self.options))
        print(f'{prompt}{resp}')
        return resp

    def _build_extra_info(self):
        extra_info = ''
        options = self.options
        if self.options_alias:
            options = []
            for alias, option in self.options_alias.items():
                options.append(option.replace(alias, f'{Format.UNDERLINE}{alias}{Format.NORMAL}', 1))
        if options and not self.auto_complete:
            extra_info = f'[{"/".join(o.upper() if o == self.default else o for o in options)}]'
        elif self.default is not None:
            extra_info += f'({self.default})'
        return extra_info

    def _normalize_options(self):
        if self.type == bool:
            self.options = [_('y'), _('n')]
            self.default = _('y' if self.default else 'n')
            self.translated_options = {_('y'): True, _('n'): False}
        elif self.options is not None:
            if isinstance(self.options, list):
                normalized_options = []
                for o in self.options:
                    option = _(str(o))
                    self.translated_options[option] = o
                    normalized_options.append(option)
                self.options = normalized_options
            elif isinstance(self.options, dict):
                self.translated_options = self.options
                self.options = list(self.options.keys())

    def _define_options_alias(self):
        alias = {}
        if self.options:
            self.use_getch = True
            max_len = max(len(o) for o in self.options)
            if max_len > 1:
                for o in self.options:
                    i = 0
                    try:
                        while o[i] in alias:
                            i += 1
                        alias[o[i]] = o
                    except IndexError:
                        raise ValueError(f'Cannot automatically determinate an alias for {o}: {alias}')

        self.options_alias = alias
