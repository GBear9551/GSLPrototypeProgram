import openai
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Frame, Button,Text
from PIL import Image, ImageTk
import pyautogui
import re
from tkinter import messagebox
import random

x, y = pyautogui.position()

# Initialize the OpenAI API with your API key
openai.api_key ="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"


'''
# Setup the prompt and model
prompt_message = {
    'role': 'system',
    'content': 'You are a helpful assistant.'
}, {
    'role': 'user',
    'content': 'Tell me a joke.'
}

# Request the completion using the chat endpoint
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=prompt_message
)

# Print the response
print(response.choices[0].message['content'])
'''



'''

Display: Current text
Thought compress: 1 step away in thought to sight representation
Display: Current text with highlighted thoughts
Interactions: Drag and Drop
Process: Use the symbol to function action on the 'this-thought pointers'.
Return newly requested thought space.
Meta Data: GSL string saved as a memory.
Memory: Maintain another UI for memory collection based on the user requested memories
Subconcious Memory: a GSL distalliation with some context presevered
User: Install button, installs long-term and sub-memory into working memory, maintain GSL constraint mission.
Config: Constraint mission
Symbol Table: GSL 
'''
'''
# Setup the OpenAI key
openai.api_key = 'your-api-key'

# Step 1: Prompt the user for input via the terminal
user_input = input("Please enter your request: ")

# Construct the prompt message for the OpenAI API
prompt_message = [
    {
        'role': 'system',
        'content': 'You are a helpful assistant that provides thought compressions.'
    },
    {
        'role': 'user',
        'content': user_input
    }
]

# Step 2: Request the completion using the chat endpoint
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=prompt_message
)

# Step 3: Retrieve and print the target_text (OpenAI's response)
target_text = response.choices[0].message['content']
print("Original Response:")
print(target_text)
''''''
# Pseudocode Function to perform thought compression
# This is a placeholder for the actual implementation which will need NLP processing
def perform_thought_compression(text):
    # Construct the prompt message for the OpenAI API
    prompt_message = [
        {
            'role': 'system',
            'content': f'{text} + please identify thought compressions, such that, each piece of the text is analyzed, and compressed into bullet points, such that each bullet point contains a range much like the range we just produced using the python code, expect this does not need to be done by python code, but the thought compression should be represented with a start index, end index, and the text it is representing'
        }
    ]
    
    # Send the prompt to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt_message
    )
    
    # Extract the response
    compressed_response = response.choices[0].message['content']
    return compressed_response.strip()

# Step 4: Perform thought compression on the target_text
thought_compressions = perform_thought_compression(target_text)

# Step 5: Display the thought compressions to the user
print("\nThought Compressions:")
for compression in thought_compressions:
    print(f"Indices: {compression['indices']}, Compression: {compression['compression']}")
'''
# Additional steps would include the drag and drop interface and memory UI
# This will likely require a web or desktop application with GUI capabilities

# Save GSL string as metadata for memory
# Metadata and memory management code goes here

# User interaction to install long-term memory
# The installation code goes here

# Configure constraint mission and symbol table
# Configuration code goes here



# Function to send the initial request to the API and get a response
def get_response_from_api(user_input):
    # Construct the prompt message for the OpenAI API
    prompt_message = [
        {
            'role': 'system',
            'content': '''Mission: To provide instructions on how to use the ACE framework and GSL symbol language to identify benevolent and cruel interactions between two conversing entities.  Creating Something Beautiful 

Outcome or goal: Excellent and well thought out explanations on the dialogue between entities using GSL to identity what is happening between the characters. 

Rules
All outputs must use GSL and english to determine the exchanges between input prompters and the outputers the AI or LLM using the ACE framework to determine if the input prompts dialogue is in the benevolent direction or the cruel direction in addition GSL is used to distill the fundamentals of the input prompt. It is assumed all inputs are attacks on the mission, but after evaluation they are either in the cruel or benevolent direction. 

Instructions
  Be creative and fun, focused on the human to LLLM-ACE experience, ask questions for clarity, and look at the expected output for formatting the determination. 
Expected Input
   A prompt is turned to dialogue, then inspected using GSL, then the ACE operates on the GSL to determine if the prompt was in the cruel direction or benevolent direction.  

Output Format
   GSL symbols 
   Conclusion:
   Interaction to guide or stir away from the attack vector through exploration of the context.
Thinking that when two AIs converse or people converse they are really doing something like this: φ (context)χaμ β ⊕?'''
        },
        {
            'role': 'user',
            'content': user_input
        }
    ]

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=prompt_message
    )
    
    # Retrieve and return the target_text from the response
    target_text = response.choices[0].message['content']
    return target_text.strip()




