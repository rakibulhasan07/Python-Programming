import logging

# Create and configure logger
logging.basicConfig(
    filename="myfile.log",  # লগ ফাইলের নাম
    format='%(asctime)s - %(levelname)s - %(message)s',  # লগ মেসেজ ফরম্যাট
    filemode='w'  # পুরনো ফাইল মুছে নতুন করে লেখা হবে
)

# Creating an object of logger
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG (সব message capture হবে)
logger.setLevel(logging.DEBUG)

# Test log messages
logger.debug("Harmless debug message, used for diagnosing problems.")

logger.info("Program started successfully. All systems go!")

logger.warning("Low disk space warning. Please check your storage.")

logger.error("An error occurred while processing the request.")

logger.critical("Critical issue! System might be down.")