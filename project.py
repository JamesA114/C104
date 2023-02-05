import cv2

img = cv2.imread("solar-system.jpg")
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

cv2.putText(
    img, 
    planets[0], (20,200),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[1], (120,200),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.5,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[2], (220,180),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.8,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[3], (300,260),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.7,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[4], (400,180),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.8,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[5], (600,100),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[6], (850,170),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.8,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[7], (1000,150),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.8,  
    color=(255,255,255)
    )
cv2.putText(
    img, 
    planets[8], (1160,150),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=.8,  
    color=(255,255,255)
    )
cv2.imshow("output",img)

cv2.waitKey(0)