PInfMain.py
================

This script presents an adaptation of Chiu et al.'s 2015 experiment investigating
the influence of peer influence, or 'other-conferred utility', on lottery choice
decision-making. See the original paper [here](https://www.nature.com/articles/nn.4022).
I adapted the code utilized by the original authors to operate standalone in Python,
using PsychoPy for stimulus presentation, and pynput for event monitoring.

This iteration of the task also experiences some procedural differences. Most notably,
participants are assessed in groups of two, so there are only two positions in the task,
and therefore there is only one partner. Consequentially, mix trials are omitted. There
are also some timing differences between trial stages, and differences in coloring, sizing,
and stimulus positioning.
