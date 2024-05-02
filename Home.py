import cv2 as cv
from Save_Data import Save_Person_Info
from Face_Recognition import Face_Recog
import os
import schedule



# Save Image clicking with s.
# Initialize webcam
cap = cv.VideoCapture(0)
face_cap = cv.CascadeClassifier('Data_For_Detection\haarcascade_frontalface_default.xml')
Save_Info = Save_Person_Info()
Face_r = Face_Recog()

# Identify Person.....
video_capture = cv.VideoCapture(0)

# Initialize some variables
process_this_frame = True
Face_Recognition = Face_Recog()


def Attend_False():
    for i in range(len(os.listdir('data'))):
        Save_Info.Attendence_False(i+1)

    print("This function runs every 60 sec.")
# Schedule the function to run every 24 hours
schedule.every(150).seconds.do(Attend_False)

def Attend_True(pid):
    Save_Info.Attendence_True(pid)


def Face_Attend():
    while True:
        schedule.run_pending()
        # Grab a single frame of video
        ret, frame = video_capture.read()
        frame_copy = frame.copy()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # loading data
        known_face_encodings, known_face_names = Face_Recognition.load_data()
        Is_person = Face_Recognition.Face_detection_with_name(frame,known_face_encodings, known_face_names, process_this_frame)

        # Display the resulting image
        cv.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        # Check for key press
        key = cv.waitKey(1) & 0xFF

        # # Save person's data on 's' key press
        if key == ord('s'):
            if  Is_person:
                Save_Info.save_image(frame_copy)
            else:
                print('Person is already exists')

    # Release handle to the webcam
    video_capture.release()
    cv.destroyAllWindows()



Face_Attend()
# Attend_False()
# Attend_True(2)
# Save_Info.save_Bio(2, 'Monu', 'ok@gmail.com', 678856888578, 21)





