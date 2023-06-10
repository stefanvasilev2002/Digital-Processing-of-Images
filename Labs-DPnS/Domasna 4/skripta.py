import cv2
import os

if __name__ == '__main__':
    query_image = cv2.imread('query.jpg', 0)  # Читање на query сликата во сиво

    # Листа за чување на резултатите
    results = []

    # Лоадирање на сликите од директориумот database
    for filename in os.listdir('Leaves/'):
        image_path = os.path.join('Leaves/', filename)
        image = cv2.imread(image_path, 0)  # Читање на сликата во сиво

        # Пресметување на сличноста помеѓу query сликата и моменталната слика
        similarity = cv2.matchShapes(query_image, image, 1, 0)

        # Додавање на резултатот во листата
        results.append((image_path, similarity))

    # Сортирање на резултатите според сличноста
    results.sort(key=lambda x: x[1])

    # Печатење на резултатите
    for result in results:
        print('Image:', result[0])
        print('Similarity:', result[1])
        print('---')
