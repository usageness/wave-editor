import os
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from spleeter.separator import Separator
from pydub import AudioSegment

def remove_noise_with_spleeter_and_plot(input_audio_path, output_audio_path, selected_track='vocals'):
    separator = Separator('spleeter:2stems')
    
    separator.separate_to_file(f'{input_audio_path}.wav', output_audio_path)

    selected_track_path = os.path.join(output_audio_path, input_audio_path, f'{selected_track}.wav')

    audio = AudioSegment.from_wav(selected_track_path)
    os.makedirs(output_audio_path, exist_ok=True) 
    audio.export(os.path.join(output_audio_path, f'{selected_track}.wav'), format="wav")
    
    # librosa를 사용하여 스펙트로그램 생성 (작업 전)
    y_before, sr_before = librosa.load(f'{input_audio_path}.wav')
    D_before = librosa.amplitude_to_db(librosa.stft(y_before), ref=np.max)

    # librosa를 사용하여 스펙트로그램 생성 (작업 후)
    y_after, sr_after = librosa.load(selected_track_path)
    D_after = librosa.amplitude_to_db(librosa.stft(y_after), ref=np.max)

    # 시각화
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    librosa.display.specshow(D_before, sr=sr_before, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram Before')

    plt.subplot(2, 2, 2)
    librosa.display.specshow(D_after, sr=sr_after, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram After')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    while True:
        print('노이즈 제거 소프트웨어입니다.')
        print('잡음을 제거할 파일 이름을 입력해주세요. (.wav 확장자 생략)')
        input_audio_path = input("파일명 : ")

        output_audio_path = "output"
        remove_noise_with_spleeter_and_plot(input_audio_path, output_audio_path)