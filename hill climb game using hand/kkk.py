import cv2
import mediapipe as mp
import time
from directkeys import right_pressed, left_pressed, presskey, releasekey

break_key_pressed = left_pressed
accelerator_key_pressed = right_pressed

time.sleep(2.0)
current_key_pressed = set()

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipids = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        break_Pressed = False
        accelerator_pressed = False
        key_count = 0
        key_pressed = 0
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmark.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    mmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
                fingers = []
                if len(mmList) != 0:
                    if mmList[tipids[0]][1] > mmList[tipids[0] - 1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    for id in range(1, 5):
                        if mmList[tipids[id]][2] < mmList[tipids[id] - 2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    total = fingers.count(1)
                    if total == 0:
                        cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(image, "Brake", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                        presskey(break_key_pressed)
                        break_Pressed = True
                        current_key_pressed.add(break_key_pressed)
                        key_pressed = break_key_pressed
                        keyPressed = True
                        key_count = key_count + 1
                    elif total == 5:
                        cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(image, "gas", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                        presskey(accelerator_key_pressed)
                        key_pressed = accelerator_key_pressed
                        accelerator_pressed = True
                        keyPressed = True
                        current_key_pressed.add(accelerator_key_pressed)
                        key_count = key_count + 1

        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                releasekey(key)
            current_key_pressed = set()
        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key_pressed != key:
                    releasekey(key)
            current_key_pressed = set()

        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
# import cv2
# import mediapipe as mp
# import time
# from directkeys import right_pressed, left_pressed, presskey, releasekey

# break_key_pressed = left_pressed
# accelerator_key_pressed = right_pressed

# time.sleep(2.0)
# current_key_pressed = set()

# mp_draw = mp.solutions.drawing_utils
# mp_hand = mp.solutions.hands

# tip_ids = [4, 8, 12, 16, 20]

# video = cv2.VideoCapture(0)

# with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
#     while True:
#         keyPressed = False
#         break_pressed = False
#         accelerator_pressed = False
#         key_count = 0
#         key_pressed = 0
        
#         ret, image = video.read()
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
#         results = hands.process(image)
        
#         mmList = []
        
#         if results.multi_hand_landmarks:
#             for hand_landmark in results.multi_hand_landmarks:
#                 for idx, lm in enumerate(hand_landmark.landmark):
#                     h, w, c = image.shape
#                     cx, cy = int(lm.x * w), int(lm.y * h)
#                     mmList.append([idx, cx, cy])
                
#                 mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
                
#                 fingers = []
                
#                 if len(mmList) != 0:
#                     if mmList[tip_ids[0]][1] > mmList[tip_ids[0] - 1][1]:
#                         fingers.append(1)
#                     else:
#                         fingers.append(0)

#                     for idx in range(1, 5):
#                         if mmList[tip_ids[idx]][2] < mmList[tip_ids[idx] - 2][2]:
#                             fingers.append(1)
#                         else:
#                             fingers.append(0)
                            
#                     total = fingers.count(1)
                    
#                     if total == 0:
#                         cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
#                         cv2.putText(image, "Brake", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
#                         presskey(break_key_pressed)
#                         break_pressed = True
#                         current_key_pressed.add(break_key_pressed)
#                         key_pressed = break_key_pressed
#                         keyPressed = True
#                         key_count = key_count + 1
#                     elif total == 5:
#                         cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
#                         cv2.putText(image, "Gas", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
#                         presskey(accelerator_key_pressed)
#                         key_pressed = accelerator_key_pressed
#                         accelerator_pressed = True
#                         keyPressed = True
#                         current_key_pressed.add(accelerator_key_pressed)
#                         key_count = key_count + 1

#         if not keyPressed and len(current_key_pressed) != 0:
#             for key in current_key_pressed:
#                 releasekey(key)
#             current_key_pressed = set()
#         elif key_count == 1 and len(current_key_pressed) == 2:
#             for key in current_key_pressed:
#                 if key_pressed != key:
#                     releasekey(key)
#             current_key_pressed = set()

#         cv2.imshow("Frame", image)
#         k = cv2.waitKey(1)
#         if k == ord('q'):
#             break

# video.release()
# cv2.destroyAllWindows()
