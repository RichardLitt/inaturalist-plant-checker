import pandas as pd

# Define the array of names to match
name_array = [
  'Cordyline australis',
  'Rhopalostylis sapida',
  'Vitex lucens',
  'Schefflera digitata',
  'Pseudopanax arboreus',
  'Piper excelsum',
  'Metrosideros robusta',
  'Metrosideros umbellata',
  'Metrosideros excelsa',
  'Pterophylla racemosa',
  'Laurelia novae-zelandiae',
  'Aristotelia serrata',
  'Hedycarya arborea',
  'Didymocheton spectabilis',
  'Pennantia corymbosa',
  'Hoheria populnea',
  'Pseudopanax crassifolius',
  'Knightia excelsa',
  'Melicytus ramiflorus',
  'Myoporum laetum',
  'Elaeocarpus dentatus',
  'Alectryon excelsus',
  'Phyllocladus trichomanoides',
  'Nothofagus truncata',
  'Nothofagus fusca',
  'Nothofagus menziesii',
  'Carpodetus serratus',
  'Sophora microphylla',
  'Prumnopitys taxifolia',
  'Pectinopitys ferruginea',
  'Dacrycarpus dacrydioides',
  'Dacrydium cupressinum',
  'Nothofagus solandri',
  'Nothofagus cliffortioides',
  'Kunzea ericoides',
  'Leptospermum scoparium',
  'Podocarpus totara',
  'Myrsine australis',
  'Pittosporum tenuifolium',
  'Griselinia littoralis',
  'Corynocarpus laevigatus',
  'Brachyglottis repanda',
  'Beilschmiedia tarairi',
  'Agathis australis',
  'Pittosporum crassifolium',
  'Fuchsia excorticata',
  'Beilschmiedia tawa',
  'Dodonaea viscosa',
  'Pittosporum eugenioides'
]

# Define the file path to the CSV file
file_path = "observations-518492.csv"  # Replace with your CSV file path

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Ensure the column exists in the CSV file
if "scientific_name" not in data.columns:
    print("Error: Column 'scientific name' not found in the CSV file.")
else:
    # Optionally, display counts for each name
    individual_counts = data["scientific_name"].value_counts()
    for name in name_array:
        #print(f"{name}: {individual_counts.get(name, 0)}")

        if individual_counts.get(name) == None:
          print(f"{name}: {individual_counts.get(name)}")