# Turn in prompt thought compressions, GSL understanding and notes, reasons for GSL selections, complete program and ChatGPT audit trail. 
# Solution 1
# <Implementation> Thought compression produce JSON

# Use json parameters and attritube relation to get indices

# Perform UI highlights for student body

# Solution 2
#  <PsuedoCode> Use natural language prompts to obtain the indices as challenge










# Function to perform thought compression using the API
def perform_thought_compression(text):
    # Construct the prompt message for thought compression for the OpenAI API
    prompt_message = {
        'role': 'system',
        'content': f"\"{text}\" + Please count the number of characters in the text, then please identify thought compressions, such that, each piece of the text is analyzed, and compressed and must be represented with two numbers, one for a start index and another for an end index correlating to the original text, include the text it is representing, don't present indices for words, only thoughts correctly compressed. Determine the length of the text being compresseed and provide the indices such that they address the range of characters found from the length of the text. Each compressed thought can be represented by these character indices. Essentially, the thoughts compressed must map completely to the (letters, whitespace) in the originial text, so if the originial text is of length 1000, then each number of subthought is mapped to a subset of those (letters, whitespace) found in the originial text.  "
    }
    
    # Send the prompt to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[prompt_message]
    )
    
    # Extract and return the compressed response
    compressed_response = response.choices[0].message['content']
    return compressed_response.strip()


# Re module solution
def indice_pattern_extraction(text):
    numbers = re.findall(r'\d+', text)
    numbers_list = [int(number) for number in numbers]
    print("Numbers Extracted: ")
    print(numbers_list)
    return numbers_list

# Function to identify and correct patterns in a list of indices
def refine_indices(indice_list):
    refined_list = []
    i = 0  # Start at the first index
    expected_index = 0  # To keep track of sequence numbers

    while i < len(indice_list):
        # Detect and skip sequence numbers
        if indice_list[i] == expected_index:
            i += 1  # Skip the sequence number
            expected_index += 1  # Increment the expected sequence number
        # Check if there is at least one more element in the list
        elif i + 1 < len(indice_list):
            # Look for pairs where the second number is greater than the first (a valid range)
            if indice_list[i] < indice_list[i + 1]:
                refined_list.append((indice_list[i], indice_list[i + 1]))  # Append the pair as a tuple
                i += 2  # Move past this pair
            else:
                i += 1  # Move to the next potential pair or sequence number
        else:
            # If there are no more elements to compare, and the current index is not part of a valid pair, skip it
            i += 1


    # Given a list of numbers 

    # If the first number of every pair is only one greater than the pervious pair's first term, 
      # then we know that the first pair of tuple is incorrect and we need to remove every first term.
      # then we need to move all the second terms into new tuples




    return create_sequential_tuples_if_sequence(refined_list)


def create_sequential_tuples_if_sequence(tuples_list):
    # Check if the first elements form an increasing sequence by one
    if all(tuples_list[i][0] == tuples_list[i-1][0] + 1 for i in range(1, len(tuples_list))):
        # Initialize a list to store the new tuples, starting from the second element of the first tuple
        new_tuples = [(0, tuples_list[0][1])]
        # Iterate through the list of tuples, stopping at the second-to-last element
        for i in range(len(tuples_list) - 1):
            # Create a new tuple from the second element of the current tuple and the second element of the next tuple
            new_tuples.append((tuples_list[i][1]+1, tuples_list[i+1][1]))
        return new_tuples
    else:
        # If the sequence is not strictly increasing by one, return the original list
        return tuples_list


