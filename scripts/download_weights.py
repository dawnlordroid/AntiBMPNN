#!/usr/bin/env python3
import os
import urllib.request
import zipfile

URL = "https://zenodo.org/records/13387792/files/model_weights.zip"
TARGET_DIR = "model_weights"
ZIP_PATH = "/tmp/model_weights.zip"

os.makedirs(TARGET_DIR, exist_ok=True)
print(f"Downloading AntiBMPNN model weights from: {URL}")
urllib.request.urlretrieve(URL, ZIP_PATH)

print(f"Unzipping into {TARGET_DIR}/ ...")
with zipfile.ZipFile(ZIP_PATH, 'r') as zf:
    zf.extractall(TARGET_DIR)

os.remove(ZIP_PATH)
print("Done. Weights are in model_weights/")
print("\nTip:")
print('- example/example_scripts.sh 의 --model_name 값을 model_weights/ 안 .pt 파일명(확장자 제외)으로 맞추세요 (예: antibmpnn_000).')
print('- 필요 시 실행 시 --path_to_model_weights model_weights 옵션을 추가하세요.')
