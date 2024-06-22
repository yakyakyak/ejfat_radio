#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: EJFAT UDP Source
# Author: yak
# GNU Radio version: 3.10.9.2

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import network
from test_core import test_core  # grc-generated hier_block




class test_ejfat_udp_source(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "EJFAT UDP Source", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.test_core_0 = test_core(
            samp_rate=10000,
        )
        self.network_udp_sink_0 = network.udp_sink(gr.sizeof_gr_complex, 1, '127.0.0.1', 2000, 0, 1472, False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.test_core_0, 0), (self.network_udp_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=test_ejfat_udp_source, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
