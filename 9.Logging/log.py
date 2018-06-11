import logging
import math

#create and configurate logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "./log_file.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "w")
logger = logging.getLogger()

#test the logger
logger.debug("We are in love")
logger.info("I have been cheated!")
logger.warning("You will suffer")
logger.error("I shouldn't done it")
logger.critical("Well, is to late")


#Let try it
def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    #compute the discriminant
    logger.debug("#compute the discriminant")
    disc = b**2 - 4*a*c

    #compute the two root
    logger.debug("#compute the two root")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    #Return the roots
    logger.debug("#Return the roots")
    return(root1,root2)

roots = quadratic_formula(1,0,-4)
print(roots)
