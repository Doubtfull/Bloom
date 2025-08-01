
import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.keys import KC
from kmk.extensions.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.row_pins = [
    board.GP26, board.GP27, board.GP28, board.GP22, board.GP21, board.GP20
]

keyboard.col_pins = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15
]

keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW

keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NO, KC.NO, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.RSFT,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.APP, KC.RCTL
    ]
]

# Rotary Encoder setup (EC_A=GP27, EC_B=GP26)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP27, board.GP26),)
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)
keyboard.extensions.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
