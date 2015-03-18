# -*. coding: utf-8 -*-
# Copyright (c) 2015 CNRS and University of Strasbourg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

"""
capillary - A class describing a capillary used in electrophoresis
"""
class Capillary:
    def __init__(self, total_length = 100.0, to_window_length = 90.0,
                 diameter = 30.0, pressure = 30.0, duration = 21.0,
                 viscosity = 1.0, concentration = 21.0,
                 molecular_weight = 150000.0, voltage = 30000.0,
                 electric_current = 4.0, detection_time = 3815.0,
                 electro_osmosis_time = 100.0):
        # The length of the capillary (centimeter)
        self.total_length = total_length
        # The window length (centimeter)
        self.to_window_length = to_window_length
        # The capillary inside diameter (micrometer)
        self.diameter = diameter
        # The pressure drop across the capillary (mbar)
        self.pressure = pressure
        # The time the pressure is applied (second)
        self.duration = duration
        # The buffer viscosity (cp)
        self.viscosity = viscosity
        # Analyte concentration (mol/l)
        self.concentration = concentration
        # Analyte molecular weight (g/mol)
        self.molecular_weight = molecular_weight
        # The voltage applied to the capillary (volt)
        self.voltage = voltage
        # The current applied to the capillary (microampere)
        self.electric_current = electric_current
        # The detection time (s)
        self.detectionTime = detection_time
        # The electro-osmosis time (s)
        self.electro_osmosis_time = electro_osmosis_time


    def getDelivedVolume(self):
        """Add description"""
        return 0.0

    def getCapillaryVolume(self):
        """Add description"""
        return 0.0

    def getToWindowVolume(self):
        """Add description"""
        return 0.0

    def getInjectionPlugLength(self):
        """Add description"""
        return 0.0

    def getTimeToReplaceVolume(self):
        """Add description"""
        return 0.0

    def getViscosity(self):
        """Add description"""
        return 0.0

    def getConductivity(self):
        """Add description"""
        return 0.0

    def getFieldStrength(self):
        """Add description"""
        return 0.0

    def getMicroEOF(self):
        """Add description"""
        return 0.0

    def getLengthPerMinute(self):
        """Add description"""
        return 0.0

    def getFlowRate(self):
        """Add description"""
        return 0.0
