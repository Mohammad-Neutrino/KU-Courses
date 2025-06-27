
import xml.etree.ElementTree as ET
import subprocess, glob, os, datetime
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for filename in glob.glob("open_exoplanet_catalogue/systems/*.xml"):
		system = ET.parse(open(filename, 'r'))
		planets = system.findall(".//planet")
		for planet in planets:
			try:
				M = float(planet.findtext("./mass"))
				a = float(planet.findtext("./semimajoraxis"))
				discoverymethod = planet.findtext("./discoverymethod")
				if discoverymethod=="RV":
				   plt.scatter(a, M, s = 4, c = 'r')
				   
				elif discoverymethod=="transit":
				     plt.scatter(a, M, s = 4, c = 'b')
				     
				elif discoverymethod=="imaging":
				     plt.scatter(a, M, s = 4, c = 'm')
				     
				elif discoverymethod=="microlensing":
				     plt.scatter(a, M, s = 4, c = 'g')
				     
				elif discoverymethod=="timing":
				     plt.scatter(a, M, s = 4, c = 'c')
				     
				else:
				    plt.scatter(a, M, s = 4, c = 'k')
				    
				
			except:
				# Most likely cause for an exception: Mass or semi-major axis not specified for this planet.
				# One could do a more complicated check here and see if the period and the mass of the host star is given and then calculate the semi-major axis 
				pass

plt.scatter([], [], c = 'r', label = 'RV')
plt.scatter([], [], c = 'b', label = 'Transit')
plt.scatter([], [], c = 'm', label = 'Direct Imaging')
plt.scatter([], [], c = 'g', label = 'Microlensing')
plt.scatter([], [], c = 'c', label = 'Pulsar Timing')
plt.scatter([], [], c = 'k', label = 'Others')

plt.legend(loc = 'upper center', bbox_to_anchor=(0.5, 1.09), ncol = 3, fancybox = True, shadow = True)
plt.grid(color = 'k', alpha = 0.5, linestyle = 'dotted', linewidth = 0.6)
ax.set_xlabel(r'Semimajor Axis, a [AU]')
ax.set_ylabel(r'Planet Mass, $M_p$ [$M_J$]')
ax.set_yscale('log')
ax.set_xscale('log')
plt.savefig('Exoplanet_Discovery_Methods.pdf')
plt.show()
				
	        
				
				
