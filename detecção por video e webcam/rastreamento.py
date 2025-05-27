import cv2

# Criar rastreador (exemplo com CSRT)
rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture("race.mp4")
ok, frame = video.read()

# Seleciona a região de interesse (ROI)
bbox = cv2.selectROI(frame, False)

# Inicializa o rastreador
ok = rastreador.init(frame, bbox)

# Se inicializou corretamente, desenha o retângulo
if ok:
    (x, y, w, h) = [int(v) for v in bbox]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
else:
    cv2.putText(frame, 'Erro', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Loop de rastreamento
while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = rastreador.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'Erro no rastreamento', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Rastreamento", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

video.release()
cv2.destroyAllWindows()
