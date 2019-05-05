#!/usr/bin/env python3

import logging
from ArrayTools.matrix import Matrix, Array2D

logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(lineno)d: %(message)s', level=logging.DEBUG)
# logging.info("INFO")
# logging.debug("DEBUG")
# logging.warning("WARNING")
# logging.fatal("FATAL")
test_matrix = True
test_array = True

if __name__ == '__main__':

    if test_matrix:
        m = Matrix(3, 7)
        logging.info("Matrix: {0}".format(type(m)))
        logging.info("m.matrix: {0}".format(m.matrix))
        logging.info("m.ncol: {0}".format(m.ncol))
        logging.info("m.nrow: {0}".format(m.nrow))
        logging.info(m.print())

    if test_array:
        a = Array2D(7, 9)
        logging.info("Array2d: {0}".format(a))
        logging.info("a.ncol: {0}".format(a.ncol))
        logging.info("a.nrow: {0}".format(a.nrow))
