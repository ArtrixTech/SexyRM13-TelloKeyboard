import cv2
import numpy as np

cap = cv2.VideoCapture(0)


class Color:
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b


def BGRtoRGB(color):
    return Color(color[2],color[1],color[0])

def RGBtoBGR(color):
    assert isinstance(color,Color)
    return [color.b,color.g,color.r]



while (1):
    # get a frame
    ret, frame = cap.read()
    # show a frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    height, width = frame.shape[0], frame.shape[1]


    # Cut the small middle area of full frame
    class CutArea:
        pass


    CutArea.width = 300
    CutArea.height = 240

    CutArea.verticalStart = int(0.5 * height - 0.5 * CutArea.height)
    CutArea.horizontalStart = int(0.5 * width - 0.5 * CutArea.width)

    cFrame = frame[CutArea.verticalStart:CutArea.verticalStart + CutArea.height,
             CutArea.horizontalStart:CutArea.horizontalStart + CutArea.width]

    tgtColor = Color(0, 50, 220)

    outputFrame = cFrame

    for y in range(CutArea.height):

        for x in range(CutArea.width):

            pix=BGRtoRGB(cFrame[y, x])

            threshold = 40
            if abs(pix.r - tgtColor.r) < threshold and abs(pix.g - tgtColor.g) < threshold and abs(
                    pix.b - tgtColor.b) < threshold:
                outputFrame[y, x] = RGBtoBGR(Color(255,255,255))
            else:
                outputFrame[y, x] = [0, 0, 0]

    # End cut

    cv2.imshow("captureFull", frame)
    cv2.imshow("capture", outputFrame)
cap.release()
cv2.destroyAllWindows()
