# ghost-hunter

TODO: Create way of doing inference on multiple dm4 files  

## Project Workflow: 

### Training (only need to do once)
- Retrieve dm4 files
- Turn to png using `scripts/dm4_to_png.py` 
- Label 500 images or so using `labelling/binary_search_labelling`
- setup yaml file with location of png files and select model settings
- train on labelled images using `src/run.py`
- Run inference using checkpoint using `src/inference.py` (real space segmentation will be output to `images/`)

### Inference
- Retrieve dm4 files
- Turn to png using `scripts/dm4_to_png.py` 
- setup yaml file with location of png files and select model settings
- Run inference using checkpoint using `src/inference.py` (real space segmentation will be output to `images/`)

>[!NOTE]
> All the file imports have been setup so that they are relative to the top folder. 
> So that when you reference files in the config files, always use folder paths relative to the top repo folder.

## Usage 

The config files are contained within the `configs` directory. You can control all the parameters of the model within this file. If you are running this model with your own data you will want to change the `train_dir` and `data_dir` directory. The project is also set up with wandb so and you can change the settings of this under the `wandb` section.

Within the `jobs/` section you will find the pre-made bash scripts for running the experiments shown in the paper. But if you wish to run without them you can simply do so as following:

Training
```
python -m src.run "CONFIG_FILE.yaml" 
```

Inference
```
python -m src.inference "CONFIG_FILE.yaml"
```
