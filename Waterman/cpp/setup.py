# https://docs.python.org/3/distutils/apiref.html
from distutils.core import setup
from distutils.extension import Extension

Waterman = Extension(
    'Waterman',
    sources=['Waterman.cpp','QuickHull3D.cpp','Face.cpp','FaceList.cpp','HalfEdge.cpp','Point3d.cpp','Vector3d.cpp','Vertex.cpp','VertexList.cpp'],
    libraries=['boost_python37-mt', 'boost_numpy37-mt'],
    extra_compile_args=['-std=c++11']  # lambda support required
)

setup(
    name='Waterman',
    version='0.1',
    ext_modules=[Waterman])

# call with: python3.7 setup.py build_ext --inplace
