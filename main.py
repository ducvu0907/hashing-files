import hashlib

# helper function for hashing data using sha256
def hash_data(data):
  hash_object = hashlib.sha256()
  hash_object.update(data)
  return hash_object.digest()

# read chunks to hash
def read_chunks(file_object, chunk_size=1024):
  while True:
    chunk = file_object.read(chunk_size)
    if not chunk:
      break
    yield chunk
    
# hash each chunks
def hash_file(file_path, chunk_size=1024):
  chunk_list = []
  with open(file_path, "rb") as file:
    for chunk in read_chunks(file, chunk_size):
      chunk_list.append(chunk)
  prev_hash = None
  h0 = None
  file_blocks = chunk_list[:]
  for idx, chunk in enumerate(chunk_list[::-1]):
    curr_hash = hash_data(chunk + prev_hash) if prev_hash else hash_data(chunk)
    prev_hash = curr_hash
    h0 = curr_hash.hex()
  return file_blocks, h0

# read and verify each block
def verify_blocks(file_blocks, h0, chunk_size=1024):
  def read_blocks():
    for block in file_blocks:
      yield block
  h = h0
  for block in read_blocks(file_blocks):
    pass
  print("File is clean")

if __name__ == "__main__":
  file_path = "test_file/birthday.mp4"
  chunk_size = 1024
  file_blocks, h0 = hash_file(file_path, chunk_size)
  print(h0)