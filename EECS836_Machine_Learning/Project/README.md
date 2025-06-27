# EECS836 Machine Learning Project: Surface Detection in Echograms

This repository contains the complete code and data pipeline for the Spring 2025 EECS836 course project at the University of Kansas. The project focuses on detecting the **air–snow boundary** in radar echograms using a combination of weakly supervised learning and fine-tuned CNN models.

## Overview

Radar echograms collected by CReSIS provide vertical profiles of snow and ice layers in polar regions. Manually identifying surface boundaries is tedious and does not scale across large datasets.

This project leverages:
- Weakly labeled data (via edge detection)
- Manual boundary clicks on a small subset
- A U-Net-based segmentation model
- BCE + Dice loss for improved mask quality

## Folder Structure

```
Project/
├── data/
│   ├── raw/                # Original cropped + resized echograms (from CReSIS)
│   ├── processed/          # Preprocessed .npy files for training
│   ├── labels_manual/      # Hand-clicked labels for air-snow surface
│   ├── labels_weak/        # Auto-generated weak labels using Sobel + Canny
│   └── heldout_eval/       # Held-out test images (not used in training)
│
├── results/
│   ├── overlays/           # Epoch-wise overlay predictions
│   ├── heldout_eval/       # Model outputs on held-out data
│   └── model_final.pth     # Final trained model parameters
│
├── src/
│   ├── preprocess.py
│   ├── download_data.py
│   ├── manual_label_surface.py
│   ├── generate_weak_labels.py
│   ├── visualize_echograms.py
│   ├── train.py
│   ├── eval_metrics.py
│   └── evaluate_heldout.py
│
└── report/
    └── final_report.tex    # Final LaTeX writeup
    └── figs/               # Summary plots and visuals for report
```

## Getting Started

Run the following steps from the repo's root:

1. **Download Data**
```bash
python src/download_data.py
```

2. **Preprocess Images**
```bash
python src/preprocess.py
```

3. **Manual Labeling (Optional UI)**
```bash
python src/manual_label_surface.py
```

4. **Generate Weak Labels**
```bash
python src/generate_weak_labels.py
```

5. **Train the Model**
```bash
python src/train.py
```

6. **Evaluate and Plot Metrics**
```bash
python src/eval_metrics.py
python src/evaluate_heldout.py
```

## Key Results

- Achieved **mean IoU: 0.979** and **mean F1 Score: 0.989** on the manually labeled validation set.
- Model generalized well to unseen echograms, including noisy and stratigraphically complex inputs.
- BCE + Dice loss improved interior segmentation and reduced “hollow” prediction effects seen in earlier training epochs.

## Dataset Source

Data is publicly available from:  
**[CReSIS Snow Radar Dataset](https://data.cresis.ku.edu/data/snow/)**

We specifically used 2022 Greenland P3 radar echograms from:  
`https://data.cresis.ku.edu/data/snow/2022_Greenland_P3/images/`

## Report

The final project report (written in LaTeX) is available at:  `report/final_report.tex`

## Future Work

- Use `.mat` files for 3D reconstructions and geospatial surface tracking.
- Add temporal context (adjacent frames) for smoother predictions.
- Integrate post-processing like morphological operations or CRFs.
- Deploy the trained model across other CReSIS campaigns in Antarctica and beyond.
- Use active learning to prioritize which echograms need manual labeling.

## Contact

Developed by: **Mohammad Ful Hossain Seikh**  
KU EECS and Physics & Astronomy Graduate Student [Project GitHub Repository](https://github.com/Mohammad-Neutrino/EECS836_Machine_Learning/tree/trunk/Project)

