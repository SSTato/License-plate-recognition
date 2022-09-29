from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=False, lang="ch", use_gpu=False)  # need to run only once to download and load model into memory
img_path = r'C:\Users\Administrator\Desktop\yolov5-6.1\OCR\444.jpeg'
result = ocr.ocr(img_path, cls=False)
for line in result:
    print(line)
text_ = [line[1][0] for line in result]
text_box_position = [line[0] for line in result]
confidence = [line[1][1] for line in result]

text = {}
text['text'] = text_[0]
text['text_box_position'] = text_box_position
text['confidence'] = confidence
