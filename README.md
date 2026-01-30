Video ROI Crop Tool
A utility for selecting a Region of Interest (ROI) and cropping video files using Python, OpenCV, and FFmpeg via a drag-and-drop batch interface.




1. Prerequisites
Miniconda or Anaconda
https://docs.anaconda.com/miniconda/





2. Environment Setup
Create a dedicated Conda environment to manage dependencies and avoid global system conflicts:

Powershell:
##############################################################################################
# Create the environment
conda create -n cropvid -c conda-forge python=3.10 opencv ffmpeg -y

# Verify the installation
conda activate cropvid
python -c "import cv2; print('OpenCV Version:', cv2.__version__)"
##############################################################################################





3. Local Configuration
You must update the paths in CropDrop.bat to match your local installation.
To find CONDA_PATH: Open PowerShell and run:

PowerShell
##################################################################################
(Get-Command conda).Source.Replace("Scripts\conda.exe", "condabin\conda.bat")
##################################################################################

To find SCRIPT_PATH: In File Explorer, navigate to the folder where you cloned this repository. Click the address bar, copy the path, and append \crop_tool.py to it.

Update these variables in CropDrop.bat:
set "CONDA_PATH=C:\YOUR_PATH_HERE\condabin\conda.bat"
set "SCRIPT_PATH=C:\YOUR_PATH_HERE\crop_tool.py"







4. Usage Instructions
Drag and Drop: Drag the target video file onto the CropDrop.bat icon.
Create links/shortcuts to the .bat file to use this function in other directories or from the desktop.

An interactive window will open displaying the first frame of the video.
Left-click and drag the mouse to draw a rectangle over the desired area.
Confirm: Press ENTER or SPACE to confirm.

Output: The script will process the video. The result is saved in the source directory with the suffix _cropped.mp4.








5. Troubleshooting
'ffmpeg' is not recognized: Ensure FFmpeg is installed. If it is installed but not in your System PATH, you can specify the absolute path to ffmpeg.exe inside the crop_tool.py script in the cmd list.

Window closes immediately: This usually indicates an incorrect path in the CONDA_PATH or SCRIPT_PATH variables. Double-check that both files exist at the specified locations.

File in use error: Ensure the video file you are trying to crop is not open in another application (e.g., VLC, Windows Media Player, or Premiere Pro) during processing.

OpenCV Window doesn't appear: Verify that the cropvid environment was created successfully and that opencv-python is installed within it.








6. FFMPEG Technical Specifications
Video Encoding: Uses libx264 with a Constant Rate Factor (CRF) of 23.
Speed Preset: Set to slow for optimized compression efficiency.
Audio Handling: Audio is passed through using -c:a copy to ensure no loss in quality or synchronization.
ROI Interface: Handled via cv2.selectROI.
