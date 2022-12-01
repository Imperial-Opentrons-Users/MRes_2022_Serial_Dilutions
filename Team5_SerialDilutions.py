#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from opentrons import protocol_api

metadata = {'apiLevel': '2.8',
           'protocollName': 'Serial Dilution Protocol',
           'author': 'Team 5'}

def run(protocol: protocol_api.ProtocolContext):

#Labware
    reservoir = protocol.load_labware('4ti0131_12_reservoir_21000ul', 1)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    plate = protocol.load_labware('costar3370flatbottomtransparent_96_wellplate_200ul', 3)

#liquids
    PBS = reservoir['A1']
    Fluorescine = reservoir['A2']

#pipettes
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack_1])
#     protocol.max_speeds['Z'] = 10

#commands
    row = plate.rows()[0]
    #pbs addition
    p300.transfer(100, PBS, row[1:], blow_out='always', blowout_location = 'destination well', touch_tip=True)
    #fluorescine addition
    p300.transfer(100, Fluorescine, row[0:2], mix_after(3,50), blow_out='always', blowout_location = 'destination well',touch_tip=True)
    #serial dilution 
    p300.transfer(100, row[1:10], row[2:11], mix_after=(3,50), blow_out='always', blowout_location = 'destination well',touch_tip=True, new_tip = 'always')
    #waste removal   
    p300.pick_up_tip()
    p300.aspirate(100, row[10])
    p300.drop_tip()

