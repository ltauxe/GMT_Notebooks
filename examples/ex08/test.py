import mayavi.mlab as  mlab
from netCDF4 import Dataset
import numpy as np
cfile='guinea_bay.nc'
nc=Dataset(cfile,mode='r')
xs= nc.variables['x'][:]
ys=nc.variables['y'][:]
zs=nc.variables['z'][:]
x,y=np.meshgrid(xs,ys)
mlab.mesh(x,y,zs)
mlab.show()

