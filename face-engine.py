import numpy as np
import cv2
import insightface
from insightface.app import FaceAnalysis

class FaceEngine:
    def __init__(self):
        self.app = FaceAnalysis(name='buffalo_l')
        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def get_embedding(self, image_path):
        img = cv2.imread(image_path)
        faces = self.app.get(img)
        if len(faces) == 0:
            return None
        return faces[0].embedding

    def compare_embeddings(self, emb1, emb2, threshold=0.6):
        dot = np.dot(emb1, emb2)
        norm1 = np.linalg.norm(emb1)
        norm2 = np.linalg.norm(emb2)
        sim = dot / (norm1 * norm2)
        return float(sim), sim >= threshold