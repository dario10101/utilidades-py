from pydub import AudioSegment

track_0 = './audio/intro1.mp3'
track_1 = './audio/YoSoyBabalu.mp3'
track_2 = './audio/ElCumbanchero.mp3'
output_name = './audio/coreo2.mp3'

def run():
    
    # Cargar dos archivos de audio
    audio0 = AudioSegment.from_file(track_0)
    audio1 = AudioSegment.from_file(track_1)
    audio2 = AudioSegment.from_file(track_2)

    # Recortar: del segundo 10 al 20 (tiempo en milisegundos)
    audio0_clipp = audio0[9_500:]
    audio1_clipp = audio1[0:140_890]
    audio1_1_clipp = audio0[14_000:]
    audio2_clipp = audio2[0:113_250]

    # Obtener duración total
    #duration = len(audio1_clipp)  # en milisegundos

    # Separar la parte final (2 segundos)
    final1 = audio1_clipp[-2000:]

    # Aplicar fade out al final
    final_with_fade1 = final1.fade_out(2000)

    # Combinar parte sin cambios + parte con fade
    audio1_clipp = audio1_clipp[:-2000] + final_with_fade1

    # Subir el volumen en +3 decibelios (dB)
    audio2_clipp = audio2_clipp.apply_gain(+3)

    # Unir el recorte con el segundo audio
    final_audio = audio0_clipp + audio1_clipp + audio1_1_clipp + audio2_clipp

    # Guardar el resultado
    final_audio.export(output_name, format="mp3")



if __name__ == '__main__':
    run()
