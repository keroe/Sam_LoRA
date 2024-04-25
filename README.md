# LoRA for SAM (meta's segment-anything)

## Usage
1. Create a conda environment and install pytorch as described [here](https://pytorch.org/get-started/locally/)
2. run `pip install .` or `pip install -e .`
3. Get the model checkpoints [here](https://github.com/facebookresearch/segment-anything/tree/main?tab=readme-ov-file#model-checkpoints) or run   
`mkdir pretrained_weights &&  wget -P pretrained_weights https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth`

### Example
See the [test](./scripts/test_lora.py)

## Train
Coming soon and welcome pull request.

## Thanks
The code for LoRA ViT comes form
https://github.com/JamesQFreeman/LoRA-ViT
