# Parameter reconstruction for non-linear stress-strain relations

## Problem statement
The purpose of this project is to implement various machine learning techniques to reconstruct the model parameters from given stress-strain curves. It is a priori known that the stress-strain relation is given by an explicit *Ramberg-Osgood* model, which represents a non-linear relation between the stress and the strain 
 
## Data-driven approach
The implemented machine learning models learn the non-linear stress-strain relation through training data. Herein, each training sample corresponds to vector-valued stresses and strains, which are mapped to the corresponding model parameters. To this end, the following split is proposed:

*   features: stress and strain vectors
*   labels: two model parameters

Note that the labels represent the target of a prediction, while the data generation process will be explained later. Since two parameters correspond to each stress-strain curve, the machine learning problem is consequently classified as a **multi-target regression**.


## Model requirements
The trained model should predict the material parameters from stress-strain curves, while the following requirements should be addressed through the implementation:

* noise in the stress-strain curves to represent experimental data,
* data points for the strain values are unevenly distributed,
* flexible adjustment of the number of data points in stress-strain curves.

## Solution procedure

* Analyze an exemplary stress-strain curve.
* Generating apropriate test and train data.
* Implement a machine learning model.
* Training the model and optimize hyperparameter.
* Evaluate the generalization performance on the test data.

## Using Anaconda 
The environment file `mlenv.yml` was used to produce the output presented in the Jupyter notebook. You can find a helpful guide about anaconda installation environments through the following link: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
