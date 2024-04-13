import hashlib
import os

# input file
file_path = "birthday.mp4"

def chunk_hash(chunk_data):
  hash_object = hashlib.sha256()
  hash_object.update(chunk_data)
  return hash_object.digest()

def verify_chunk(file_path, chunk_index, expected_hash, chunk_size=1024):
  pass

def read_chunks(file_object, chunk_size=1024):
  while True:
    data = file_object.read(chunk_size)
    if not data:
      break
    yield data
    
def read_chunks_reversed(file_path, chunk_size=1024):
  with open(file_path, "rb") as file:
    file.seek(0, 2)
    file_size = file.tell()
    remaining_bytes = file_size
    while remaining_bytes > 0:
      start_pos = max(0, file_size - chunk_size)
      bytes_to_read = min(remaining_bytes, chunk_size)
      file.seek(start_pos)
      chunk = file.read(bytes_to_read)
      print(chunk)
      remaining_bytes -= bytes_to_read
      file_size = start_pos

def bytes_to_bits(byte_data):
  return ''.join(format(byte, "08b") for byte in byte_data)

def bits_to_bytes(bits):
  int_value = int(bits, 2)
  num_bytes = (len(bits) + 7) 
  return int_value.to_bytes(num_bytes, 'big')

def hash_file(file_path):
  data_list = []
  with open(file_path, "rb") as file:
    for chunk in read_chunks(file):
      data_list.append(chunk)
  return data_list

if __name__ == "__main__":
  prev_hash = None
  curr_hash = None
  for data in hash_file(file_path)[::-1]:
    curr_hash = chunk_hash(data) if not prev_hash else chunk_hash(data + prev_hash)
    prev_hash = curr_hash
  print(curr_hash.hex())