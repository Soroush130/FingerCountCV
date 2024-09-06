import cv2
import mediapipe as mp

from utility import calculate_bisector

mediapipHands = mp.solutions.hands
hands = mediapipHands.Hands()
Draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    result = hands.process(frame_rgb)
    
    if result.multi_hand_landmarks:
        Counter = 0
        
        for handlandmarks in result.multi_hand_landmarks:
            h, w, _ = frame.shape
            
            # List to store whether each finger is open or closed
            finger_status = []
            
            # Thumb (compare tip [4] and joint [2])
            thumb_tip = handlandmarks.landmark[4]
            thumb_mcp = handlandmarks.landmark[2]
            if thumb_tip.x < thumb_mcp.x:
                finger_status.append("Thumb Closed")
            else:
                Counter += 1
                finger_status.append("Thumb Open")
            
            
            # Index Finger (compare tip [8] and PIP joint [6])
            index_tip = handlandmarks.landmark[8]
            index_pip = handlandmarks.landmark[6]
            if index_tip.y < index_pip.y:
                Counter += 1
                finger_status.append("Index Finger Open")
            else:
                finger_status.append("Index Finger Closed")
            
            # Middle Finger (compare tip [12] and PIP joint [10])
            middle_tip = handlandmarks.landmark[12]
            middle_pip = handlandmarks.landmark[10]
            if middle_tip.y < middle_pip.y:
                Counter += 1
                finger_status.append("Middle Finger Open")
            else:
                finger_status.append("Middle Finger Closed")
            
            # Ring Finger (compare tip [16] and PIP joint [14])
            ring_tip = handlandmarks.landmark[16]
            ring_pip = handlandmarks.landmark[14]
            if ring_tip.y < ring_pip.y:
                Counter += 1
                finger_status.append("Ring Finger Open")
            else:
                finger_status.append("Ring Finger Closed")
            
            # Pinky Finger (compare tip [20] and PIP joint [18])
            pinky_tip = handlandmarks.landmark[20]
            pinky_pip = handlandmarks.landmark[18]
            if pinky_tip.y < pinky_pip.y:
                Counter += 1
                finger_status.append("Pinky Finger Open")
            else:
                finger_status.append("Pinky Finger Closed")
                
                
                
            print(finger_status)
                
            # TODO :
            Draw.draw_landmarks(frame, handlandmarks, mediapipHands.HAND_CONNECTIONS)

                
        cv2.putText(frame, f'{Counter}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)           
            
    
    cv2.imshow("Camera", frame)
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    