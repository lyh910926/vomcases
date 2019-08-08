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
  input_10:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/0_benchmark/dailyweather.prn
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default: linear
    inputBinding:
      position: 11
      prefix: -p
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_12:
    default: data/VOM_input/HowardSprings/9_weather/dailyweather.prn
    inputBinding:
      position: 12
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
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
    default: T.Max
    inputBinding:
      position: 3
      prefix: --var
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: T.Min
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: Rain
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: Radn
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: VP
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: Pres
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: d
    inputBinding:
      position: 9
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_12)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_input/HowardSprings/9_weather
    writable: true
successCodes: []
temporaryFailCodes: []
