# Circuit Playground 808 Drum machine
import time
import board
import neopixel
import digitalio
import random

try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

bpm = 200  # Beats per minute, change this to suit your tempo

# Enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True


buttonPads = (digitalio.DigitalInOut(board.A1), digitalio.DigitalInOut(board.A2),
              digitalio.DigitalInOut(board.A3), digitalio.DigitalInOut(board.TX),
              digitalio.DigitalInOut(board.A5), digitalio.DigitalInOut(board.A6),
              digitalio.DigitalInOut(board.A4))

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

for i in range(7):
    buttonPads[i].direction = digitalio.Direction.INPUT
    buttonPads[i].pull = digitalio.Pull.UP


# The seven files assigned to the buttonPads
audiofiles = ["elec_blip2.wav", "bass_hit_c.wav", "bd_tek.wav",
              "bd_zome.wav", "elec_cymbal.wav", "elec_hi_snare.wav","blank.wav"
              ]

audio = AudioOut(board.SPEAKER)


def play_file(filename):
    print("playing file " + filename)
    file = open(filename, "rb")
    wave = WaveFile(file)
    audio.play(wave)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(bpm / 960)  # Sixteenth note delay


buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.switch_to_input(pull=digitalio.Pull.DOWN)

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.switch_to_input(pull=digitalio.Pull.UP)

while True:
    for i in range(7):
        if buttonPads[i].value is False and switch.value is False:
            pixels[i] = (random.randrange(1, 100, 1), random.randrange(1, 100, 1),
                         random.randrange(1, 100, 1))
            pixels.show()
            play_file(audiofiles[i])

    if switch.value is True:
        if buttonPads[2].value is False:
            dieroll = random.randrange(1, 7, 1)
            print(dieroll)
            print("playing file " + "bd_tek.wav")
            # file = open("bd_tek.wav", "rb")
            # wave = WaveFile(file)
            # audio.play(wave)
            for i in range(9):

                pixels[i] = (random.randrange(1, 100, 1), random.randrange(1, 100, 1),
                             random.randrange(1, 100, 1))
                pixels.show()
                play_file(audiofiles[random.randrange(1, 6, 1)])
                time.sleep(.05)
                pixels[i] = (0, 0, 0)
            play_file(audiofiles[0])
            if dieroll == 1:
                pixels[1] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
            elif dieroll == 2:
                pixels[1] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[8] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
            elif dieroll == 3:
                pixels[1] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[8] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[2] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
            elif dieroll == 4:
                pixels[1] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[8] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[2] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[7] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
            elif dieroll == 5:
                pixels[1] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[8] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[2] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[7] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[3] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
            elif dieroll == 6:
                pixels[1] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[8] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[2] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[7] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[3] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
                pixels[6] = (random.randrange(1, 20, 1), random.randrange(1, 20, 1),
                             random.randrange(1, 20, 1))
            pixels.show()

            time.sleep(.5)

    if buttonA.value and bpm < 900:
        bpm = bpm + 50


    elif buttonB.value and bpm > 40:
        bpm = bpm - 50

