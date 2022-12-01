#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Team 6 Serial Dilution

 

import opentrons

import opentrons.execute

from opentrons import protocol_api

 

metadata = {'apiLevel': '2.7'}

def run(protocol: protocol_api.ProtocolContext):

    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 1)

    reservoir = protocol.load_labware('nest_12_reservoir_15ml', 2)

    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 3)

    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tips])

    row = plate.rows()[0]

    p300.pick_up_tip()

    p300.transfer(100, reservoir['A1'], row[1:], new_tip='never')

    p300.blow_out()

    p300.transfer(200, reservoir['A2'], row[0], new_tip='never')

    p300.blow_out()

    p300.transfer(100, row[:10], row[1:11], mix_after=(3, 50), new_tip='never')

    p300.aspirate(100, row[10])

    p300.drop_tip() 

