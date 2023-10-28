#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 10:49
# @Author  : unicorn-yh
# @File    : download.py
from huggingface_hub import snapshot_download

repo_id = "meta-llama/Llama-2-7b-hf"  # 模型在huggingface上的名称
local_dir = "model/llama2/Llama-2-7b-hf"  # 本地模型存储的地址
local_dir_use_symlinks = False  # 本地模型使用文件保存，而非blob形式保存
token = "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"  # 在hugging face上生成的 access token


snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    local_dir_use_symlinks=local_dir_use_symlinks,
    token=token
)
