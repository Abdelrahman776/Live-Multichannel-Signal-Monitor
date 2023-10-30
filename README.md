# Live-Multichannel-Signal-Monitor

preview gif

## **Introduction** :-

This PyQt-powered application serves as a **real-time vital sign monitoring system**. It features a polished user interface that offers an intuitive platform for visualizing and analyzing vital signals. This tool empowers users to effortlessly navigate through a diverse array of signals, extracting pertinent information from each, and even provides the flexibility to fine-tune them to precise specifications, delivering a tailored and insightful outcome.

## Features :-

- **Real-Time Playback:** Seamlessly play and display signals in real-time for immediate insights.
- **Playback Controls:** Enjoy comprehensive playback controls, including play, pause, and zoom functionalities, enhancing signal examination.
- **Customization Options:** Personalize signal names and colors to optimize visualization and analysis.
- **Signal Management:** Effortlessly move signals between viewers and selectively hide them for focused examination.
- **Statistical Reports:** Generate comprehensive reports with statistical measures for in-depth signal analysis.
- **Viewer Synchronization:** Link viewers for synchronized playback and simultaneous analysis, ensuring coherence in observations.
- **Snapshot Capture:** Capture snapshots of signal views for documentation or easy sharing.
- **Dynamic Speed Control:** Adjust signal playback speed to suit your specific requirements, facilitating precise examination.

## Installation

1. Clone the repository

```sh
   git clone https://github.com/Abdelrahman776/Live-Multichannel-Signal-Monitor#live-multichannel-signal-monitor
```

2. Install project dependencies

```sh
   pip install typing
   pip install os
   pip install PyQt5
   pip install reportlab
   pip install pandas
   pip install numpy
   pip install pyqtgraph
```

3. Run the application

```sh
   python main.py
```

## Libraries

- PyQt5
- pandas
- pyqtgraph
- matplotlib
- reportlab
- platypus

## Usage

- Playing Signals :-

  Open the file tab at the left hand corner it displays drop-down menu for viewer one and viewer two, choose what you want and then you can browse to choose a signal.

- Changing Signal Properties :-

  you can change the name of the signal on the line-edit with the word label beside it, you can also change color by pushing a button that displays various and
  different color palettes to choose from.

- Moving Signals To Another Viewer :-

  You can move the signal from viewer one to viewer two by clicking a button named Move To V2 and vice versa.

- Playback Controls :-

  You can pause, replay from the specified buttons or zoom in and out by clicking the buttons that have the plus and minus icons, and even speed up or down the velocity of the signal.

- Taking Snapshots :-

  You can take a screenshot of the signal, or more than one signal by clicking on the snapshot icon and save it as an image on your computer.

- Generating Reports :-

  A pdf report is generated when you click on the Generate report tab that displays a table of the statistical measures of each signal, its label and all the snapshots you captured.

- Linking Viewers :-

  Linking the two viewers together for synchronized playback and analysis of the signals, using the controls will enable you to handle the two signals simultaneously.
