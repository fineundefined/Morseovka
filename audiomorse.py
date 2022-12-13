
"""
Audiomorse file.

This file is used to encode morse code to audio
"""

import wave
import math
import struct


def write_signal(wavef, duration, volume=0, rate=44100.0,
                 frequency=1240.0):
    """Create a function to create a sound signal."""
    """
    rate = 44100.0 in Hertz
    duration = 0.1 seconds
    frequency = 1240.0 hertz
    """
    for i in range(int(duration * rate * duration)):
        value = int(volume *
                    math.sin(frequency *
                             math.pi * float(i)
                             / float(rate)))
        data = struct.pack('<h', value)
        wavef.writeframesraw(data)


def morse_to_wav(text, pathjoin):
    """Create a function to record the signal in a certain sequence."""
    wav = wave.open(pathjoin, 'w')
    wav.setnchannels(1)
    wav.setsampwidth(2)
    rate = 44100.0
    wav.setframerate(rate)
    write_signal(wav, 0.9, volume=0)
    for char in text:

        match char:

            case '.':
                write_signal(wav, 0.4, volume=32767)
                write_signal(wav, 0.3, volume=0)

            case '-':
                write_signal(wav, 0.7, volume=32767)
                write_signal(wav, 0.4, volume=0)

            case ' ':
                write_signal(wav, 0.6, volume=0)
            case '/':
                write_signal(wav, 0.6, volume=0)
    wav.close()
