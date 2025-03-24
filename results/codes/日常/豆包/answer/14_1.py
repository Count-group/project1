from pydub import AudioSegment
from pydub.effects import speedup


def modify_music(input_file, output_file, volume_increase=5, pitch_factor=1.2):
    try:
        # 读取音乐文件
        audio = AudioSegment.from_file(input_file)

        # 增大音量
        audio = audio + volume_increase

        # 提高音调
        new_sample_rate = int(audio.frame_rate * pitch_factor)
        pitch_shifted_audio = audio._spawn(audio.raw_data, overrides={
            "frame_rate": new_sample_rate
        })
        pitch_shifted_audio = pitch_shifted_audio.set_frame_rate(audio.frame_rate)

        # 去掉最后 5 秒
        duration = len(pitch_shifted_audio)
        new_audio = pitch_shifted_audio[:duration - 5000]

        # 保存修改后的音乐文件
        new_audio.export(output_file, format="mp3")
        print(f"修改后的音乐文件已保存为 {output_file}")
    except FileNotFoundError:
        print("错误: 未找到输入的音乐文件!")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")


if __name__ == "__main__":
    input_file = "input.mp3"
    output_file = "output.mp3"
    modify_music(input_file, output_file)
    