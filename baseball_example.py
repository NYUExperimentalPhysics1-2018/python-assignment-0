
"""
Baseball example:
    asks user for initial velocity and angle of baseball 
    and plots the x-y trajectory of the baseball neglecting air resistance
    
    demonstrates course style guidelines

    @author: Marc Gershow
    TA: John Jacob Jingleheimerschmidt
    Assignment: PS0
"""

import numpy as np
import matplotlib.pyplot as plt


def plotUserTrajectory():
    """prompts user to enter velocity and angle of a projectile then plots the path
    """
    
    v0 = getNumberInputInRange("How fast is your baseball in m/s?", [0,np.Inf])
    theta = getNumberInputInRange("What angle to the ground in degrees?", [0,90])
    [x,y] = calculateTrajectory(v0, theta)
    plt.plot(x,y)
    
def calculateTrajectory(v0, theta, g = 9.8, npts = 100):
    """calculates the trajectory of a projectile 
       
        neglects air resistance
        
        Parameters
        ----------
            v0 : float
                initial velocity (in meters/second): must be >= 0
            theta : float 
                intial angle (in degrees): must be in range [0,90]
            g : float, optional
                acceleration due to gravity (in meters/second): must be > 0, default value 9.8                 
            npts : int, optional
                number of points to calculate along the trajectory
        Returns
        -------
            x,y : ndarray of floats
                x and y positions of the projectile along the trajectory
                in case of error, 'x' and 'y' are empty
    """
    tnext = calculateIntersectionWithGround(v0, theta, g)
    if (np.isnan(tnext) or npts <= 0):
        return (np.emtpy(), np.emtpy())
    tvec = np.linspace(0, tnext, npts)
    vx = v0*np.cos(np.deg2rad(theta))
    vy = v0*np.sin(np.deg2rad(theta))
    x = vx*tvec
    y = vy*tvec - 0.5 * g * np.power(tvec,2)
    return (x,y)


def calculateIntersectionWithGround(v0, theta, g = 9.8):
    """ finds the next time of intersection with the ground for projectile motion
    
        neglects air resistance
        
        Parameters
        ----------
            v0 : float
                initial velocity (in meters/second): must be >= 0
            theta : float 
                intial angle (in degrees): must be in range [0,90]
            g : float, optional
                acceleration due to gravity (in meters/second): must be > 0, default value 9.8
        Returns
        -------
            t : float
                time interval until projectile again has initial vertical position
                
    """
    if (v0 < 0 or theta < 0 or theta > 90 or g <= 0):
        return float('nan')
    vy = v0*np.sin(np.deg2rad(theta))
    return 2*vy/g #time to decelerate = vy/g; takes as long to come back down as to go up
    
def getNumberInputInRange(prompt, validRange):
    """displays prompt and converts user input to a number
    
       in case of non-numeric input, re-prompts user for numeric input
       in case value is out of range, re-promts user to enter a valid value
       
       Parameters
       ----------
           prompt : str
               prompt displayed to user
           validRange : list 
               two element list of form [min, max]
               value entered must be in range [min, max] inclusive
        Returns
        -------
            float
                number entered by user
    """
    
    num = getNumberInput(prompt)
    if (num >= validRange[0] and num <= validRange[1]):
        return num
    print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") #Python 3 sytanx
    return getNumberInputInRange(prompt, validRange)


def getNumberInput (prompt):
    """displays prompt and converts user input to a number
    
       in case of non-numeric input, re-prompts user for numeric input
       
       Parameters
       ----------
           prompt : str
               prompt displayed to user
           validRange : list 
               two element list of form [min, max]
        Returns
        -------
            float
                number entered by user
    """
    
    #note that getNumberInputInRange and getNumberInput could be combined with range as an optional argument
    while True:
        try:
            num = float(input(prompt))
        except Exception:
            print ("Please enter a number")
        else:
            break
    return num
          
#run the main function  
plotUserTrajectory()

    

