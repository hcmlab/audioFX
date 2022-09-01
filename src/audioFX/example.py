from Fx import Fx

from librosa import load

_WRITE_BACKEND = "soundfile"

if _WRITE_BACKEND == "scipy":
    import numpy as np
    from scipy import io
elif _WRITE_BACKEND == "soundfile":
    import soundfile as sf

infile = 'test.wav'
outfile = 'my_processed_audio_file.wav'

x, sr = load(infile)

# Define dict with the effect chain. The signal is passed through the chain in the same order as the effects in the dictionary.
# Values represent the dry/wet portion of the signal. 0.0 = dry, 1.0 = wet.
# Implemented effects: flanger, distortion, wahwah, tremolo, chorus, pitch, griffin
fx_factors = {"pitch": 0.0,
              "tremolo": 0.0,
              "flanger": 0.0,
              "griffin": 0.0,
              "timestretch": 1.0
              }

# Define dict to control additional parameters of the effects. If a parameter is not defined, the default value is used.
# Parameters can be:
# flanger_frequency, flanger_depth, flanger_delay
# chorus_frequency, chorus_depth, chorus_delay
# tremolo_alpha, tremolo_modfreq
# distortion_alpha
# wahwah_damp, wahwah_minf, wahwah_maxf, wahwah_wahf
# pitch_semitones, pitch_mirror
# griffin_iters
additional_parameters = {"pitch_semitones": 12.0,
                         "pitch_mirror": True,
                         "tremolo_alpha": 1.0,
                         "tremolo_modfreq": 10.0,
                         "flanger_frequency": 0.75,
                         "flanger_depth": 9.75,
                         "flanger_delay": 0.9375,
                         "griffin_iters": 0
                         }



fx = Fx(sr)
y = fx.process_audio(x, fx_factors, additional_parameters)

if _WRITE_BACKEND == "scipy":
    y = np.float32(y)
    io.wavfile.write(outfile, sr, y)
elif _WRITE_BACKEND == "soundfile":
    sf.write(outfile, y, sr)
