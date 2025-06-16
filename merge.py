import subprocess, os, tempfile

def merge(infolder, outfolder):
    
    if not infolder or not outfolder:
        return False, "Invalid video folder(s)"
    

    # Get files in folder
    allfilelist = os.listdir(infolder)
    filelist = []

    for file in allfilelist:
        if(os.path.isfile(os.path.join(infolder, file)) and file.lower().endswith(".mp4")):
            filelist.append(os.path.join(infolder, file))


    # Create temporary text file for ffmpeg
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix='.txt') as f:
            list_file_path = f.name

            for path in filelist:
                f.write(f"file '{path}'\n")

    except:
        print("Error occured creating tempfile.")
        return False, "Error occured creating tempfile."
    

    # Run ffmpeg command
    try:
        command_list = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', list_file_path,
            '-c', 'copy',
            '-y', # Overwrite output file without asking
            os.path.join(outfolder, "output.mp4")
        ]

        process = subprocess.run(command_list, capture_output=True, text=True, check=True, encoding='utf-8')

        if 'list_file_path' in locals() and os.path.exists(list_file_path):
            os.remove(list_file_path)
            #print(f"DEBUG: Cleaned up temporary list file: {list_file_path}")

        return True, f"Successfully concatenated videos to: {outfolder}"
    
    except Exception as e:
        return False, f"An error occurred running the ffmpeg command: {e}"