import numpy as np
import wave

def generate_wave(frequency, duration, sample_rate=44100):
    """Gera uma onda senoidal com uma frequência e duração específicas."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave_data = np.sin(2 * np.pi * frequency * t)
    return wave_data

def apply_interruptions(main_wave, interrupt_wave, interrupt_duration, sample_rate=44100):
    """Aplica interrupções na onda principal com base na onda de interrupção e duração da interrupção."""
    interrupt_samples = int(sample_rate * interrupt_duration)
    num_interrupts = len(main_wave) // (2 * interrupt_samples)

    for i in range(num_interrupts):
        start = i * 2 * interrupt_samples
        end = start + interrupt_samples
        main_wave[start:end] = interrupt_wave[:interrupt_samples]

    return main_wave

def save_wave_file(filename, audio_data, sample_rate=44100):
    """Salva os dados de áudio em um arquivo WAV."""
    audio_data = (audio_data * 32767).astype(np.int16)
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def main():
    # Solicita os dados ao usuário
    main_freq = float(input("Digite a frequência principal (Hz): "))
    interrupt_freq = float(input("Digite a frequência de interrupção (Hz): "))
    interrupt_duration = float(input("Digite a duração da interrupção (segundos): "))
    total_duration = float(input("Digite a duração total da gravação (segundos): "))

    # Gera a onda principal e a onda de interrupção
    main_wave = generate_wave(main_freq, total_duration)
    interrupt_wave = generate_wave(interrupt_freq, interrupt_duration)

    # Aplica as interrupções na onda principal
    final_wave = apply_interruptions(main_wave, interrupt_wave, interrupt_duration)

    # Salva o áudio em um arquivo WAV
    output_filename = "output.wav"
    save_wave_file(output_filename, final_wave)

    print(f"Áudio salvo em {output_filename}")
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

