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
      path: ../../src_py/write_dailyweather.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default: m
    inputBinding:
      position: 2
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/Silo/daly.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: c
    inputBinding:
      position: 4
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/MaunaLoa/weekly_in_situ_co2_mlo.csv
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: linear
    inputBinding:
      position: 6
      prefix: -p
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: work/DalyUncleared/freedrainage_cpcff0.2/params_nf0.2/input/dailyweather.prn
    inputBinding:
      position: 7
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_7)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/DalyUncleared/freedrainage_cpcff0.2/params_nf0.2/input
    writable: true
successCodes: []
temporaryFailCodes: []
