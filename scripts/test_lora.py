from segment_anything import sam_model_registry
from sam_lora.sam_lora import LoRA_Sam
import torch

if __name__ == "__main__":
    sam = sam_model_registry["vit_b"](
        checkpoint="pretrained_weights/sam_vit_b_01ec64.pth"
    )
    lora_sam = LoRA_Sam(sam, 4)
    lora_sam.sam.image_encoder(torch.rand(size=(1, 3, 1024, 1024)))
