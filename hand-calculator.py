import cv2
import numpy as np
import pickle
import math
from collections import Counter, deque

def euclidean_distance(a, b):
	x2, x1, y2, y1 = a[0], b[0], a[1], b[1]
	return np.sqrt((x2-x1)**2+(y2-y1)**2)

def start_calculator():
	cam = cv2.VideoCapture(1)
	numbers = deque(maxlen = 100)
	x, y, w, h = 300, 100, 300, 300
	flag_first_number, flag_operator, flag_second_number, flag_clear, flag_new_number = True, False, False, False, False
	display_text = ""
	display_info = ""
	with open("range.pickle", "rb") as f:
		t = pickle.load(f)
	lower = np.array([t[0], t[1], t[2]])					# HSV green lower
	upper = np.array([t[3], t[4], t[5]])					# HSV green upper
	x, y, w, h = 300, 100, 300, 300

	display_info = "Enter first number"
	count_clear_frames = 0
	while True:
		_, img = cam.read()
		img = cv2.flip(img, 1)
		imgCrop = img[y:y+h, x:x+w]
		imgHSV = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2HSV)
		blur = cv2.medianBlur(imgHSV, 15)
		blur = cv2.GaussianBlur(blur , (5,5), 0)
		mask = cv2.inRange(blur, lower, upper)
		thresh = cv2.threshold(mask,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
		contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]

		fingers = 0
		if len(contours) > 0:
			contour = max(contours, key = cv2.contourArea)
			cv2.drawContours(imgCrop, [contour], 0, (0, 0, 255), 2)
			M = cv2.moments(contour)
			if M['m00'] != 0:
				center = np.array([int(M['m10']/M['m00']), int(M['m01']/M['m00'])])
				cv2.circle(imgCrop, tuple(center), 4, (0, 0, 255), -1)
			hulls = cv2.convexHull(contour, returnPoints = False)
			defects = cv2.convexityDefects(contour, hulls)
			if np.any(defects != None):
				list_a, list_b, list_c, list_angleA, list_start, list_end, list_far = [], [], [], [], [], [], []
				for i in range(defects.shape[0]):
					s,e,f,d = defects[i,0]
					start = tuple(contour[s][0])
					end = tuple(contour[e][0])
					far = tuple(contour[f][0])
					list_start.append(start)
					list_end.append(end)
					list_far.append(far)

					a = euclidean_distance(start, end)
					b = euclidean_distance(start, far)
					c = euclidean_distance(end, far)
					list_a.append(a)
					list_b.append(b)
					list_c.append(c)

					angleA = math.acos((b**2+c**2-a**2)/(2*b*c))*57
					angleB = math.acos((a**2+c**2-b**2)/(2*a*c))*57
					angleC = math.acos((b**2+a**2-c**2)/(2*b*a))*57

					list_angleA.append(angleA)

					if angleA <= 90:
						fingers += 1
						cv2.circle(imgCrop, tuple(start), 3, (0,0,255), -1)
						cv2.circle(imgCrop, tuple(far), 3, (255,255,0), -1)
						cv2.line(imgCrop, tuple(center), tuple(start), (0,255,0), 3)
						cv2.line(imgCrop, tuple(center), tuple(end), (0,255,0), 3)
						flag_new_number = True

				center_y = center[1]
				end_y = list_end[list_a.index(max(list_a))][1]
				if (list_a.index(max(list_a)) == list_b.index(max(list_b)) \
						and list_b.index(max(list_b)) == list_c.index(max(list_c))) \
						and list_angleA[list_a.index(max(list_a))] > 110 \
						and center_y > end_y:
					fingers = 0
					cv2.circle(imgCrop, tuple(list_start[list_a.index(max(list_a))]), 3, (0,0,255), -1)
					cv2.circle(imgCrop, tuple(list_far[list_a.index(max(list_a))]), 3, (255,255,0), -1)
					cv2.line(imgCrop, tuple(center), tuple(list_end[list_a.index(max(list_a))]), (0,255,0), 3)
					flag_new_number = True
				elif np.all(np.array(list_angleA) > 120):
					if flag_new_number:
						flag_new_number = False
						if flag_first_number and len(numbers) > 10:
							flag_first_number = False
							first = Counter(numbers).most_common(1)[0][0]
							display_text = str(first)
							display_info = "Enter operator"
							flag_operator = True
						
						elif flag_operator and len(numbers) > 10:
							flag_operator = False
							operator = Counter(numbers).most_common(1)[0][0]
							if operator == 1:
								operator = " + "
							elif operator == 2:
								operator = " - "
							elif operator == 3:
								operator = " * "
							elif operator == 4:
								operator = " / "
							elif operator == 5:
								operator = " % "
							display_text = display_text + operator
							display_info = "Enter second number"
							flag_second_number = True
						
						elif flag_second_number and len(numbers) > 10:
							flag_second_number = False
							second = Counter(numbers).most_common(1)[0][0]
							display_text = display_text + str(second)
							display_text = display_text +" = " + str(eval(display_text))
							display_info = "Clear screen"
							flag_clear = True

						elif flag_clear:
							count_clear_frames = 0
							flag_clear = False
							display_text = ""
							display_info = "Enter first number"
							flag_first_number = True
						
					elif flag_clear and count_clear_frames > 25:
						count_clear_frames = 0
						flag_clear = False
						display_text = ""
						display_info = "Enter first number"
						flag_first_number = True

					numbers = deque(maxlen = 100)
																		
			fingers += 1
			numbers.append(fingers)

		if display_info == "Clear screen":
			count_clear_frames += 1
		cv2.putText(img, display_text, (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))
		cv2.putText(img, display_info, (30, 440), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255) )
		cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
		cv2.imshow("Calculator", img)
		cv2.imshow("thresh", thresh)
		if cv2.waitKey(1) == ord('q'):
			break

start_calculator()
