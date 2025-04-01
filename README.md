# ghost-hunter

>[!NOTE]
> All the file imports have been setup so that they are relative to the top folder. 
> So that when you reference files in the config files, always use folder paths relative to the top repo folder.

## Labelling
run `python labelling/gui_labeller.py` to start labelling images. Where the filename and label are pasted into labels.yaml. 

The labelled training data files from the paper are also contained within the `labelling/` directory.

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
