import cv2
import os

#scripts paths
videos_path = 'videos-to-generate-dataset'
output_path = 'output'

def outputFilesCleaner():
    if not os.path.exists(output_path): # create output path if not exists
        try:
            os.makedirs(output_path)
        except OSError as e:
            print(f'Error: {output_path}: {e}')
    else: #remove all contents if exists
        files = os.listdir(output_path)
        for file in files:
            file_path = os.path.join(output_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

def filesToCompile(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def saveFramesByVideo(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_seconds = frame_count / fps
    filename = os.path.splitext(video_path)[0].split('\\')[1]
    print(f'Filename: {filename} FPS: {fps} - Frames: {frame_count} - Seconds: {duration_seconds}')

    count = 0

    #read video and save frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        #define frame name to save
        frame_name = os.path.join(output_path, f'{filename}_frame_{count}.jpg')
        #save frame
        cv2.imwrite(frame_name, frame)
        count += 1

    cap.release()

def main():
    files_to_generate = filesToCompile(videos_path)
    print("File(s) found: ", len(files_to_generate))
    print('-----------------------------')
    for video_path in files_to_generate:
        print(f"Split video frames: {video_path}")
        saveFramesByVideo(video_path)
        print('-----------------------------')


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----------------------------')
    outputFilesCleaner()
    main()
    print('Done!')