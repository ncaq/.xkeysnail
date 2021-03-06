import re
from xkeysnail.transform import *

define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL
})

define_keymap(re.compile("Mikutter.rb|Skype|discord"), {
    K("C-m"): [K("Shift-Enter"), set_mark(False)],
    K("Enter"): [K("Enter"), set_mark(False)],
}, "改行と投稿を統一する")

define_keymap(re.compile("Slack"), {
    K("C-m"): [K("Shift-Enter"), set_mark(False)],
    K("Enter"): [K("Ctrl-Enter"), set_mark(False)],
}, "改行と投稿を統一する")

define_keymap(re.compile("Slack|discord"), {
    # j
    K("M-c"): [K("M-Shift-Down")],
    # k
    K("M-v"): [K("M-Shift-Up")],
    # n
    K("M-l"): [K("M-Down")],
    # t
    K("M-k"): [K("M-Up")],
}, "Slack and Discord switch channel")

define_keymap(re.compile("LilyTerm|Slack|discord"), {
    K("C-w"): K("MUHENKAN"),
    K("C-e"): K("HENKAN"),
}, "C-,、C-.のショートカットを無効化する")

define_keymap(re.compile("XCOM2"), {
    # ,
    K("w"): K("COMMA"),
    # .
    K("e"): K("DOT"),
}, "XCOM2のWとEが謎の動作をするのを修正")

define_keymap(re.compile(
    "Chromium|"
    "Firefox|"
    "Jdim|"
    "Mikutter.rb|"
    "Skype|"
    "Slack|"
    "Thunderbird|"
    "copyq|"
    "discord|"
    "jetbrains-idea-ce"
), {
    # g
    K("C-u"): [K("ESC"), set_mark(False)],

    # y
    K("C-t"): [K("C-Dot"), set_mark(False)],

    # /
    K("C-Left_Brace"): [K("C-Slash"), set_mark(False)],

    # \
    K("C-Backslash"): escape_next_key,

    # a
    K("C-a"): with_mark(K("Home")),

    # o
    K("C-s"): K("C-k"),
    K("M-s"): K("C-Shift-k"),

    # -
    K("M-Apostrophe"): K("C-Shift-k"),

    # e
    K("C-d"): with_mark(K("End")),

    # u
    K("C-f"): [K("Home"), K("Shift-End"), K("C-b"), set_mark(False)],

    # d
    K("C-h"): [K("Delete"), set_mark(False)],
    K("M-h"): [K("C-Delete"), set_mark(False)],

    # h
    K("C-j"): with_mark(K("Left")),
    K("M-j"): with_mark(K("C-Left")),

    # s
    K("C-Semicolon"): with_mark(K("Right")),
    K("M-Semicolon"): with_mark(K("C-Right")),

    # t
    K("C-k"): with_mark(K("Up")),

    # n
    K("C-l"): with_mark(K("Down")),

    # q
    K("C-x"): K("C-comma"),

    # k
    K("C-v"): [K("Shift-End"), K("C-b"), set_mark(False)],

    # x
    K("C-b"): {
        # g
        K("C-u"): pass_through_key,
        # h
        K("j"): [K("C-Home"), K("C-a"), set_mark(True)],
    },

    # b
    K("C-n"): [K("Backspace"), set_mark(False)],
    K("M-n"): [K("C-Backspace"), set_mark(False)],

    # m
    K("C-m"): [K("Enter"), set_mark(False)],

    # w
    K("C-comma"): [K("C-b"), set_mark(False)],
    K("M-comma"): [K("C-i"), set_mark(False)],

    # space
    K("C-space"): set_mark(True),
    K("Shift-C-space"): set_mark(True),
}, "Web textarea like Application")
