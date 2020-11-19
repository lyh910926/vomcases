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
      path: ../../src_py/benchmarking.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/DINGO/Ea_sturt.txt
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default: data/emp_benchmarks/emp1_ade
    inputBinding:
      position: 13
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: Radn
    inputBinding:
      position: 14
      prefix: --var
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/Silo/adelaide.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: x
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
      path: ../../data/Silo/daly.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../data/Silo/dry.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/Silo/howard.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/Silo/sturt.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default: y
    inputBinding:
      position: 8
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_13)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/emp_benchmarks
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/benchmarking.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/Silo/adelaide.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/Silo/daly.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/Silo/dry.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/Silo/howard.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/Silo/sturt.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO/Ea_dry.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/DINGO/Ea_sturt.txt
    writable: false
successCodes: []
temporaryFailCodes: []
