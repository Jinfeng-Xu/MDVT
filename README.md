# MDVT: Enhancing Multimodal Recommendation with Model-Agnostic Multimodal-Driven Virtual Triplets

## Introduction

This is the Pytorch implementation for our MDVT paper:

>MDVT: Enhancing Multimodal Recommendation with Model-Agnostic Multimodal-Driven Virtual Triplets

## Environment Requirement
- python 3.9
- Pytorch 2.1.0

## Dataset

We utilize three distinct public multimodal recommendation datasets: Baby, Sports, Clothing

## Training
  ```
  cd ./src
  python main.py
  ```
*<u>Static strategies offer broad coverage but are costly. For some models, MDVT can cause significant fluctuations in their original optimal hyper-parameter settings, potentially requiring substantial hyper-parameter search costs to identify the new optimal settings.</u>*

## Performance Comparison

<img src="images/Performance.png"/>

## Citing MDVT

If you find MDVT useful in your research, please consider citing our [paper](https://arxiv.org/pdf/2505.16665).

```
@inproceedings{xu2025mdvt,
  title={Mdvt: Enhancing multimodal recommendation with model-agnostic multimodal-driven virtual triplets},
  author={Xu, Jinfeng and Chen, Zheyu and Li, Jinze and Yang, Shuo and Wang, Hewei and Li, Yijie and Li, Mengran and Wu, Puzhen and Ngai, Edith CH},
  booktitle={Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2},
  pages={3378--3389},
  year={2025}
}
```


## Acknowledgement

The structure of this code is  based on [MMRec](https://github.com/enoche/MMRec). Thank for their work.