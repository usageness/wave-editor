import os
from spleeter.separator import Separator
from pydub import AudioSegment

def remove_noise_with_spleeter(input_audio_path, output_audio_path, selected_track='vocals'):
    separator = Separator('spleeter:2stems')
    
    separator.separate_to_file(input_audio_path, output_audio_path)

    selected_track_path = os.path.join(output_audio_path, f'{selected_track}.wav')
    audio = AudioSegment.from_wav(selected_track_path)

    os.makedirs(output_audio_path, exist_ok=True) 
    audio.export(os.path.join(output_audio_path, "clean_audio_spleeter.wav"), format="wav")

if __name__ == "__main__":
  
    while True:
        print('노이즈 제거 소프트웨어입니다.')
        print('잡음을 제거할 파일 이름을 입력해주세요. (.wav 까지 입력)')
        input_audio_path = input("파일명 : ")

        output_audio_path = "output"
        remove_noise_with_spleeter(input_audio_path, output_audio_path)