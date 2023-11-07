# --------------------------------------------------------------------
# test.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Tuesday November 7, 2023
# --------------------------------------------------------------------

import waterlog

waterlog.setup()
waterlog.set_level(waterlog.DEBUG)

if __name__ == '__main__':
    waterlog.info("Hello, world!")
