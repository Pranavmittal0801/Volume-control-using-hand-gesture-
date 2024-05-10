#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import pyautogui


# In[2]:


x1 = y1 = x2 = y2 = 0

webcam=cv2.VideoCapture(0)
my_hands=mp.solutions.hands.Hands() #object to capture our hands
drawing_utils =mp.solutions.drawing_utils # object to draw points on our hands 


# In[3]:


while True:
    _,image=webcam.read() 
    image=cv2.flip(image,1) #this line flip the image and here 1 arguement is passed that is used to flip the image horizontally
    frame_height,frame_width,_ =image.shape
    rgb_image =cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output=my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)
            landmarks =hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=image,center=(x,y),radius=4,color=(0,255,255),thickness=3)
                    x1=x
                    y1=y
                if id == 4:
                    cv2.circle(img=image,center=(x,y),radius=4,color=(0,0,255),thickness=3)
                    x2=x
                    y2=y
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//6
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5) 
        if dist > 10:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")
    cv2.imshow("volume control using hand gesture",image)       
    key=cv2.waitKey(10) 
    if key==27:
        break


# In[4]:


webcam.release()
cv2.destroyAllWindows()


# In[5]:


print(cv2.__version__)


# In[6]:


print(mp.__version__)


# In[7]:


print(pyautogui.__version__)


# In[ ]:




