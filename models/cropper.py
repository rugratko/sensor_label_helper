import numpy as np
import cv2
import os

def do_crop(LABEL_CLASS, PATH, CLASS_DIR, FIRST, LAST):
    
	os.chdir(PATH)
	counter = FIRST
	while (counter <= LAST):

		#cap = cv2.VideoCapture('/home/mvz/mark_home/Look/VideoFiles/kvadro.avi')
		full_name_video_file = CLASS_DIR + '\\{}_{}\\{}_{}.avi'.format(LABEL_CLASS, counter, LABEL_CLASS, counter)
		print(full_name_video_file)
		
		# cap = cv2.VideoCapture("D:/1Sensor_video/Comp/comp_01.avi") 
		cap = cv2.VideoCapture(full_name_video_file)

		list1 = full_name_video_file.split("\\")
		#print('full video name = ', list1)

		video_file_name = list1[-1]
		print('Video file name = ', video_file_name)

		folder_video_file = video_file_name[:-4]
		print('Folder video file = ', folder_video_file)

		folder_category = list1[-3]
		print('Folder category = ', folder_category)

		#"D:/Look/VideoFiles/slow_traffic_small.mp4"  revaz_red.avi  VID_20170803_200125.3gp  
		# cap = cv2.VideoCapture(1)

		fourcc = cv2.VideoWriter_fourcc(*'XVID')
				#out = cv2.VideoWriter('output.avi', fourcc, 2.0,
				#                  (img_shape[1], img_shape[0]))
		ret, gray = cap.read()   #frame
		img_shape = gray.shape

		out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  #  img_shape[1], img_shape[0] 640,360  640 480
		img_shape = gray.shape

		cur_num_frame = 0

		while (True):
			# Capture frame-by-frame
			ret, gray = cap.read()   #frame

			if ret:
				# Our operations on the frame come here
				#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				img_shape = gray.shape
				gray = cv2.resize(gray, (640,480),  interpolation = cv2.INTER_AREA ) 

				## out.write(gray) 
				'''
				fourcc = cv2.VideoWriter_fourcc(*'XVID')
				#out = cv2.VideoWriter('output.avi', fourcc, 2.0,
				#                  (img_shape[1], img_shape[0]))

				out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,360))
				''' 
				blurthreshold = 20.0
				blur = cv2.Laplacian(gray, cv2.CV_64F).var()
				
				cur_num_frame +=  1
				cur_file_name = folder_category + "\\" + folder_video_file + "\\" + folder_video_file + "_" + str(cur_num_frame) +"_"+ str(int(blur)) + ".jpg"
				#print(cur_file_name)
				## print("Blur = ", blur) 
				if (cur_num_frame % 10 == 5) or (cur_num_frame % 10 == 0):
					if(blur > blurthreshold):
						cv2.imwrite(cur_file_name, gray)
				
				#out.write(gray) 
				# Display the resulting frame
				cv2.imshow(' Show video ', gray)   
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			else:
				break

		print ('Создание изображений завершено')
		cap.release()
		out.release()
		cv2.destroyAllWindows()

		counter += 1




