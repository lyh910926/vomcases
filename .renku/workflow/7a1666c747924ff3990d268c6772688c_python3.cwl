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
      path: ../../src_py/adj_dailyweather.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/MaunaLoa/weekly_in_situ_co2_mlo.csv
    inputBinding:
      position: 2
      prefix: --co2file
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: d
    inputBinding:
      position: 3
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/0_benchmark/dailyweather.prn
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default: linear
    inputBinding:
      position: 5
      prefix: -p
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: data/VOM_input/HowardSprings/4_co2_var/dailyweather.prn
    inputBinding:
      position: 6
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_6)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_input/HowardSprings/4_co2_var
    writable: true
successCodes: []
temporaryFailCodes: []
