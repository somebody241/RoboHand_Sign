import sign_letters
from hand import Hand
import code

rh = Hand(code.right_hand)
lh = Hand(code.left_hand)

table = dict()
table['а'] = []
table['а'] += sign_letters.sign_a(rh)
table['б'] = []
table['б'] += sign_letters.sign_b(rh)
table['в'] = []
table['в'] += sign_letters.sign_v(rh)
table['г'] = []
table['г'] += sign_letters.sign_g(lh)
table['е'] = []
table['е'] += sign_letters.sign_e(rh)
table['и'] = []
table['и'] += sign_letters.sign_i(rh)
table['л'] = []
table['л'] += sign_letters.sign_l(lh)
table['м'] = []
table['м'] += sign_letters.sign_m(lh)
table['н'] = []
table['н'] += sign_letters.sign_n(rh)
table['о'] = []
table['о'] += sign_letters.sign_o(rh)
table['п'] = []
table['п'] += sign_letters.sign_p(lh)
table['р'] = []
table['р'] += sign_letters.sign_r(rh)
table['т'] = []
table['т'] += sign_letters.sign_t(lh)
table['у'] = []
table['у'] += sign_letters.sign_u(rh)
table['х'] = []
table['х'] += sign_letters.sign_h(rh)
table['ц'] = []
table['ц'] += sign_letters.sign_c(rh)
table['ч'] = []
table['ч'] += sign_letters.sign_ch(rh)
table['ш'] = []
table['ш'] += sign_letters.sign_sh(rh)
table['ю'] = []
table['ю'] += sign_letters.sign_yu(rh)
