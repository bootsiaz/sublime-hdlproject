

import os
import sys
import getopt
try:
  import openai
except Exception as e:
  print('ERROR: ' + str(e))
  print('Please install from command line: ')
  print('  pip install --upgrade openai')
  print(' OR ')
  print('  pip3 install --upgrade openai')
  print(' OR ')
  print('  python3 -m pip install openai')

def chat_gpt_request(model, system_content, request):

  try:
    response = openai.ChatCompletion.create(
      model=model,
      messages=[
          {"role": "system", "content": system_content},
          {"role": "user", "content": request},
      ],
      temperature=0,
    )
  except Exception as e:
    print('ERROR: ' + str(e))
    
  return response



def main():

  api_key = None
  organization = None
  model = None
  system_content = None
  request_file = None

  try:
    opts, args = getopt.getopt(sys.argv[1:],'ha:o:m:s:r:')
  except getopt.GetoptError:
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      # usage()
      sys.exit()
    elif opt == '-a':
      api_key = arg   
    elif opt == '-o':
      organization = arg     
    elif opt == '-m':
      model = arg
    elif opt == '-s':
      system_content = arg
    elif opt == '-r':
      request_file = arg

  openai.api_key = api_key
  openai.organization = organization

  with open(request_file, "r") as f:
    request = f.read()

  response = chat_gpt_request(model, system_content, request)

  print(response['choices'][0]['message']['content'])

  print()
  print('  -- chatgpt_request info -- ')
  print('total tokens: ' + str(response['usage']['total_tokens']))
  print()

  if response['choices'][0]['finish_reason'] == 'length':
    print()
    print('Incomplete model output.')

    if response['usage']['total_tokens'] > 4096:
      print('Total number of tokens in request and message exceed amount allowed by chatgpt: 4096')
      print('Try creating a shorter request.')

  sys.exit()


if __name__ == "__main__":
  main()   




