import os
import subprocess
from pathlib import Path
from datetime import date

# USER SETTINGS
PROJECT_ROOT = r"D:\Document folder\Projects\Research_Nigeria\Kainji Lake\ManuKainji to Professor\General format\ManuKainjiPhd\2025Papz\2_DLSegF\Submission_3_\Submission\Scripts"
REPO_NAME = "UResNetMNDWI_Ensemble_FloodMapping"

# README CONTENT
README_TEXT = f"""# {REPO_NAME}

Code repository for my manuscript submission titled:

**Assessment of Deep Learning and Monte Carlo-based MNDWI Ensemble for Enhanced Rapid and Spatial Probabilistic Water Extent Mapping under Dynamic Flow Conditions**

Submitted to *ISPRS Journal of Photogrammetry and Remote Sensing*.

## Summary

Accurate surface water mapping in river–reservoir systems remains challenging due to mixed pixels, turbidity, cloud contamination, and variable water spectral behavior under rapidly varying inflows. Spectral index approaches often fail in transition zones due to manual thresholding problems, while deep learning models also struggle to generalize under dynamic hydrologic conditions.

This repository implements a probabilistic ensemble framework that integrates deep learning segmentation with Monte Carlo–baed MNDWI pertubations to improve delineation under complex flow regimes. The framework was developed and tested over the Kainji Reservoir and flood events along the transboundary Niger River system.

## Instruction

- Run code accordingly with adequate input data 

## Repository Structure
Scripts/
├── *.py # Executable workflows
├── requirements.txt # Preserved dependency list
├── Figs/ # Figures for analysis and manuscript
├── GIS Files/ # Raster and vector datasets

## Environment

All dependencies are listed in `requirements.txt`.  
Deep learning inference relies on the ArcGIS Pro Python environment and ArcPy.

## Notes

- Large raster datasets are not included and must be supplied locally.
- File paths in scripts may require adjustment depending on the local setup.
- The repository is intended for research reproducibility and peer review.

## Citation

Please cite the associated ISPRS Journal of Photogrammetry and Remote Sensing submission when using this code.

Repository initialized on {date.today().isoformat()}.
"""

# HELPER FUNCTION
def run_cmd(cmd, cwd):
    subprocess.run(cmd, cwd=cwd, shell=True, check=True)

# MAIN
def main():
    root = Path(PROJECT_ROOT)

    if not root.exists():
        raise FileNotFoundError(f"Project directory not found: {root}")

    os.chdir(root)

    # Initialize git only if not already present
    if not (root / ".git").exists():
        print("Initializing Git repository...")
        run_cmd("git init", root)
    else:
        print("Git repository already exists. Skipping init.")

    # Write README.md only
    readme_path = root / "README.md"
    print("Writing README.md...")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(README_TEXT)

    # Stage all files (requirements.txt is preserved)
    print("Staging files...")
    run_cmd("git add .", root)

    # Commit
    print("Creating initial commit...")
    run_cmd(
        'git commit -m "Initial commit: UResNet–MNDWI ensemble flood mapping framework"',
        root
    )

    print("\nRepository ready for GitHub.")
    print("Next steps:")
    print("  git remote add origin https://github.com/USERNAME/REPOSITORY.git")
    print("  git branch -M main")
    print("  git push -u origin main")

if __name__ == "__main__":
    main()