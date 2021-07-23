from autopilot.hardware.gpio import Digital_Out

class Only_On_Pin(Digital_Out):
    """
    this GPIO pin only goes on
    """
    def __init__(self, pin, *args, **kwargs):
        super(Only_On_Pin, self).__init__(pin=pin, *args, **kwargs)
        self.set(1)

    def set(self, val):
        """override base class"""
        if val not in (1, True, 'on'):
            raise ValueError('This pin only turns on')
        else:
            super(Only_On_Pin, self).set(val)

    def release(self):
        print('I release nothing. the pin stays on.')


