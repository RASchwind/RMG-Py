#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
#   RMG - Reaction Mechanism Generator
#
#   Copyright (c) 2002-2010 Prof. William H. Green (whgreen@mit.edu) and the
#   RMG Team (rmg_dev@mit.edu)
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the 'Software'),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#
################################################################################

import sys

try:
    from distutils.core import setup
    from distutils.extension import Extension
except ImportError:
    print 'The distutils package is required to build or install RMG Py.'
    
try:
    from Cython.Distutils import build_ext
    import Cython.Compiler.Options
except ImportError:
    print 'Cython (http://www.cython.org/) is required to build or install RMG Py.'
    
try:
    import numpy
except ImportError:
    print 'NumPy (http://numpy.scipy.org/) is required to build or install RMG Py.'

# Create annotated HTML files for each of the Cython modules
Cython.Compiler.Options.annotate = True

# Turn on profiling capacity for all Cython modules
#Cython.Compiler.Options.directive_defaults['profile'] = True

################################################################################

def getMainExtensionModules():
    return [
        # Molecules and molecular representations
        Extension('rmgpy.molecule.atomtype', ['rmgpy/molecule/atomtype.py'], include_dirs=['.']),
        Extension('rmgpy.molecule.element', ['rmgpy/molecule/element.py'], include_dirs=['.']),
        Extension('rmgpy.molecule.graph', ['rmgpy/molecule/graph.py'], include_dirs=['.']),
        Extension('rmgpy.molecule.group', ['rmgpy/molecule/group.py'], include_dirs=['.']),
        Extension('rmgpy.molecule.molecule', ['rmgpy/molecule/molecule.py'], include_dirs=['.']),
        Extension('rmgpy.molecule.symmetry', ['rmgpy/molecule/symmetry.py'], include_dirs=['.']),
        # Statistical mechanics
        Extension('rmgpy.statmech.mode', ['rmgpy/statmech/mode.pyx']),
        Extension('rmgpy.statmech.schrodinger', ['rmgpy/statmech/schrodinger.pyx']),
        # Miscellaneous
        Extension('rmgpy.constants', ['rmgpy/constants.py'], include_dirs=['.']),
        Extension('rmgpy.kinetics', ['rmgpy/kinetics.py'], include_dirs=['.']),
        Extension('rmgpy.quantity', ['rmgpy/quantity.py'], include_dirs=['.']),
        Extension('rmgpy.reaction', ['rmgpy/reaction.py'], include_dirs=['.']),
        Extension('rmgpy.species', ['rmgpy/species.py'], include_dirs=['.']),
        Extension('rmgpy._statmech', ['rmgpy/_statmech.pyx'], include_dirs=['.']),
        Extension('rmgpy.statmech', ['rmgpy/statmech.py'], include_dirs=['.']),
        Extension('rmgpy.thermo', ['rmgpy/thermo.py'], include_dirs=['.']),
    ]

def getMeasureExtensionModules():
    return [
        Extension('rmgpy.measure._network', ['rmgpy/measure/_network.pyx'], include_dirs=['.']),
        Extension('rmgpy.measure.collision', ['rmgpy/measure/collision.pyx'], include_dirs=['.']),
        Extension('rmgpy.measure.reaction', ['rmgpy/measure/reaction.pyx'], include_dirs=['.']),
        Extension('rmgpy.measure.msc', ['rmgpy/measure/msc.pyx'], include_dirs=['.']),
        Extension('rmgpy.measure.rs', ['rmgpy/measure/rs.pyx'], include_dirs=['.']),
        Extension('rmgpy.measure.cse', ['rmgpy/measure/cse.pyx'], include_dirs=['.']),
        Extension('rmgpy.measure.me', ['rmgpy/measure/me.pyx'], include_dirs=['.']),
        Extension('rmgpy.constants', ['rmgpy/constants.py'], include_dirs=['.']),
        Extension('rmgpy.quantity', ['rmgpy/quantity.py'], include_dirs=['.']),
        Extension('rmgpy._statmech', ['rmgpy/_statmech.pyx'], include_dirs=['.']),
    ]
    
def getSolverExtensionModules():
    return [
        Extension('rmgpy.solver.base', ['rmgpy/solver/base.pyx'], include_dirs=['.']),
        Extension('rmgpy.solver.simple', ['rmgpy/solver/simple.pyx'], include_dirs=['.']),
    ]

################################################################################

ext_modules = []
if 'install' in sys.argv:
    # This is so users can still do simply `python setup.py install`
    ext_modules.extend(getMainExtensionModules())
    ext_modules.extend(getMeasureExtensionModules())
    ext_modules.extend(getSolverExtensionModules())
elif 'main' in sys.argv:
    # This is for `python setup.py build_ext main`
    sys.argv.remove('main')
    ext_modules.extend(getMainExtensionModules())
elif 'measure' in sys.argv:
    # This is for `python setup.py build_ext measure`
    sys.argv.remove('measure')
    ext_modules.extend(getMeasureExtensionModules())
elif 'solver' in sys.argv:
    # This is for `python setup.py build_ext solver`
    sys.argv.remove('solver')
    ext_modules.extend(getSolverExtensionModules())   
    
scripts=['cantherm.py', 'measure.py', 'rmg.py']

# Initiate the build and/or installation
setup(name='RMG Py',
    version='0.1.0',
    description='Reaction Mechanism Generator',
    author='William H. Green and the RMG Team',
    author_email='rmg_dev@mit.edu',
    url='http://rmg.mit.edu/',
    packages=['rmgpy'],
    scripts=scripts,
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    include_dirs=[numpy.get_include()],
)
