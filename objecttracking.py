import cv2 
import time
import time

p1=530
p2=300
xs=[]
ys=[]
video=cv2.VideoCapture("bb3.mp4")

#load tracker
tracker=cv2.TrackerCSRT_create()

#read the first frame of the video
returned,img=video.read()

#select the bounding box on the image 
bbox=cv2.selectROI("tracking",img,False)

#initialise the tracker the img and bounding the box
tracker.init(img,bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    #getting the center of the box
    c1=x+int(w/2)
    c2=y+int(h/2)
    #drawing a small circle 
    cv2.circle(img,(int(p1),int(p2)),2,(0,255,0),3)
    cv2.circle=(img,(c1,c2),2,(0,0,225),5)

    #calculating distance
    dist = math.sqrt(((c1-p1)**2)+(c2-p2)**2)
    print(dist)


   #goal is reached if the dist the is less than 20
   if(dist<=20):
    cv2.putText(img,"goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i],2,(0,0,255),5)

        while True:
            check,img=video.read()

            #updating the tracker
            success,bbox=tracker.update(img)
             #draw box
             if success:
                drawbox(img,bbox)
             else:
                cv2.putText(img,"LOst",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

                goal_track(img,bbox)
                cv2.imshow("result",img)
                key=.waitKey(25)
                if key==32:
                print("stopped")
                break
            video.release()
            cv2.destroyALLwindows()


