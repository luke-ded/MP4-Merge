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


    return True, "Success"