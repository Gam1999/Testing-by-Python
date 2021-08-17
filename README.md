# Testing-by-Python
------------ คำอธิบายสำหรับรัน Test ------------
ไฟลTestทั้งหมดมี 3 ไฟล์ ดังนี้

1.ไฟล์ Test_matrix.py: ไฟล์นี้จะTest โค้ดในไฟล์ matrix.py
	วิธีการ Test ไฟล์ Test_matrix.py
		python -m unittest test_matrix.py 
 
	วิธีการทดสอบ coverage ไฟล์ Test_matrix.py
		coverage run -m unittest test_matrix
		coverage report -m

2.ไฟล์ Test_shape.py: ไฟล์นี้จะTest โค้ดในไฟล์ shape.py
	วิธีการ Test ไฟล์ Test_shape.py
		python -m unittest test_shape.py  

	วิธีการทดสอบ coverage ไฟล์ Test_shape.py
		coverage run -m unittest test_shape
		coverage report -m

3.ไฟล์ Test_equation.py: ไฟล์นี้จะTest โค้ดในไฟล์ equation.py
	วิธีการ Test ไฟล์ Test_equation.py
		python -m unittest test_equation.py  

	วิธีการทดสอบ coverage ไฟล์ Test_equation.py
		coverage run -m unittest test_equation
		coverage report -m