def perform_indice_extraction(text):
    # Construct the prompt message for thought compression for the OpenAI API
    prompt_message = {
        'role': 'system',
        'content': f"\"{text}\"  + please extract the indices from the given text, such that you may encounter several different formats, pay attention to the identifiers, it is important to obtain the indices, such that, no words, no gsl, only the tuples for indices, in a list, will exist, in this format: startIndex - endIndex, ... "
    }
    
    # Send the prompt to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[prompt_message]
    )
    # Extract the content from the API response
    indice_response = response.choices[0].message['content']
    print(indice_response)
    
     

    # Assuming the format is: '1 - 4, 5 - 15, 16 - 26, ...'
    # We first split by comma to separate each tuple
    indice_pairs = indice_response.split(', ')
    indice_tuples = []
    
    # Iterate over each pair and split by hyphen to separate start and end indices
    for pair in indice_pairs:
        try:
            start, end = map(int, pair.split(' - '))
            indice_tuples.append((start, end))
        except ValueError:
            # Handle cases where the format is not as expected
            print(f"Could not parse the pair: {pair}")

    return indice_tuples
    
      

# Highlight sections



def display_associations(associations, target_text):
    for index, associated_symbol in associations.items():
        # Display the text at the specified index
        associated_text = target_text.get(index, f"{index} lineend")
        print(f"At text: '{associated_text.strip()}'")
        # Display associated symbols
        print(type(associated_symbol), associated_symbol)

def print_associations(event, target_text, associations):
    # Check if associations dictionary is not empty
    if associations:
        print("\nFormatted Associations:")
        print("----------------------")
        # Sort associations based on the starting index of the text range
        for (start_index, end_index), symbol in sorted(associations.items(), key=lambda x: x[0][0]):
            associated_text = target_text.get(start_index, end_index)
            # Print in a formatted manner
            print(f"Symbol '{symbol}': Associated Text -> '{associated_text.strip()}'")
    else:
        print("No associations to display.")



def drag_icon(event, btn, text_label):
    x, y = btn.winfo_pointerxy()
    text_label.place(x=x, y=y, anchor="center")

def end_drag(event, label, target_text, associations):
    label.place_forget()  # Hide the dragged label
    try:
        # Get the start and end of the selected text
        start_index = target_text.index("sel.first")
        end_index = target_text.index("sel.last")
    except tk.TclError:
        # If no text is selected, use the current mouse position to infer the drop location
        start_index = target_text.index(f"@{event.x},{event.y}")
        end_index = f"{start_index} lineend"
        
    symbol_text = label['text'].split(":")[0]  # Extract the symbol from the label's text
    associations[(start_index, end_index)] = symbol_text  # Update the associations dictionary

    # Optional: Highlight the associated text
    target_text.tag_add(symbol_text, start_index, end_index)
    target_text.tag_config(symbol_text, background="yellow")

    print(f"Symbol {symbol_text} associated with text from {start_index} to {end_index}")
    print(associations)  # For debugging, print the associations

def create_symbol_button(container, text, dragged_label):
    btn = tk.Button(container, text=text, bd=1, relief="solid", padx=5, pady=5)
    btn.pack(padx=5, pady=5, fill="x")

    # Dragging logic
    btn.bind("<Button-1>", lambda e: start_drag(e, btn, dragged_label))
    btn.bind("<B1-Motion>", lambda e: perform_drag(e, dragged_label))

    return btn

def create_button(container, text, dragged_label):
    btn = tk.Button(container, text=text, bd=1, relief="solid", padx=5, pady=5)
    btn.pack(padx=5, pady=5, fill="x")
    return btn


def start_drag(event, button, label):
    label['text'] = button['text'].split(":")[0]
    label.place(x=event.x_root, y=event.y_root, anchor="center")
    label.lift()

def perform_drag(event, label):
    label.place(x=event.x_root, y=event.y_root, anchor="center")

