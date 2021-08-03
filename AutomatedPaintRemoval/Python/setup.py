import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg-PaintRemovalRobot",
    version="0.1.2",
    author="Joey Meijer",
    author_email="Joey.Meijer@inholland.nl",
    description="PaintRemovalRobot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/meijerjoey/paint-removal-robot-prr",
    packages=setuptools.find_packages(),
    install_requires=[
        'cv2',
        'PySide2',
        'robodk',
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.7.9',
)