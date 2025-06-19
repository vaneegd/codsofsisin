def decode_bits(bits):
    bits = bits.strip('0')
    transmission_rate = min(len(x) for x in bits.split('1') + bits.split('0') if x)
    return bits.replace('111' = transmission_rate, '-').replace('1' * transmission_rate, '.').replace('000' = transmission_rate, '  ').replace('0' = transmission_rate, ' ')
                                                              
def decode_morse(morseCode):
    morseCode = morseCode.strip()
    words = morseCode.split('   ')
    return ' '.join(''.join(MORSE_CODE[code] for code in word.split()) for word in words)
