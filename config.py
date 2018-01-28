import json
import logging

# Configuration with default values
import configargparse
import sys

log = logging.getLogger(__name__)

cfg = {
    'host': '127.0.0.1',
    'port': 4242,
    'db_host': 'localhost',
    'db_port': 3306,
    'db_name': '',
    'db_user': '',
    'db_pass': '',
    'db_max_connections': 20,
    'log_updates': True,
    'account_release_timeout': 120,     # Accounts are being released automatically after this many minutes from last update
    'max_queue_size': 50                # Block update requests if queue already has this many items
}


def cfg_get(key, default=None):
    return cfg.get(key, default)

# ===========================================================================

parser = configargparse.ArgParser()
parser.add_argument('-c', '--config',
                    help=('Specify different config file. Default: config.json'),
                    default='config.json')
parser.add_argument('-i', '--import-csv',
                    help=('Filename of a CSV file to import accounts from.'),
                    default=None)
parser.add_argument('-l', '--level',
                    help=('Trainer level of imported accounts.'),
                    type=int, default=None)
parser.add_argument('-s', '--system',
                    help=('System ID.'),
                    default=None)
parser.add_argument('-cnd', '--condition',
                    help=('Account condition of imported accounts. One of [unknown, good, banned, blind, captcha]. Default: unknown'),
                    default='unknown')
parser.add_argument('-a', '--api',
                    help=('Shuffle PTC Account API.'),
                    default=None)
parser.add_argument('-n', '--number',
                    help=('Number of accounts to get from Shuffle Database.'),
                    type=int, default=None)
parser.add_argument('-h', '--hour',
                    help=('Check records <x> hours before since the checking time.'),
                    type=int, default=0)
parser.add_argument('-d', '--delay',
                    help=('Delay between each extraction. Default 12 hours (unit in hour).'),
                    type=int, default=12)

args = parser.parse_args()

args.condition = args.condition.lower()
if args.condition != 'unknown' and not args.level:
    log.error("You must also specify a trainer level with --level if you force an account condition with --condition.")
    sys.exit(1)
elif args.api is None:
	log.error("You must specify Shuffle PTC Account API using -a or --api")
	sys.exit(1)
elif args.level is None:
	log.error("You must specify account level using -l or --level")
	sys.exit(1)
elif args.number is None:	
	log.error("You must specify extraction amount using -n or --number")
	sys.exit(1)

with open(args.config, 'r') as f:
    user_cfg = json.loads(f.read())
    cfg.update(user_cfg)
