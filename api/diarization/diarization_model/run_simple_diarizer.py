import soundfile as sf
import matplotlib.pyplot as plt
import sys
import io

from simple_diarizer.diarizer import Diarizer
from simple_diarizer.utils import combined_waveplot


def diarize(wav_file: str):
    diar = Diarizer(
        embed_model='ecapa',  # 'xvec' and 'ecapa' supported
        cluster_method='ahc'  # 'ahc' and 'sc' supported
    )
    segments = diar.diarize(wav_file=wav_file,
                            num_speakers=2,
                            outfile=f'{wav_file.rstrip(".wav")}_simple.rttm')
    # print(segments)
    # signal, fs = sf.read(wav_file)
    # combined_waveplot(signal, fs, segments)
    # plt.show()
    return segments


def diarizePlot(wav_file: str):
    diar = Diarizer(
        embed_model='ecapa',  # 'xvec' and 'ecapa' supported
        cluster_method='ahc'  # 'ahc' and 'sc' supported
    )
    segments = diar.diarize(wav_file=wav_file,
                            num_speakers=2,
                            outfile=f'{wav_file.rstrip(".wav")}_simple.rttm')
    # print(segments)
    signal, fs = sf.read(wav_file)
    plt.switch_backend('AGG')
    fig = combined_waveplot(signal, fs, segments)
    # plt.show()
    img_buf = io.BytesIO()
    fig.savefig(img_buf, format='png')
    img_buf.seek(0)
    return img_buf


def main(args):
    if len(args) != 1:
        sys.stderr.write(
            'Usage: run_simple_diarize.py <path to wav file>\n')
        sys.exit(1)
    diarize(args[0])


if __name__ == '__main__':
    main(sys.argv[1:])
