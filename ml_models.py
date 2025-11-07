import torch
import torch.nn.functional as F
import pickle
import numpy as np
from torch_geometric.nn import SAGEConv

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# === Modelo GraphSAGE (Académico) ===
class GraphSAGE(torch.nn.Module):
    def __init__(self, in_channels, out_channels, hidden_channels=8):
        super(GraphSAGE, self).__init__()
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        self.conv2 = SAGEConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)


# Cargar modelo académico
model_graphsage = GraphSAGE(in_channels=11, out_channels=3)
model_state = torch.load('ML-Academic/model_academic.pth', map_location=device)
model_graphsage.load_state_dict(model_state['model_state_dict'])
model_graphsage.to(device)
model_graphsage.eval()

with open('ML-Academic/label_encoder_academic.pkl', 'rb') as f:
    career_map = pickle.load(f)
career_names = {v: k for k, v in career_map.items()}


# === Modelo MLP (Psicológico) ===
class MLP(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(MLP, self).__init__()
        self.fc1 = torch.nn.Linear(in_channels, hidden_channels)
        self.fc2 = torch.nn.Linear(hidden_channels, out_channels)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Cargar modelo psicológico
model_psychological = MLP(in_channels=6, hidden_channels=16, out_channels=3)
checkpoint = torch.load('ML-Psychological/model_psychological.pth')
model_psychological.load_state_dict(checkpoint['model_state_dict'])
model_psychological.eval()

with open('ML-Psychological/label_encoder_psychological.pkl', 'rb') as f:
    le_psychological = pickle.load(f)


# === Funciones de predicción ===
def predecir_carrera_graphsage(model, notas_nuevo_estudiante):
    calificacion_map = {'AD': 4, 'A': 3, 'B': 2, 'C': 1}
    notas_nuevo_estudiante = [calificacion_map.get(nota, 0) for nota in notas_nuevo_estudiante]
    notas_tensor = torch.tensor(np.array(notas_nuevo_estudiante).reshape(1, -1), dtype=torch.float).to(device)
    edge_index_empty = torch.tensor([[], []], dtype=torch.long).to(device)

    with torch.no_grad():
        out = model(notas_tensor, edge_index_empty)
        pred = out.argmax(dim=1)

    return career_names[pred.item()]


def predecir_facultad_psychological(model, datos_psicologicos):
    x_new = torch.tensor(datos_psicologicos, dtype=torch.float)
    out_new = model(x_new)
    pred_new = out_new.argmax(dim=1) if len(out_new.shape) == 2 else out_new.argmax(dim=0)
    facultades = le_psychological.classes_
    return facultades[pred_new.item()]
