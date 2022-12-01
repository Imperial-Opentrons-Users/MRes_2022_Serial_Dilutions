from opentrons import protocol_api

metadata = {'apiLevel':'2.7'}

#protocol = simulate.get_protocol_api('2.7')

def run(protocol: protocol_api.ProtocolContext):

    # identifies the types and locations of tips, reservoir, and 96 well plate
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', 2)
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 3)

    # identifies multi channel pipette in left position
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks = [tips])
    
    # puts 100ul of PBS in every column except column 1
    p300.transfer(100, reservoir['A1'], [plate.columns_by_name()[col_name]
                  for col_name in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']])

    # puts 200ul of fluorescein solution into column 1
    p300.transfer(200, reservoir['A2'], plate.columns_by_name()['1'])

    # sets the row as row A (first row)
    row = plate.rows()[0]

    # serial dilution from col 1 to 2, 2 to 3, etc. stopping at 11
    p300.transfer(100, row[:10], row[1:11], mix_after=(3,50))
    
    # removes 100ul from column 11 and dumps in reservoir col 3
    p300.transfer(100, plate.columns_by_name()['11'], reservoir['A3'])