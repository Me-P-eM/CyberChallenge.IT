from pwn import remote
import traceback

# CONNECTION
HOST = "***"
PORT = 10015

# HEADER (5 bytes)
TRANSFER_FRAME_VERSION_NUMBER = "00"			# 2 bits - recommended for standard
BYPASS_FLAG = "1"								# 1 bit - to bypass frame acceptance checks (Type-B)
CONTROL_COMMAND_FLAG = "0"						# 1 bit - data frame, not control frame (Type-D)
RESERVED_SPARE = "00"							# 2 bits - reserved for future use
SPACECRAFT_ID = bin(69)[2:].zfill(10)			# 10 bits - got from connection
VIRTUAL_CHANNEL_ID = bin(55)[2:].zfill(6)		# 6 bits - got from connection
FRAME_LENGTH = bin(11)[2:].zfill(10)			# 10 bits - number of bytes in header (5) + payload (7) - 1
FRAME_SEQUENCE_NUMBER = bin(0)[2:].zfill(8)		# 8 bits - all zeros because of Type-B
HEADER = (TRANSFER_FRAME_VERSION_NUMBER +		# 5 bytes
          BYPASS_FLAG +
          CONTROL_COMMAND_FLAG +
          RESERVED_SPARE +
          SPACECRAFT_ID +
          VIRTUAL_CHANNEL_ID +
          FRAME_LENGTH +
          FRAME_SEQUENCE_NUMBER)

#PAYLOAD
BODY = "GETFLAG".encode()						# 7 bytes

# PADDING
PACKET_SIZE = 0x1be								# expected from challenge

def createTcFrameWithoutFecf():
	"""Create TC Transfer Frame without FECF"""
	headerInt = int(HEADER, 2)
	headerBytes = headerInt.to_bytes(5, byteorder="big")
	tcFrameWithoutFecf = headerBytes + BODY
	return tcFrameWithoutFecf

def calculateCrc16(data):
	"""Calculate CRC-16 using CCSDS standard polynomial"""
	# CCSDS CRC-16: G(X) = X^16 + X^12 + X^5 + 1 = 0x1021
	poly = 0x1021
	crc = 0xFFFF 	# Initialize to all 1s (preset)
	for byte in data:
		crc ^= (byte << 8)
		for _ in range(8):
			if crc & 0x8000:
				crc = (crc << 1) ^ poly
			else:
				crc <<= 1
			crc &= 0xFFFF
	return crc.to_bytes(2, byteorder="big")

if __name__ == "__main__":
	print("Connecting to CCSDS satellite channel coding tap...")
	try:
		r = remote(HOST, PORT)
		# Create the TC Transfer Frame
		print("Creating TC Transfer Frame...")
		tcWithoutFecf = createTcFrameWithoutFecf()
		print("Calculating CRC-16...")
		fecf = calculateCrc16(tcWithoutFecf)
		tcTransferFramePadded = (tcWithoutFecf + fecf).ljust(PACKET_SIZE, b'\x00')
		# Send the TC Transfer Frame
		print("Sending TC Transfer Frame...")
		r.sendafter(b'N', tcTransferFramePadded)
		# Receive the flag
		print("Receiving flag...")
		response = r.recvuntil(b"d0wnl1nk")
		flag = response.decode('latin-1').split('First part of the flag is ')[1].strip()
		print(f"{flag}")
		r.close()
	except Exception as e:
		print(f"Error: {e}")
		r.close()
		traceback.print_exc()
