# Structured-Pruning-for-Semantic-Segmentation-A-Comprehensive-Analysis

## Goal of the Project
This project investigates the application of structured pruning techniques to enhance the efficiency of real-time semantic segmentation models crucial for computer vision applications. This project investigates the application of structured pruning techniques to enhance the efficiency of real-time semantic segmentation models crucial for computer vision applications. Employing popular architectures such as ICNet and BiSeNetV2, we conducted a comprehensive analysis of the impact of structured pruning on model accuracy, inference speed, and parameter reduction. Our research explores the tradeoff between model compression and task-specific performance, considering various pruning ratios and strategies. The findings provide valuable insights into the feasibility and efficacy of structured pruning for optimizing neural networks, offering a roadmap for deploying efficient semantic segmentation models in resource-constrained environments within the evolving landscape of machine learning.

## Overview
This GitHub repository presents the culmination of groundbreaking research aimed at optimizing real-time semantic segmentation models using structured pruning techniques. The project focuses on two prominent architectures, ICNet and BiSeNetV2, leveraging structured pruning to assess and enhance critical metrics such as accuracy, speed, and parameter reduction.

## Key Contributions
In-Depth Analysis: We conducted a comprehensive analysis of the ICNet and BiSeNetV2 architectures, employing structured pruning to understand its impact on crucial metrics. The study delves into the delicate balance between model compression and task-specific performance, especially in resource-constrained environments.

Structured Pruning Methodologies: The repository introduces and implements structured pruning methodologies within the PyTorch framework. This systematic approach reduces model complexity while maintaining or improving real-world performance.

ICNet Optimization: Our methodology achieved a significant 11% reduction in model parameters for ICNet. Despite the reduction, the mean Intersection over Union (mIoU) was maintained at the benchmark level of 67.62. Notably, we achieved a real-time performance of 31 frames per second (FPS), showcasing a fine balance between speed and accuracy.

BiSeNetV2 Tradeoffs: The results for BiSeNetV2 revealed an unrecoverable mIoU degradation of 67.49 (benchmark 73.4) despite minimal sparsity. However, we achieved a notable FPS of 54, highlighting the nuanced tradeoffs between model compression and performance metrics.

## Repository Structure
Semantic_Segmentation_X.ipynb - Contains the implementation of structured pruning methodologies in PyTorch for ICNet and BiSeNetV2.

/models - Explore this folder for scripts for model architecture definitions.

/Outputs - This directory contains the outputs generated during experiments, including logs, model checkpoints, and evaluation results.

/configs - Here, you'll find configuration files used for training and evaluating the models. Adjust these configurations to customize experiments.

/tools -  Essential tools and scripts that support the experimentation process, including fine-tuning and evaluation.

/utils - Utilities and helper functions that facilitate data preprocessing, visualization, and other essential tasks.

## Conclusion
Our research represents a significant step forward in the optimization of real-time semantic segmentation models. By addressing the challenges posed by computational constraints in dynamic urban environments, we've provided valuable insights into the interplay between model compression, task adaptation, and overall performance. Moving forward, we aim to refine our approach and overcome resource limitations, unlocking new avenues for advancing the efficiency and adaptability of deep learning models in real-world applications.

