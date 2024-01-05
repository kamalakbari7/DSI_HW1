
# Import the argparse library which is used for parsing command line arguments
import argparse 

# Create a new ArgumentParser object.
parser = argparse.ArgumentParser(description='Say Hello')

# Add a positional argument 'name' that will be used to input the user's name.
parser.add_argument(
    'name',
    type= str,
    default='World',
    help='Name to greet',
)

# Add an optional argument '--repeats' that can also be abbreviated as '-r'. 
# It is of type int (integer), and it defaults to 1 if not specified.
# The 'help' parameter provides a brief description of what the argument does.
parser.add_argument(
    '--repeats', 
    '-r', 
    type=int, 
    default=1, 
    help='Number of times to greet')

# Add a positional argument '--goodbye' that will be used to input for saying Goodby to the user's name.
parser.add_argument(
    '--goodbye',
    '-g',
    action='store_true',
    help='Say goodbye instead of hello',
)

# Parse the arguments given by the user and store them in 'args'.
args = parser.parse_args()

# Define the type of greeting, Hello or Goodby
if args.goodbye:
    message = 'Goodbye'
else:
    message = 'Hello'

# Use a for loop to print the greeting the number of times specified by args.repeats.
for _ in range(args.repeats):
  print(f'{message} {args.name}!')
