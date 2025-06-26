from setuptools import setup, find_packages

setup(
    name="cocola",
    version="0.1.1",
    description="Cocola package for feature extraction and evaluation",
    author="Gladia Research Group, Ruben Ciranni    ",
    author_email="contact@gladia.org",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "lightning[pytorch-extra]>=2.2.1",
        "numpy>=1.26.4",
        "torch>=2.2.2",
        "torchvision>=0.17.2",
        "torchaudio>=2.2.2",
        "pandas>=2.2.1",
        "efficientnet_pytorch==0.7.1",
        "tqdm>=4.66.2",
        "librosa>=0.10.1",
        "soundfile>=0.12.1",
    ],
    py_modules=["contrastive_model", "feature_extraction"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
