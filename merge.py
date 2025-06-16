import subprocess, os, tempfile

def merge(infolder, outfolder):
    
    if not infolder or not outfolder:
        return False, "Invalid video folder(s)"
    

    # Get files in folder
    allfilelist = os.listdir(infolder)
    filelist = []

    for file in allfilelist:
        if(os.path.isfile(os.path.join(infolder, file))):
            filelist.append(file)

    print(filelist)

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
    command = f"ffmpeg -f concat -safe 0 -i {list_file_path} -c copy -y {outfolder}"

    try:
        process = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')

        print("DEBUG: FFmpeg stdout:\n", process.stdout)
        print("DEBUG: FFmpeg stderr:\n", process.stderr)

        if 'list_file_path' in locals() and os.path.exists(list_file_path):
            os.remove(list_file_path)
            print(f"DEBUG: Cleaned up temporary list file: {list_file_path}")

        return True, f"Successfully concatenated videos to: {outfolder}"
    
    except Exception as e:
        return False, f"An error occurred running the ffmpeg command: {e}"