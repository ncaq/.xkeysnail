import re
from xkeysnail.transform import *

define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL
})

define_keymap(re.compile("Firefox|Chromium"), {
    # g
    K("C-u"): [K("ESC"), set_mark(False)],

    # y
    K("C-t"): [K("C-Dot"), set_mark(False)],

    # /
    K("C-Left_Brace"): [K("C-Slash"), set_mark(False)],

    # a
    K("C-a"): with_mark(K("Home")),

    # o
    K("C-s"): K("C-k"),

    # e
    K("C-d"): with_mark(K("End")),

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

    # x
    K("C-b"): {
        K("j"): [K("C-Home"), K("C-a"), set_mark(True)],
        K("C-u"): pass_through_key,
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
}, "Firefox and Chromium")
