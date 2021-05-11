import numpy as np
import cv2

i = np.arange(28*28).reshape(28, 28)
k = i.tobytes()
y = np.frombuffer(k, dtype=i.dtype)
print(type(i.dtype),type(k),type(y))