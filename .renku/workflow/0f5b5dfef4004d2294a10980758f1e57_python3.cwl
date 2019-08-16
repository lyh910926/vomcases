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
    default: d
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
      path: ../../data/VOM_input/HowardSprings/0_benchmark/dailyweather.prn
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: linear
    inputBinding:
      position: 4
      prefix: -p
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: data/VOM_input/HowardSprings/1_benchmark-repr/dailyweather.prn
    inputBinding:
      position: 5
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_5)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_input/HowardSprings/1_benchmark-repr
    writable: true
successCodes: []
temporaryFailCodes: []
