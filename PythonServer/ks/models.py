# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECellType(Enum):
	Empty = 0
	DestroyableBlock = 1
	UndestroyableBlock = 2


class Cell(object):

	@staticmethod
	def name():
		return 'Cell'


	def __init__(self, type=None):
		self.initialize(type)
	

	def initialize(self, type=None):
		self.type = type
	

	def serialize(self):
		s = b''
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('B', self.type.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.type
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			self.type = ECellType(tmp1)
		else:
			self.type = None
		
		return offset


class Bomberman(object):

	@staticmethod
	def name():
		return 'Bomberman'


	def __init__(self, x=None, y=None, bomb_level=None, is_dead=None):
		self.initialize(x, y, bomb_level, is_dead)
	

	def initialize(self, x=None, y=None, bomb_level=None, is_dead=None):
		self.x = x
		self.y = y
		self.bomb_level = bomb_level
		self.is_dead = is_dead
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('B', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('B', self.y)
		
		# serialize self.bomb_level
		s += b'\x00' if self.bomb_level is None else b'\x01'
		if self.bomb_level is not None:
			s += struct.pack('B', self.bomb_level)
		
		# serialize self.is_dead
		s += b'\x00' if self.is_dead is None else b'\x01'
		if self.is_dead is not None:
			s += struct.pack('?', self.is_dead)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.x = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.x = None
		
		# deserialize self.y
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.y = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.y = None
		
		# deserialize self.bomb_level
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.bomb_level = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.bomb_level = None
		
		# deserialize self.is_dead
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.is_dead = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_dead = None
		
		return offset


class Bomb(object):

	@staticmethod
	def name():
		return 'Bomb'


	def __init__(self, x=None, y=None, timer=None, level=None):
		self.initialize(x, y, timer, level)
	

	def initialize(self, x=None, y=None, timer=None, level=None):
		self.x = x
		self.y = y
		self.timer = timer
		self.level = level
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('B', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('B', self.y)
		
		# serialize self.timer
		s += b'\x00' if self.timer is None else b'\x01'
		if self.timer is not None:
			s += struct.pack('B', self.timer)
		
		# serialize self.level
		s += b'\x00' if self.level is None else b'\x01'
		if self.level is not None:
			s += struct.pack('B', self.level)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.x = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.x = None
		
		# deserialize self.y
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.y = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.y = None
		
		# deserialize self.timer
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.timer = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.timer = None
		
		# deserialize self.level
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.level = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.level = None
		
		return offset


class Explosion(object):

	@staticmethod
	def name():
		return 'Explosion'


	def __init__(self, x=None, y=None):
		self.initialize(x, y)
	

	def initialize(self, x=None, y=None):
		self.x = x
		self.y = y
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('B', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('B', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.x = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.x = None
		
		# deserialize self.y
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.y = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.y = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, board=None, bombermans=None, bombs=None, explosions=None, explosion_radiuses=None):
		self.initialize(board, bombermans, bombs, explosions, explosion_radiuses)
	

	def initialize(self, board=None, bombermans=None, bombs=None, explosions=None, explosion_radiuses=None):
		self.board = board
		self.bombermans = bombermans
		self.bombs = bombs
		self.explosions = explosions
		self.explosion_radiuses = explosion_radiuses
	

	def serialize(self):
		s = b''
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			tmp12 = b''
			tmp12 += struct.pack('I', len(self.board))
			while len(tmp12) and tmp12[-1] == b'\x00'[0]:
				tmp12 = tmp12[:-1]
			s += struct.pack('B', len(tmp12))
			s += tmp12
			
			for tmp13 in self.board:
				s += b'\x00' if tmp13 is None else b'\x01'
				if tmp13 is not None:
					tmp14 = b''
					tmp14 += struct.pack('I', len(tmp13))
					while len(tmp14) and tmp14[-1] == b'\x00'[0]:
						tmp14 = tmp14[:-1]
					s += struct.pack('B', len(tmp14))
					s += tmp14
					
					for tmp15 in tmp13:
						s += b'\x00' if tmp15 is None else b'\x01'
						if tmp15 is not None:
							s += tmp15.serialize()
		
		# serialize self.bombermans
		s += b'\x00' if self.bombermans is None else b'\x01'
		if self.bombermans is not None:
			tmp16 = b''
			tmp16 += struct.pack('I', len(self.bombermans))
			while len(tmp16) and tmp16[-1] == b'\x00'[0]:
				tmp16 = tmp16[:-1]
			s += struct.pack('B', len(tmp16))
			s += tmp16
			
			for tmp17 in self.bombermans:
				s += b'\x00' if tmp17 is None else b'\x01'
				if tmp17 is not None:
					tmp18 = b''
					tmp18 += struct.pack('I', len(tmp17))
					while len(tmp18) and tmp18[-1] == b'\x00'[0]:
						tmp18 = tmp18[:-1]
					s += struct.pack('B', len(tmp18))
					s += tmp18
					
					s += tmp17.encode('ISO-8859-1') if PY3 else tmp17
				s += b'\x00' if self.bombermans[tmp17] is None else b'\x01'
				if self.bombermans[tmp17] is not None:
					s += self.bombermans[tmp17].serialize()
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp19 = b''
			tmp19 += struct.pack('I', len(self.bombs))
			while len(tmp19) and tmp19[-1] == b'\x00'[0]:
				tmp19 = tmp19[:-1]
			s += struct.pack('B', len(tmp19))
			s += tmp19
			
			for tmp20 in self.bombs:
				s += b'\x00' if tmp20 is None else b'\x01'
				if tmp20 is not None:
					tmp21 = b''
					tmp21 += struct.pack('I', len(tmp20))
					while len(tmp21) and tmp21[-1] == b'\x00'[0]:
						tmp21 = tmp21[:-1]
					s += struct.pack('B', len(tmp21))
					s += tmp21
					
					s += tmp20.encode('ISO-8859-1') if PY3 else tmp20
				s += b'\x00' if self.bombs[tmp20] is None else b'\x01'
				if self.bombs[tmp20] is not None:
					tmp22 = b''
					tmp22 += struct.pack('I', len(self.bombs[tmp20]))
					while len(tmp22) and tmp22[-1] == b'\x00'[0]:
						tmp22 = tmp22[:-1]
					s += struct.pack('B', len(tmp22))
					s += tmp22
					
					for tmp23 in self.bombs[tmp20]:
						s += b'\x00' if tmp23 is None else b'\x01'
						if tmp23 is not None:
							s += tmp23.serialize()
		
		# serialize self.explosions
		s += b'\x00' if self.explosions is None else b'\x01'
		if self.explosions is not None:
			tmp24 = b''
			tmp24 += struct.pack('I', len(self.explosions))
			while len(tmp24) and tmp24[-1] == b'\x00'[0]:
				tmp24 = tmp24[:-1]
			s += struct.pack('B', len(tmp24))
			s += tmp24
			
			for tmp25 in self.explosions:
				s += b'\x00' if tmp25 is None else b'\x01'
				if tmp25 is not None:
					s += tmp25.serialize()
		
		# serialize self.explosion_radiuses
		s += b'\x00' if self.explosion_radiuses is None else b'\x01'
		if self.explosion_radiuses is not None:
			tmp26 = b''
			tmp26 += struct.pack('I', len(self.explosion_radiuses))
			while len(tmp26) and tmp26[-1] == b'\x00'[0]:
				tmp26 = tmp26[:-1]
			s += struct.pack('B', len(tmp26))
			s += tmp26
			
			for tmp27 in self.explosion_radiuses:
				s += b'\x00' if tmp27 is None else b'\x01'
				if tmp27 is not None:
					s += struct.pack('I', tmp27)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.board
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp30 = s[offset:offset + tmp29]
			offset += tmp29
			tmp30 += b'\x00' * (4 - tmp29)
			tmp31 = struct.unpack('I', tmp30)[0]
			
			self.board = []
			for tmp32 in range(tmp31):
				tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp34:
					tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp36 = s[offset:offset + tmp35]
					offset += tmp35
					tmp36 += b'\x00' * (4 - tmp35)
					tmp37 = struct.unpack('I', tmp36)[0]
					
					tmp33 = []
					for tmp38 in range(tmp37):
						tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp40:
							tmp39 = Cell()
							offset = tmp39.deserialize(s, offset)
						else:
							tmp39 = None
						tmp33.append(tmp39)
				else:
					tmp33 = None
				self.board.append(tmp33)
		else:
			self.board = None
		
		# deserialize self.bombermans
		tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp41:
			tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp43 = s[offset:offset + tmp42]
			offset += tmp42
			tmp43 += b'\x00' * (4 - tmp42)
			tmp44 = struct.unpack('I', tmp43)[0]
			
			self.bombermans = {}
			for tmp45 in range(tmp44):
				tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp48:
					tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp50 = s[offset:offset + tmp49]
					offset += tmp49
					tmp50 += b'\x00' * (4 - tmp49)
					tmp51 = struct.unpack('I', tmp50)[0]
					
					tmp46 = s[offset:offset + tmp51].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp51]
					offset += tmp51
				else:
					tmp46 = None
				tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp52:
					tmp47 = Bomberman()
					offset = tmp47.deserialize(s, offset)
				else:
					tmp47 = None
				self.bombermans[tmp46] = tmp47
		else:
			self.bombermans = None
		
		# deserialize self.bombs
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp55 = s[offset:offset + tmp54]
			offset += tmp54
			tmp55 += b'\x00' * (4 - tmp54)
			tmp56 = struct.unpack('I', tmp55)[0]
			
			self.bombs = {}
			for tmp57 in range(tmp56):
				tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp60:
					tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp62 = s[offset:offset + tmp61]
					offset += tmp61
					tmp62 += b'\x00' * (4 - tmp61)
					tmp63 = struct.unpack('I', tmp62)[0]
					
					tmp58 = s[offset:offset + tmp63].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp63]
					offset += tmp63
				else:
					tmp58 = None
				tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp64:
					tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp66 = s[offset:offset + tmp65]
					offset += tmp65
					tmp66 += b'\x00' * (4 - tmp65)
					tmp67 = struct.unpack('I', tmp66)[0]
					
					tmp59 = []
					for tmp68 in range(tmp67):
						tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp70:
							tmp69 = Bomb()
							offset = tmp69.deserialize(s, offset)
						else:
							tmp69 = None
						tmp59.append(tmp69)
				else:
					tmp59 = None
				self.bombs[tmp58] = tmp59
		else:
			self.bombs = None
		
		# deserialize self.explosions
		tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp71:
			tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp73 = s[offset:offset + tmp72]
			offset += tmp72
			tmp73 += b'\x00' * (4 - tmp72)
			tmp74 = struct.unpack('I', tmp73)[0]
			
			self.explosions = []
			for tmp75 in range(tmp74):
				tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp77:
					tmp76 = Explosion()
					offset = tmp76.deserialize(s, offset)
				else:
					tmp76 = None
				self.explosions.append(tmp76)
		else:
			self.explosions = None
		
		# deserialize self.explosion_radiuses
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp80 = s[offset:offset + tmp79]
			offset += tmp79
			tmp80 += b'\x00' * (4 - tmp79)
			tmp81 = struct.unpack('I', tmp80)[0]
			
			self.explosion_radiuses = []
			for tmp82 in range(tmp81):
				tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp84:
					tmp83 = struct.unpack('I', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp83 = None
				self.explosion_radiuses.append(tmp83)
		else:
			self.explosion_radiuses = None
		
		return offset
