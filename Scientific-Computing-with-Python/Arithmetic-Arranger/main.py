# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

#import the main function of the arithmetic formatter
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(['3 + 855', '988 + 40'], True))

# Run unit tests automatically
main(['-vv'])
