from transformers import AutoModel, AutoTokenizer

# Charger le tokenizer et le modèle BioMistral
tokenizer = AutoTokenizer.from_pretrained("BioMistral/BioMistral-7B")
model = AutoModel.from_pretrained("BioMistral/BioMistral-7B")

print("BioMistral chargé avec succès !")
