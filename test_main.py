import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self):
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200 )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 2 - this_x[i])<1e-7, "the x coordinates in your graph are not correct" )
            
    def test_svariance(self) :
       # Do some resampling
       samples = 100*[0]
       for i in range(100) : 
          samples[i], mean = 0, 0
          for j in range(200) : 
             val = expectation + np.sqrt(variance)*np.random.normal(0,1)
             mean = mean + val
             samples[i] = samples[i] + val*val
          mean = mean / 200
          samples[i] = ( 200 / 199 )*( samples[i] / 200 - mean*mean )
    
       samples.sort()

       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       ss = this_y[len(this_y)-1]
       self.assertTrue( ss>samples[0] and ss<samples[98], "the y-coordinates in your graph appear to be incorrect" )