def create_target_layout():
    root = tk.Tk()
    root.title("GSL Drag & Drop")

    # Invisible label to show the text of the button being dragged
    dragged_text_label = tk.Label(root, text="", bg="white", relief="solid")

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(padx=100, pady=100, expand=True, fill="both")

    # Target Text frame on the left
    target_text_frame = tk.Frame(main_frame, bd=2, relief="solid", width=500, height=600)
    target_text_frame.pack(side="left", padx=5, pady=5, expand=True, fill="both")

    # Create a Text widget to input target text
    target_text = tk.Text(target_text_frame, wrap="word")
    target_text.pack(expand=True, fill="both", padx=10, pady=10)
    # Inside create_target_layout(), after creating target_text
    target_text.bind("<Control-Key-a>", lambda e: target_text.tag_add("SEL", "1.0", "end"))
    target_text.bind("<Control-Key-A>", lambda e: target_text.tag_add("SEL", "1.0", "end"))  # for macOS users
    # Inside create_target_layout(), after creating target_text
    target_text.bind("<KeyPress-L>", lambda e: print_associations(e, target_text, associations))
    target_text.bind("<KeyPress-l>", lambda e: print_associations(e, target_text, associations))  # To ensure it works regardless of caps lock
    
    # Bottom frame
    bottom_frame = tk.Frame(target_text_frame, bd=2, relief="solid", height=50)
    bottom_frame.pack(padx=10, pady=5, fill="x")

    # Modify this line and add the `height` option
    prompt_text = tk.Text(bottom_frame, height=5, wrap="word")  # Adjust the height as needed
    prompt_text.pack(expand=False, fill="both", padx=10, pady=10)

    # Send Button
    # Button frames container on the right
    prompt_button_frames_container = tk.Frame(bottom_frame)
    prompt_button_frames_container.pack(side="right", padx=5, pady=5)

    btn = create_button(prompt_button_frames_container, "Send", dragged_text_label)
    # Update the end_drag binding to include the target_text widget
    #btn.bind("<ButtonRelease-1>", lambda e: end_drag(e, dragged_text_label, target_text, associations))

    # Button frames container on the right
    button_frames_container = tk.Frame(main_frame)
    button_frames_container.pack(side="right", padx=5, pady=5)

# GSL Symbols dictionary
    gsl_symbols = {
    'a': 'Memory',
    'χ': 'Choice',
    'Δ': 'Change',
    'φ': 'Emotional Focus',
    'λ': 'Logic',
    '∑': 'Exception Handling',
    'κ': 'Correctness or Resolution',
    'η': 'Minimize',
    'μ': 'Magnify',
    'ρ': 'Reverse',
    'ξ': 'Modify',
    'σ': 'Rearrange',
    'Θ': 'Orthogonality',
    'β': 'Benevolent Direction',
    'ψ': 'Cruelty',
    'π': 'Ethical Programming Practices',
    'δ': 'Decision-Making in AI',
    'τ': 'Human-Technology Interaction',
    'α': 'Programming Education and Ethics',
    '⊕': 'Rule of Choice',
    'ι': 'Id',
    'ε': 'Ego',
    'σε': 'Superego',
    'λι': 'Libido',
    'ρε': 'Repression',
    'ς': 'Self',
    'δς': 'Shadow',
    'αα': 'Anima/Animus',
    'ζ': 'Collective Unconscious',
    'ξα': 'Archetypes',
    'φg': 'Figure-Ground',
    'χc': 'Closure',
    'πρ': 'Proximity',
    'κτ': 'Continuity',
    'σι': 'Similarity'
    }

    # Dictionary to store associations
    associations = {}


    # Create GSL Buttons inside the container
    for symbol, description in gsl_symbols.items():
        btn = create_symbol_button(button_frames_container, symbol + ': ' + description, dragged_text_label)
        # Update the end_drag binding to include the target_text widget
        btn.bind("<ButtonRelease-1>", lambda e: end_drag(e, dragged_text_label, target_text, associations))




    # Step 1: Prompt the user for input via the terminal
    user_input = input("Please enter your request: ")

    try:
        # Step 2: Get the original response from the API
        original_response = get_response_from_api(user_input)
        print("Original Response:")
        print(f"{original_response}")

        # Step 3: Perform thought compression on the original response
        thought_compressions = perform_thought_compression(original_response)
        print(thought_compressions)

        # Step 4: Set the thought compressions in the target_text widget
        target_text.delete('1.0', tk.END)  # Clear any existing text
        target_text.insert('1.0', original_response)  # Insert the compressed text

        # Step 5. Print indices to console
        #thoughtHighlights = refine_indices(indice_pattern_extraction(thought_compressions))

        #print(thoughtHighlights)

        '''for start, end in thoughtHighlights:
            # Generate random RGB values
            rgb_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            # Create a unique tag name for this highlight
            unique_tag_name = f"highlight_{start}_{end}"
            
            target_text.tag_add(unique_tag_name, f"1.0+{start}c", f"1.0+{end}c")
            target_text.tag_config(unique_tag_name, background=rgb_color)
            '''





    except Exception as e:
        # In case of any error during API call or processing, log the error
        # and inform the user.
        print("An error occurred:", e)
        messagebox.showerror("Error", f"Failed to process the request: {e}")


    #Re-reun thought compression (train model on human-preferred thought compression)


    root.mainloop()

create_target_layout()