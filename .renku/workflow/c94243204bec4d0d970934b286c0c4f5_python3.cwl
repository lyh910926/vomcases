arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/model_stats.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default: o
    inputBinding:
      position: 11
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_12:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default: 5
    inputBinding:
      position: 13
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: 9
    inputBinding:
      position: 14
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default: w
    inputBinding:
      position: 15
      prefix: -s
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_16:
    default: 12
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_17:
    default: w
    inputBinding:
      position: 17
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: 3
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: o
    inputBinding:
      position: 19
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/DalyRiverUncleared.csv
    inputBinding:
      position: 2
      prefix: --bess
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default: d
    inputBinding:
      position: 21
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default: data/SavMIP_stats/BESS/DalyUncleared
    inputBinding:
      position: 23
      prefix: --out_bess
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_24:
    default: data/SavMIP_stats/BIOS2/DalyUncleared
    inputBinding:
      position: 24
      prefix: --out_bios2
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_25:
    default: data/SavMIP_stats/LPJGUESS/DalyUncleared
    inputBinding:
      position: 25
      prefix: --out_lpjguess
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_26:
    default: data/SavMIP_stats/MAESPA/DalyUncleared
    inputBinding:
      position: 26
      prefix: --out_maespa
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_27:
    default: data/SavMIP_stats/SPA/DalyUncleared
    inputBinding:
      position: 27
      prefix: --out_spa
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_28:
    default: data/SavMIP_stats/CABLE/DalyUncleared
    inputBinding:
      position: 28
      prefix: --out_cable
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/DalyRiverUncleared_ET_GPP.csv
    inputBinding:
      position: 3
      prefix: --bios2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_et_eco.txt
    inputBinding:
      position: 4
      prefix: --lpjguess
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_gpp_eco.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/DalyRiverUncleared_savannas_maespa_simulation.csv
    inputBinding:
      position: 6
      prefix: --maespa
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/dalyriveruncleared_hourly_outputs.csv
    inputBinding:
      position: 7
      prefix: --spa
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/DalyRiverUncleared_CABLE.nc
    inputBinding:
      position: 8
      prefix: --cable
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: o
    inputBinding:
      position: 9
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_23)
    streamable: false
    type: Directory
  output_1:
    outputBinding:
      glob: $(inputs.input_24)
    streamable: false
    type: Directory
  output_2:
    outputBinding:
      glob: $(inputs.input_25)
    streamable: false
    type: Directory
  output_3:
    outputBinding:
      glob: $(inputs.input_26)
    streamable: false
    type: Directory
  output_4:
    outputBinding:
      glob: $(inputs.input_27)
    streamable: false
    type: Directory
  output_5:
    outputBinding:
      glob: $(inputs.input_28)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/BESS/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/BIOS2/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/LPJGUESS/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/MAESPA/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/SPA/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/CABLE/DalyUncleared
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/model_stats.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/SavMIP_extracted/SavMIP/BESS/DalyRiverUncleared.csv
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/DalyRiverUncleared_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_et_eco.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/DalyRiverUncleared_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/dalyriveruncleared_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/DalyRiverUncleared_CABLE.nc
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
