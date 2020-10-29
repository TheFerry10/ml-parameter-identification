class PlotLabels(object):
    """Creating plot labels for convenience and use them globally"""
    def __init__(self):
        self.time = r'Time $t$ [s]'
        self.stress = r'Stress $\sigma$ [N/m$^2$]'
        self.stress_in_MPa = r'Stress $\sigma$ [MPa]'
        self.strain = r'Strain $\varepsilon$ [-]'
        self.concentration = r'Concentration $c$ [mg/l]'
        self.rmse = r'Residual Mean Squared Error [-]'
        self.epochs = r'Number of epochs for training [-]'