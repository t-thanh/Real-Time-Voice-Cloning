from vlibs import fileio
import torch

project_root = fileio.abspath(fileio.leafdir(__file__))

librispeech_root = "E://Datasets/LibriSpeech"
librispeech_datasets = ["train-other-500"]
voxceleb1_root = "E://Datasets/VoxCeleb1"
anglophone_nationalites = ['australia', 'canada', 'ireland', 'uk', 'usa']
clean_data_root = "E://Datasets//SpeakerEncoder"

model_dir = fileio.join(project_root, "saved_models")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
