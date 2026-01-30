import cv2
import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("!! No file dropped.")
        return

    video_path = sys.argv[1]
    base_name, extension = os.path.splitext(video_path)
    output_path = f"{base_name}_cropped.mp4"

    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    cap.release()
    
    if not success:
        print("!! Could not read the video file.")
        return

    # Draw the rectangle, then press ENTER
    roi = cv2.selectROI("Select Crop Area (ENTER to Confirm)", frame)
    cv2.destroyAllWindows()
    
    x, y, w, h = [int(v) for v in roi]
    if w == 0 or h == 0:
        print("!! Selection cancelled.")
        return

    # THE FIX: All arguments must be strings
    cmd = [
        'ffmpeg', '-i', str(video_path),
        '-vf', f'crop={w}:{h}:{x}:{y}', # f-strings handle the int-to-str conversion
        '-c:v', 'libx264', '-crf', '23',
        '-preset', 'slow',
        '-c:a', 'copy', 
        str(output_path), '-y'
    ]

    print(f"--- Encoding: {os.path.basename(output_path)} ---")
    subprocess.run(cmd, check=True) # check=True will catch FFmpeg errors too

if __name__ == "__main__":
    main()