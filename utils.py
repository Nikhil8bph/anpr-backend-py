
def get_car(plate_detection,vehicle_detections_):
    plate_x1, plate_y1, plate_x2 ,plate_y2 ,plate_score ,plate_class_id = plate_detection
    for vehicle_detection in vehicle_detections_.boxes.data.tolist():
        vehicle_x1, vehicle_y1, vehicle_x2, vehicle_y2, vehicle_track_id, vehicle_score, vechile_class_id = vehicle_detection
        if plate_x1 > vehicle_x1 and plate_y1 > vehicle_y1 and plate_x2 < vehicle_x2 and plate_y2 < vehicle_y2:
            return vehicle_detection 
    return -1, -1, -1, -1, -1, -1, -1

def read_plate(reader, license_plate_crop):
    detections = reader.readtext(license_plate_crop)
    for detection in detections:
        bbox, text, score = detection
        text = text.upper().replace(' ', '')
        return text, score
    return "text_not_clear",-1