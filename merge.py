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


    return True, "Success"