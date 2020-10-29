import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import itertools


class CustomPlotStyle(object):
    def __init__(self, textwidth_in_inches=6.30):
        self.TEXTWIDTH_LATEX = textwidth_in_inches
        self.ASPECT_RATIO = 4/3
        self.SCALE = 1.0
        self.WIDTH = self.SCALE * self.TEXTWIDTH_LATEX
        self.HEIGHT = self.WIDTH / self.ASPECT_RATIO
        self.PALETTE = sns.color_palette(mpl.colors.TABLEAU_COLORS)
        self.MARKERS = ['o', 's', '^', 'v', 'D','P','X','*']
    
    def create_figure(self, width=None, height=None, aspect_ratio=None, width_scale=None):
        if width_scale is None:
            width_scale = self.SCALE
        if width is None:
            width = self.TEXTWIDTH_LATEX * width_scale
        if height is None:
            height = width / self.ASPECT_RATIO
        if aspect_ratio is not None:
            height =  width / aspect_ratio
        fig, ax = plt.subplots(figsize=(width, height), tight_layout=True)
        return fig, ax    
    
    def get_marker_cycle(self):
        return itertools.cycle(self.MARKERS)

    def get_color_cycle(self):
        return itertools.cycle(self.PALETTE)  


def create_label_without_line(label, ax):
    return ax.plot([],[],label=label, linewidth=0, color='k')

def set_figsize(width=6.3, aspect_ratio=4/3, width_scale=1.0):
    width = width * width_scale
    height =  width / aspect_ratio
    return (width, height)    

def save_fig(file_name, output_dir='', dpi=300, file_extensions=['.pdf','.png']):
    file_name = os.path.join(output_dir,file_name)
    for file_extension in file_extensions:
        plt.gcf().savefig(file_name + file_extension, dpi=dpi)