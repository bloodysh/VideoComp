import os
import subprocess
def compress_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mov') or filename.endswith('.mp4'):

            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_directory, f'compressed_{filename}')

            #pour vérifier les chemins:
            print(input_path)
            print(output_path)

            ffmpeg_cmd = f'ffmpeg -i {input_path} -c:v libx264 -c:a copy -crf 20 {output_path}'
            subprocess.run(ffmpeg_cmd, shell=True)

#chemin du dossier des vidéos

folder_path = 'file_path'      #<--- à remplacer ici

#emplacement de sortie de vidéos compréssées

output_directory = 'file_path'    #<--- à remplacer ici

#appel fonction pour compresser
compress_videos(folder_path)
