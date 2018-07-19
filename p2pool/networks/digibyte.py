from p2pool.bitcoin import networks

PARENT = networks.nets['digibyte']
SHARE_PERIOD = 40
CHAIN_LENGTH = 1*24*60
REAL_CHAIN_LENGTH = 1*24*60
TARGET_LOOKBEHIND = 100
SPREAD = 30
IDENTIFIER = '309A27228C3652C6'.decode('hex')
PREFIX = '309A132050FC3477'.decode('hex')
P2P_PORT = 5026
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5027
BOOTSTRAP_ADDRS = 'triplezen.tk'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 6160200 <= v else 'DigiByte version too old. Upgrade to 6.16.2 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
