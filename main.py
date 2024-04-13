import hashlib
import os

# testing
file_path = "birthday.mp4"

def calculate_chunk_hash(file_path, chunk_size=1024):
  pass

def verify_chunk(file_path, chunk_index, expected_hash, chunk_size=1024):
  pass

def read_chunks(file_object, chunk_size=1024):
  while True:
    data = file_object.read(chunk_size)
    if not data:
      break
    yield data

def bytes_to_bits(byte_data):
  return ''.join(format(byte, "08b") for byte in byte_data)

def read_file(file_path):
  with open(file_path, "rb") as file:
    for chunk in read_chunks(file):
      # TODO: implement hashing and checking each chunks
      pass
      
if __name__ == "__main__":
  pass