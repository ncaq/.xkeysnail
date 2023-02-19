import re

from xkeysnail.transform import *

xkeysnail_literal_special_source: list[tuple[str, str]] = [
    ("[", "left_brace"),
    ("]", "right_brace"),
    ("\\", "backslash"),
    ("`", "grave"),
    ("'", "apostrophe"),
    (",", "comma"),
    (".", "dot"),
    ("/", "slash"),
    ("-", "minus"),
    (";", "semicolon"),
]
"""
文字のリテラル表現と、xkeysnailで表現する特殊なキー表現の対応リスト。
[xkeysnail/key.py at master · mooz/xkeysnail · GitHub](https://github.com/mooz/xkeysnail/blob/master/xkeysnail/key.py)
"""


def xkeysnail_literal_special(literal: str) -> str | None:
    """リテラル表現をxkeysnailの表現に変換する。"""
    return next(
        (t[1] for t in xkeysnail_literal_special_source if t[0] == literal), None
    )


def xkeysnail_special_literal(special: str) -> str | None:
    """xkeysnailの表現をリテラル表現に変換する。"""
    return next(
        (t[0] for t in xkeysnail_literal_special_source if t[1] == special), None
    )


dvorak: str = "[]\\`',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz"
"""
USキーボードでDvorakとQwertyで差分が生じる範囲のDvorak側の文字配列。
"""
qwerty: str = "-=\\`qwertyuiop[]asdfghjkl;'zxcvbnm,./"
"""
USキーボードでDvorakとQwertyで差分が生じる範囲のQwerty側の文字配列。
"""


def d2q(key: str) -> str:
    """
    Dvorak to Qwerty.
    """
    literal = xkeysnail_special_literal(key) or key
    try:
        i = dvorak.index(literal)
        q = qwerty[i]
        return xkeysnail_literal_special(q) or q
    except ValueError:
        return key


def D(exp: str) -> Combo:
    """`K`がDvorak設定を無視するので設定側で入れ替えする。"""
    # 末尾の`-`で分割してプレフィクスと単体のキーを取り出す。
    match exp.rsplit("-", 1):
        # "C-w"や"C-Shift-w"を正常に分割出来れば長さは2となる。
        case [prefix, key]:
            return K(f"{prefix}-{d2q(key)}")
        case _:
            # 分割できていない場合単体でキーバインドを指すことが多いため分割せず変換する。
            return K(d2q(exp))


define_modmap({Key.CAPSLOCK: Key.LEFT_CTRL})

define_keymap(
    re.compile("Mikutter.rb|Skype|discord"),
    {
        D("C-m"): [D("Shift-enter"), set_mark(False)],
        D("enter"): [D("enter"), set_mark(False)],
    },
    "改行と投稿を統一する",
)

define_keymap(
    re.compile("Slack"),
    {
        D("C-m"): [D("enter"), set_mark(False)],
        D("enter"): [D("Ctrl-enter"), set_mark(False)],
    },
    "改行と投稿を統一する",
)

define_keymap(
    re.compile("Slack|discord"),
    {
        # チャンネルスイッチのキーバインドを使いやすくします。
        # 下に移動。
        D("M-j"): [D("M-Shift-down")],
        # 上に移動。
        D("M-k"): [D("M-Shift-up")],
        # 下の未読に移動。
        D("M-n"): [D("M-down")],
        # 上の未読に移動。
        D("M-t"): [D("M-up")],
    },
    "Slack and Discord",
)

define_keymap(
    re.compile("Slack|discord|kitty"),
    {
        D("C-comma"): D("muhenkan"),
        D("C-dot"): D("henkan"),
    },
    "`C-,`, `C-.`のショートカットを無効化する",
)

define_keymap(
    re.compile(
        "|".join(
            [
                "Chromium",
                "Jdim",
                "Mikutter.rb",
                "Skype",
                "Slack",
                "copyq",
                "discord",
                "firefox",
                "jetbrains-idea-ce",
                "thunderbird",
            ]
        )
    ),
    {
        D("C-g"): [D("esc"), set_mark(False)],
        D("C-y"): [D("C-v"), set_mark(False)],
        D("C-slash"): [D("C-z"), set_mark(False)],
        D("C-backslash"): escape_next_key,
        D("C-a"): with_mark(D("home")),
        D("C-o"): D("C-t"),
        D("M-o"): D("C-Shift-t"),
        D("M-minus"): D("C-Shift-t"),
        D("C-e"): with_mark(D("end")),
        D("C-u"): [D("home"), D("Shift-end"), D("C-x"), set_mark(False), D("delete")],
        D("C-d"): [D("delete"), set_mark(False)],
        D("M-d"): [D("C-delete"), set_mark(False)],
        D("C-h"): with_mark(D("left")),
        D("M-h"): with_mark(D("C-left")),
        D("C-s"): with_mark(D("right")),
        D("M-s"): with_mark(D("C-right")),
        D("C-t"): with_mark(D("up")),
        D("C-n"): with_mark(D("down")),
        D("C-q"): D("C-w"),
        D("C-k"): [D("Shift-end"), D("C-x"), set_mark(False)],
        D("C-x"): {
            D("C-g"): pass_through_key,
            D("h"): [D("C-home"), D("C-a"), set_mark(True)],
        },
        D("C-b"): [D("backspace"), set_mark(False)],
        D("M-b"): [D("C-backspace"), set_mark(False)],
        D("C-m"): [D("enter"), set_mark(False)],
        D("C-w"): [D("C-x"), set_mark(False)],
        D("M-w"): [D("C-c"), set_mark(False)],
        D("C-space"): set_mark(True),
        D("C-Shift-space"): set_mark(True),
    },
    "Web textarea like Application",
)
