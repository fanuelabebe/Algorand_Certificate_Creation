import cv2
import os
img = cv2.imread('/home/fanuel-data/Projects/Week5/AlgorandCertificate/Algorand_Certificate_Creation/ImageGeneration/asset/openai_image_test_1.PNG',1)
# img = cv2.resize(img, (0,0),fx = 0.5, fy = 0.5)

# cv2.putText(img,"Fanuel Abebe",(160,129),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)




def put_text_on_image(img,name,company,date,message,message2):
    cv2.putText(img,date,(610,239),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
    cv2.putText(img,company,(310,300),cv2.FONT_HERSHEY_SIMPLEX,2,(153,0,0),2)
    cv2.putText(img,name,(306,340),cv2.FONT_HERSHEY_PLAIN,2,(0,0,51),3)
    cv2.putText(img,message,(306,400),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,51),2)
    cv2.putText(img,message2,(306,420),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,51),2)


    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

message1 = "This certificate is given to Trainee to indicate"
message2 = "that they finished their challenge successfully"
put_text_on_image(img,"Fanuel Abebe","10 Academy","January 10, 2024",message1,message2)