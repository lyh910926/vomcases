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
      path: ../../data/Silo/howard.txt
    inputBinding:
      position: 2
      prefix: --meteofile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: Pres
    inputBinding:
      position: 3
      prefix: --var
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: d
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
      path: ../../data/VOM_input/HowardSprings/0_benchmark/dailyweather.prn
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
    default: 1-1-1980
    inputBinding:
      position: 7
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: 31-12-2005
    inputBinding:
      position: 8
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: data/VOM_input/HowardSprings/6_atm/dailyweather.prn
    inputBinding:
      position: 9
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_9)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_input/HowardSprings/6_atm
    writable: true
successCodes: []
temporaryFailCodes: []
