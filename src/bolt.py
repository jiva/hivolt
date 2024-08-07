# Bolt pattern
# 0.0 = left eye
# 0.1 = right eye
# 0.2 = left smile
# 0.3 = left frown
# 0.4 = left mouth
# 0.5 = right mouth
# 0.6 = right smile
# 0.7 = right frown
#
# -> 0x77 = smiling
# -> 0xbb = frowning
class boltAnimator:
    BOLT_ANIMATION = [
        [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # All off
        [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # All off
        [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # All off
        [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # All off
        [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # All off
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff ], # Smiling
        [ 0x77, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff ], # Smiling
        [ 0x77, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff ], # Smiling
        [ 0x77, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff ], # Smiling
        [ 0x77, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff ], # Smiling
        [ 0x77, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00 ], # Smiling
        [ 0x77, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00 ], # Smiling
        [ 0x77, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling blink
        [ 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling blink
        [ 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling blink
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling
        [ 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling blink
        [ 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling blink
        [ 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Smiling blink
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
        [ 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ], # Frowning
    ]

    def length(self):
        return len(self.BOLT_ANIMATION)

    def updateBolt(self):
        for i in range(0,8):
            self._bolt[i] = self.BOLT_ANIMATION[self._offset][i]
        self._offset = (self._offset + 1) % len(self.BOLT_ANIMATION)

    def __init__(self, buffer):
        self._bolt = buffer
        self._offset = 0
